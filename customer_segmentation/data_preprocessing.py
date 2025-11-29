# data_preprocessing.py
import pandas as pd

def load_data(file_path):
    """Load and clean the dataset"""
    data = pd.read_csv(file_path)
    print("\n✅ Data Loaded Successfully!")
    print(data.head())
    return data

def select_features(data):
    """Select important features for clustering"""
    X = data[['Age', 'Annual Income (k$)', 'Spending Score (1-100)']]
    return X
