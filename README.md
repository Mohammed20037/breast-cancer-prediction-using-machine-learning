# Breast Cancer Prediction using Support Vector Machine (SVM)


## Overview

This GitHub repository hosts a breast cancer prediction project that utilizes Support Vector Machine (SVM) with an impressive 99% accuracy rate. Breast cancer prediction is a crucial task in the medical field, and this project demonstrates how machine learning can be used to assist in early diagnosis.

## Table of Contents

- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Jupyter Notebook Analysis](#jupyter-notebook-analysis)
  - [Dependencies](#dependencies)
  - [Code Sections](#code-sections)
- [Graphical User Interface (GUI)](#graphical-user-interface-gui)
- [Dataset](#dataset)
- [Usage](#usage)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Project Structure

The project is structured as follows:

- **Jupyter Notebook (`breast_cancer_prediction.ipynb`)**: This notebook contains comprehensive data analysis, model training, and evaluation. It includes code sections for data preprocessing, model selection, hyperparameter tuning, and performance evaluation.

- **GUI (`gui.py`)**: The graphical user interface provides an intuitive way for users to make predictions using the trained SVM model. It simplifies the prediction process for medical practitioners and researchers.

- **Dataset (`data.csv`)**: The dataset used for training and testing the model. It has been preprocessed to ensure compatibility with the project.

- **Images (`images/`)**: This directory contains relevant images, including data visualizations and the breast cancer awareness ribbon.

## Getting Started

### Prerequisites

Before running the project, make sure you have the following prerequisites installed:

- Python 3.x
- Jupyter Notebook (for running the analysis)
- Required Python libraries (listed in the Jupyter Notebook section)

### Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/breast-cancer-prediction.git
   ```

2. Install the required Python libraries by running:

   ```bash
   pip install -r requirements.txt
   ```

## Jupyter Notebook Analysis

### Dependencies

The Jupyter Notebook code utilizes various Python libraries, including NumPy, pandas, Matplotlib, and Scikit-Learn. Please ensure you have these libraries installed.

### Code Sections

The Jupyter Notebook contains the following code sections:

- Importing necessary libraries and modules.
- Loading the dataset and performing initial data exploration.
- Data preprocessing, including encoding and feature selection.
- Model selection and evaluation using cross-validation.
- Hyperparameter tuning for the SVM model.
- Training and evaluating the final SVM model.

## Graphical User Interface (GUI)

The GUI (`gui.py`) simplifies breast cancer prediction for end-users. It allows users to input relevant feature values and receive a prediction based on the trained SVM model. The GUI offers a user-friendly interface for medical practitioners and researchers.

![image](https://github.com/Mohammed20037/breast-cancer-prediction-using-machine-learning/assets/113844625/d5ec82df-f95f-4c57-8b28-ee01582d6b29)


## Dataset

The dataset (`data.csv`) used in this project contains various features related to breast cancer diagnosis. It has been preprocessed and prepared for machine learning tasks.

## Usage

1. Run the Jupyter Notebook (`breast_cancer_prediction.ipynb`) to perform in-depth data analysis, model training, and evaluation.

2. To use the GUI for making predictions:

   - Execute the `gui.py` script:

     ```bash
     python gui.py
     ```

   - Input the required feature values in the GUI, and the prediction will be displayed.

## Results

The trained SVM model achieves an accuracy score of 99%, demonstrating its effectiveness in breast cancer prediction. Detailed classification reports and confusion matrices are available in the Jupyter Notebook.

## Contributing

Contributions to this project are welcome! If you have ideas for improvements, bug fixes, or new features, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

Feel free to use and modify the code for your own projects or research purposes. If you have any questions or suggestions, please don't hesitate to contact the project owner.
