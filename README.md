# 🔧 Predictive Maintenance System 🛠️

![Industrial machine](images/industrial_machine.jpg)

**Enhance operational efficiency with predictive maintenance!**

## Overview

This project leverages machine learning to forecast equipment maintenance needs based on sensor data. The system includes data generation, model training, evaluation, and result visualization.

**Note:** The data used is dummy data, but the model works effectively. With real-time data, the prediction accuracy will be significantly improved.

## Table of Contents

1. [Key Features](#key-features-✨)
2. [Dataset](#dataset-📊)
3. [Project Structure](#project-structure-📂)
4. [Setup](#setup-🚀)
5. [Usage](#usage)
6. [Results](#results-🏆)
7. [Conclusion](#conclusion)
8. [Contributing](#contributing-🤝)
9. [License](#license-📜)
10. [Contact Information](#contact-information-📧)

## Key Features ✨

- **Comprehensive Data Generation:** Simulate sensor data for various machinery.
- **Neural Network Model:** Train and evaluate a robust predictive maintenance model.
- **Detailed Evaluation Metrics:** Confusion matrix and classification report.
- **Insightful Visualizations:** Understand model performance through visual plots.

## Dataset 📊

The project uses simulated sensor data to represent different machinery operations:
- Hot Forging Machine Press 6000T
- Cold Forging Machine Press 1000T
- Hydraulic Press 10000T
- Mechanical Trimming Press 110T
- Mechanical Coining Press 145T

## Project Structure 📂

- **sensor_data.csv:** Generated dummy sensor data
- **create_dummy_data.py:** Script to generate dummy sensor data
- **predictive_maintenance.py:** Script to train and evaluate the predictive model
- **visualization.py:** Script to visualize model performance and generate conclusions
- **README.md:** This file!
- **requirements.txt:** List of Python libraries needed
- **.gitignore:** Ignored files and directories

## Setup 🚀

1. **Clone the repository:**
   ```sh
   git clone https://github.com/Nick9695/Predictive-Maintenance-System
   cd predictive-maintenance-system
   ```
2. **Create a virtual environment:** 
   ```sh
   python -m venv venv
   ```
3. **Activate the virtual environment:**
   ```sh
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```
4. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

## Usage

1. **Generate Dummy Data:**
   ```sh
   python create_dummy_data.py
   ```
   This script generates random sensor data for various machinery and saves it to `sensor_data.csv`. It also displays a sample of the generated data.

2. **Train and Evaluate the Model:**
   ```sh
   python predictive_maintenance.py
   ```
   This script loads the generated data, preprocesses it, trains a neural network model, and evaluates its performance. It also plots the training loss curve.

3. **Visualize the Results and Generate Conclusions:**
   ```sh
   python visualization.py
   ```
   This script visualizes the confusion matrix and prints a classification report. It also provides a detailed conclusion based on the model's performance.

## Results 🏆

### Confusion Matrix
![Confusion Matrix](images/confusion_matrix.png)

### Training Loss Curve
![Training Loss Curve](images/training_loss_curve.png)

## Conclusion

The predictive maintenance model demonstrates strong potential in forecasting equipment maintenance needs. Although the current dataset is simulated, the model structure and methodology are robust and will yield more accurate predictions with real-time data. Here are the key metrics:

- **Total samples:** 300
- **Accuracy:** 0.85
- **Precision:** 0.84
- **Recall:** 0.88
- **F1 Score:** 0.86

**Observations:**
- The model performs well in predicting maintenance needs with high accuracy.
- It effectively identifies most cases where maintenance is needed, ensuring minimal equipment downtime.
- The model has a low rate of false positives, indicating reliable predictions.

## Contributing 🤝

Feel free to fork this repository, experiment, and contribute your improvements! Pull requests are welcome.

## License 📜

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact Information 📧
- ![Screenshot 2023-12-11 224350](https://github.com/Nick9695/Personality-Quiz-Assignment/assets/148968130/3c82c2b7-876d-447d-b149-dcd2fddedf23)
Nikhil Raju Gadekar
-  [![gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:gernikhilgadekar@gmail.com)
---
