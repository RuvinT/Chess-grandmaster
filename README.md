# Chess Grandmaster Mimic App

Welcome to the Chess Grandmaster Mimic App! This project aims to predict the moves of chess grandmasters, evaluate moves, and predict the time taken for specific moves. The application consists of three main models: grandmaster move prediction, move evaluation, and move time prediction.

## Project Overview

- **Grandmaster Move Prediction Model:** Utilizes CNN, LSTM, and DNN to predict the next move of a chess grandmaster based on the current board position and various features.
- **Move Evaluation Model:** Uses CNN to evaluate the quality of a move.
- **Move Time Prediction Model:** Employs LSTM to predict the time a grandmaster would take to make a specific move.

The project's frontend can be accessed [here](https://ruvint.github.io/frontend-host-chess/).

## Docker Hub

The backend of the project is available as a Docker image. You can find it on Docker Hub [here](https://hub.docker.com/r/ruvinthulana/chess-app).

## Requirements

To run this project locally, you need the following dependencies:

- Flask
- Flask-Cors
- numpy
- tensorflow==2.16.1
- Keras==3.3.3
- python-chess
- h5py

You can install the required packages using `pip`:


pip install Flask Flask-Cors numpy tensorflow==2.16.1 Keras==3.3.3 python-chess h5py
Running the Application
Using Docker
Pull the Docker image:


docker pull ruvinthulana/chess-app
Run the Docker container:


