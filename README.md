# comp_astro_24

Base repository for the computational astrophysics course


# Exoplanet Detection Neural Network

## Requirements
- Python 3.x
- TensorFlow
- Pandas
- NumPy
- imbalanced-learn

## Usage
1. Set up the `parameters.yaml` file with the following structure:
    ```yaml
    train_dataset_path: "/path/to/exoTrain.csv"
    dev_dataset_path: "/path/to/exoTest.csv"
    detection_method: "nn"
    epochs: 50
    batch_size: 32
    load_model: True
    render_plot: True
    ```

2. Run the script:
    ```bash
    python NN.py
    ```

## Files
- `parameters.py`: Loads and parses configuration files.
- `NN.py`: Main script for training and evaluating the neural network.
