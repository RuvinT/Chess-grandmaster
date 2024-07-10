#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 08:37:47 2024

@author: ruvinjagoda
"""

import h5py
import numpy as np

# File paths
file1 = "./magnus_datasetv3.h5"
file2 = "./valid_processed_magnus_dataset_300000.h5"
output_file = "./valid_processed_magnus_dataset_520000.h5"

# Load data from the first file
with h5py.File(file1, "r") as hf:
    val_1_1 = np.array(hf["board_matrix"])
    val_1_2 = np.array(hf["GameID"])
    val_1_3 = np.array(hf["MoveID"])
    val_1_4 = np.array(hf["PlayerMove"])
    val_1_5 = np.array(hf["TopMoves"])
    val_1_6 = np.array(hf["BestMove"])
    val_1_7 = np.array(hf["Centipawns"])
    val_1_8 = np.array(hf["Mates"])
    val_1_9 = np.array(hf["MoveSequence"])
    

# Load data from the second file
with h5py.File(file2, "r") as hf:
    val_2_1 = np.array(hf["board_matrix"])
    val_2_2 = np.array(hf["GameID"])
    val_2_3 = np.array(hf["MoveID"])
    val_2_4 = np.array(hf["PlayerMove"])
    val_2_5 = np.array(hf["TopMoves"])
    val_2_6 = np.array(hf["BestMove"])
    val_2_7 = np.array(hf["Centipawns"])
    val_2_8 = np.array(hf["Mates"])
    val_2_9 = np.array(hf["MoveSequence"])

# Concatenate the arrays
val_1 = np.concatenate((val_1_1, val_2_1), axis=0)
val_2 = np.concatenate((val_1_2, val_2_2), axis=0)
val_3 = np.concatenate((val_1_3, val_2_3), axis=0)
val_4 = np.concatenate((val_1_4, val_2_4), axis=0)
val_5 = np.concatenate((val_1_5, val_2_5), axis=0)
val_6 = np.concatenate((val_1_6, val_2_6), axis=0)
val_7 = np.concatenate((val_1_7, val_2_7), axis=0)
val_8 = np.concatenate((val_1_8, val_2_8), axis=0)
val_9 = np.concatenate((val_1_9, val_2_9), axis=0)


# Save the concatenated arrays to a new .h5 file
with h5py.File(output_file, "w") as hf:
    hf.create_dataset("board_matrix", data=val_1)
    hf.create_dataset("GameID", data=val_2)
    hf.create_dataset("MoveID", data=val_3)
    hf.create_dataset("PlayerMove", data=val_4)
    hf.create_dataset("TopMoves", data=val_5)
    hf.create_dataset("BestMove", data=val_6)
    hf.create_dataset("Centipawns", data=val_7)
    hf.create_dataset("Mates", data=val_8)
    hf.create_dataset("MoveSequence", data=val_9)

print("Data concatenated and saved successfully")
print(f"Board matrix shape: {val_1.shape}")
print(f"GameID shape: {val_2.shape}")
print(f"MoveID shape: {val_3.shape}")
print(f"PlayerMove shape: {val_4.shape}")
print(f"TopMoves shape: {val_5.shape}")
print(f"BestMove shape: {val_6.shape}")
print(f"Centipawns shape: {val_7.shape}")
print(f"Mates shape: {val_8.shape}")
print(f"MoveSequence shape: {val_9.shape}")