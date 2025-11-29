# kmeans_model.py
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt

def find_optimal_clusters(X):
    """Use the Elbow Method and Silhouette Score to find best k"""
    wcss = []
    silhouette_scores = []

    print("\n🔍 Finding the optimal number of clusters...")
    for k in range(2, 11):
        kmeans = KMeans(n_clusters=k, init='k-means++', random_state=42)
        kmeans.fit(X)
        wcss.append(kmeans.inertia_)
        silhouette_scores.append(silhouette_score(X, kmeans.labels_))
        print(f"k = {k} → Silhouette Score = {silhouette_scores[-1]:.3f}")

    # Elbow Plot
    plt.plot(range(2, 11), wcss, marker='o')
    plt.title('Elbow Method')
    plt.xlabel('Number of Clusters (k)')
    plt.ylabel('WCSS')
    plt.show()

    # Silhouette Plot
    plt.plot(range(2, 11), silhouette_scores, marker='x', color='red')
    plt.title('Silhouette Score vs k')
    plt.xlabel('Number of Clusters')
    plt.ylabel('Silhouette Score')
    plt.show()

def build_kmeans_model(X, n_clusters=5):
    """Train the KMeans model"""
    kmeans = KMeans(n_clusters=n_clusters, init='k-means++', random_state=42)
    labels = kmeans.fit_predict(X)
    print(f"\n✅ Model trained with {n_clusters} clusters.")
    return kmeans, labels
