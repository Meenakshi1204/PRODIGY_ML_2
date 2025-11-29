# visualization.py
import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D

def plot_clusters_3d(data, labels):
    """3D Cluster Visualization"""
    fig = plt.figure(figsize=(10,7))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(data['Age'], data['Annual Income (k$)'], data['Spending Score (1-100)'],
               c=labels, cmap='rainbow', s=60)
    ax.set_xlabel('Age')
    ax.set_ylabel('Annual Income (k$)')
    ax.set_zlabel('Spending Score (1-100)')
    plt.title('3D Customer Segmentation using K-Means')
    plt.show()

def plot_pairwise_clusters(data):
    """2D Pairplot to show relationships"""
    sns.pairplot(data, hue='Cluster', palette='tab10')
    plt.show()
