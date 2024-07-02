# Sunspot Occurrences Forecasting Using LSTM

## Project Overview

Sunspots are dark areas on the sun's surface caused by magnetic activity, which can influence solar radiation and impact Earth's climate and space weather. This project aims to forecast future sunspot occurrences using a Long Short-Term Memory (LSTM) neural network, a powerful deep learning model well-suited for time series prediction.

## Table of Contents

- [Introduction](#introduction)
- [Data](#data)
- [Model Architecture](#model-architecture)
- [Training and Evaluation](#training-and-evaluation)
- [Results](#results)

## Introduction

Sunspot activity follows an approximately 11-year solar cycle, which makes forecasting challenging due to its periodic but complex nature. Traditional statistical models often fall short in capturing these intricate patterns. This project leverages LSTM networks to provide accurate forecasts of sunspot numbers by learning from historical data.

## Data

The dataset used in this project is sourced from the [SIDC (Solar Influences Data Center)](http://www.sidc.be/silso/DATA/SN_m_tot_V2.0.txt). It includes monthly sunspot numbers spanning several centuries.

### Data Preprocessing

- **Normalization**: Sunspot counts are normalized to fall within a range suitable for neural network training.
- **Time Series Conversion**: The data is converted into sequences for input into the LSTM model.
- **Training and Testing Split**: The dataset is divided into training and testing subsets to evaluate model performance.

## Model Architecture

The LSTM model architecture used in this project consists of the following layers:

- **Input Layer**: Accepts the sequences of sunspot numbers.
- **LSTM Layers**: Two stacked LSTM layers to capture temporal dependencies in the data.
- **Dense Layer**: A fully connected layer to map the learned features to the output sunspot forecast.
- **Output Layer**: Produces the predicted sunspot count for the next time step.

### Hyperparameters

Key hyperparameters include:
- Number of LSTM units
- Number of layers
- Learning rate
- Batch size
- Sequence length

## Training and Evaluation

The model is trained on the normalized sunspot dataset using Mean Squared Error (MSE) as the loss function. Training involves iterating over the data in batches and optimizing the model weights using the Adam optimizer.

### Evaluation Metrics

- **Mean Squared Error (MSE)**: Measures the average of the squares of the errors.
- **Mean Absolute Error (MAE)**: Measures the average of the absolute differences between predicted and actual values.

## Results

The model's performance is evaluated on the test set, showing its ability to accurately forecast future sunspot occurrences. Visualizations of actual versus predicted sunspot numbers demonstrate the model's effectiveness in capturing the cyclical nature of sunspot activity.

