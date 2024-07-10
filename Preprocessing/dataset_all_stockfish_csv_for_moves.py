import chess
import chess.engine
import pandas as pd
import logging
from stockfish import Stockfish
import csv
from multiprocessing import Pool, cpu_count, current_process

# Path to the Stockfish engine
engine_path = "/Users/ruvinjagoda/Desktop/Aka/AIP/Stockfish and move/stockfish/stockfish-macos-m1-apple-silicon"

# Number of moves to get from Stockfish
NUMOFMOVES = 5

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def init_engine_stockfish():
    stockfish = Stockfish(engine_path)
    stockfish.set_elo_rating(3000)
    return stockfish

def init_engine():
    # Initialize the Stockfish engine
    return chess.engine.SimpleEngine.popen_uci(engine_path)

def analyze_position(board_fen, engine, num_moves=NUMOFMOVES):
    try:
        board = chess.Board(board_fen)
        
        # Get top moves with multipv
        result = engine.analyse(board, chess.engine.Limit(depth=15), multipv=num_moves)
        
        # Extract the best moves and their principal variations (PVs)
        top_moves = []
        for move_info in result:
            move = move_info["pv"][0].uci()
            score = move_info["score"]

            # Determine centipawn and mate values
            centipawns = score.relative.score() if not score.is_mate() else 0
            mate = score.relative.mate() if score.is_mate() else 0

            top_moves.append({
                "move": move,
                "centipawns": centipawns,
                "mate": mate
            })
        
        # Generate move sequences
        move_sequence = [move.uci() for move in result[0]["pv"][:num_moves]]
        
        # Extract moves, centipawns, and mates from top_moves
        moves = [move["move"] for move in top_moves]
        centipawns = [move["centipawns"] for move in top_moves]
        mates = [move["mate"] for move in top_moves]

        return moves, moves[0], centipawns, mates, move_sequence
    except Exception as e:
        print(f"An error occurred: {e}")
        return [], None, [], [], []



def process_fens(fens_chunk):
    stockfish = init_engine_stockfish()
    engine = init_engine()

    results = []
    count = 0
    for fen in fens_chunk:
        top_moves, best_move, centipawns, mates,move_sequence = analyze_position(fen, engine)
        results.append((fen, top_moves, best_move, centipawns, mates,move_sequence))
        count+=1
        
        if count % 100 == 0:
            logging.info(f"Process {current_process().name} processed {count} FENs in current chunk")
    engine.quit()
    return results

def enhance_and_save_csv(input_filename, output_filename):
    # Read the original CSV file
    df = pd.read_csv(input_filename)
    
    fens = df["FEN"].tolist()
    
    # Split the FENs into chunks for multiprocessing
    num_cores = cpu_count()
    chunk_size = len(fens) // num_cores
    fens_chunks = [fens[i:i + chunk_size] for i in range(0, len(fens), chunk_size)]

    # Process the chunks in parallel
    with Pool(num_cores) as pool:
        results = pool.map(process_fens, fens_chunks)

    # Combine the results
    results_flat = [item for sublist in results for item in sublist]

    # Create new columns in the DataFrame
    df["TopMoves"] = [result[1] for result in results_flat]
    df["BestMove"] = [result[2] for result in results_flat]
    df["Centipawns"] = [result[3] for result in results_flat]
    df["Mates"] = [result[4] for result in results_flat]
    df["MoveSequence"] = [result[5] for result in results_flat]
    # Save the enhanced DataFrame to a new CSV file
    df.to_csv(output_filename, index=False)
    logging.info(f"Enhanced data saved to {output_filename}")

if __name__ == "__main__":
    input_filename = "./Combined_dataset.csv"
    output_filename = "./enhanced_all_player_moves_dataset.csv"
    enhance_and_save_csv(input_filename, output_filename)
    
   
    