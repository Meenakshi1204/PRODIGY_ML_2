# main.py
from data_preprocessing import load_data, select_features
from kmeans_model import find_optimal_clusters, build_kmeans_model
from visualization import plot_clusters_3d, plot_pairwise_clusters
from insights import print_cluster_insights
import pandas as pd
from recommendations import give_business_tips

# Step 1: Load Dataset
data = load_data("Mall_Customers.csv")

# Step 2: Select Features
X = select_features(data)

# Step 3: Find Optimal Cluster Count (Elbow + Silhouette)
find_optimal_clusters(X)

# Step 4: Build Final Model (use 5 clusters)
kmeans, labels = build_kmeans_model(X, n_clusters=5)
data['Cluster'] = labels

# Step 5: Visualize Results
plot_clusters_3d(data, labels)
plot_pairwise_clusters(data)

# Step 6: Generate Business Insights
print_cluster_insights(data)

give_business_tips(data)
