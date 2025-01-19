# Simple Implementation of a Neural Network

This project provides a simple Python implementation of a neural network using NumPy. It demonstrates basic concepts of forward propagation, backpropagation, and parameter updates in a neural network.

## Description

The script implements a basic neural network algorithm from scratch without relying on external libraries beyond NumPy. The network adjusts weights and biases iteratively over 100 epochs to optimize the model's output.

Key features include:
- A small dataset (`X` and `y`) to illustrate matrix operations.
- Implementation of the sigmoid activation function for non-linear transformation.
- Calculation of delta and parameter updates during training.

## Code Overview

### Main Components
1. **Data Input**: 
   - `X`: Input data as a NumPy array.
   - `y`: Target values.

2. **Parameters**:
   - `sigm`: Initial sigma value used in computations.
   - `delt`: Randomly initialized delta values representing weights.

3. **Training Loop**:
   - Performs 100 iterations to update parameters.
   - Utilizes forward propagation, backpropagation, and weight adjustments.

4. **Output**:
   - Prints the transformed output of the neural network after each iteration.

### Key Functions
- **Sigmoid Function**: `1 / (1 + np.exp(-x))`
  - Applied multiple times for non-linear transformations during forward and backward passes.

- **Matrix Operations**:
  - Dot product calculations for updating weights and biases.
  - Element-wise transformations for gradients.

## Prerequisites

- Python 3.x
- NumPy library

Install NumPy if not already installed:
```bash
pip install numpy
```

## Usage

1. Save the script as `simple_nn.py`.
2. Run the script:
   ```bash
   python simple_nn.py
   ```
3. Observe the neural network's outputs for each iteration.

## Limitations

- The network lacks a clear loss function for measuring performance.
- Only demonstrates the mechanics of a simple neural network without real-world application.
- Fixed number of epochs (100) with no stopping criteria.

## Future Enhancements

- Add a loss function to track training progress.
- Enable dynamic adjustments of learning parameters.
- Introduce support for multiple layers and configurable architectures.

## License

This script is provided as-is under an open-source license. Feel free to modify and enhance it for learning and experimentation.
