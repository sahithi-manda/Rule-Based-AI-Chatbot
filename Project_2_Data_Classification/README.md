# Project 2: Data Classification Using AI 🍷🤖

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![scikit-learn](https://img.shields.io/badge/scikit--learn-Latest-orange.svg)
![Pandas](https://img.shields.io/badge/Pandas-Data_Manipulation-yellow.svg)

## 📌 Project Overview
This project demonstrates a foundational machine learning workflow for **Data Classification**. We utilize the classic **Wine Dataset** to predict the cultivar (class) of wine based on its chemical analysis. The model applied is a **Random Forest Classifier**, which is robust and effective for tabular classification tasks.

The codebase includes both a standalone Python script and an interactive Jupyter Notebook, making it versatile for both automated execution and step-by-step exploration.

## 🎯 Key Objectives
- **Data Loading & Exploration:** Import and examine the properties of the Wine dataset.
- **Data Preprocessing:** Perform a train-test split (80% training, 20% testing).
- **Model Implementation:** Initialize, train, and apply a Random Forest Classification algorithm.
- **Model Evaluation:** Measure model performance using Accuracy, Confusion Matrices, and a detailed Classification Report.

## 🛠️ Technologies Used
- **Python 3:** Core programming language.
- **pandas:** For data structure creation and visualization.
- **scikit-learn (`sklearn`):** Used for dataset loading, model selection, ensemble methods, and metric calculations.
- **Jupyter Notebook:** For interactive data analysis and step-by-step execution.

## 📊 Dataset Information
- **Source:** `sklearn.datasets.load_wine()`
- **Characteristics:** 178 samples, 13 numeric predictive attributes (features).
- **Target:** 3 classes representing different wine cultivars (`class_0`, `class_1`, `class_2`).
- **Features Include:** Alcohol, Malic acid, Ash, Alcalinity of ash, Magnesium, Total phenols, Flavanoids, Nonflavanoid phenols, Proanthocyanins, Color intensity, Hue, OD280/OD315 of diluted wines, Proline.

## 🚀 Installation & Setup

1. **Clone or Download the Repository:**
   Ensure you have the project files locally in your directory.

2. **Install Required Dependencies:**
   Make sure you have `pandas` and `scikit-learn` installed. You can install them via pip:
   ```bash
   pip install pandas scikit-learn jupyter
   ```

## 💻 Usage Instructions

You can run this project in two different ways depending on your preference:

### Option 1: Run the Python Script
For a quick, automated execution of the entire pipeline, run the Python script from your terminal:
```bash
python data_classification.py
```
This will print out the dataset shape, testing/training shapes, model accuracy, confusion matrix, and classification report directly to your console.

### Option 2: Explore via Jupyter Notebook
For a more interactive, step-by-step exploration of the data and the model training process, use the Jupyter Notebook:
```bash
jupyter notebook data_classification.ipynb
```
Execute the cells sequentially to see intermediate outputs, such as dataframes and step-by-step metric evaluations.

## 📈 Results & Evaluation Metrics
The model's performance is evaluated on a 20% holdout test set. Typical outputs include:
- **Accuracy Score:** High accuracy (> 95%) predicting the correct wine cultivar.
- **Confusion Matrix:** Provides a breakdown of true vs. predicted classifications to visualize any misclassifications.
- **Classification Report:** Detailed metrics including **Precision**, **Recall**, and **F1-Score** for each of the 3 wine classes.

## 📂 Project Structure
```text
Project_2_Data_Classification/
│
├── data_classification.py       # Main Python script with the full ML pipeline
├── data_classification.ipynb    # Interactive Jupyter Notebook equivalent
└── README.md                    # Project documentation (this file)
```
