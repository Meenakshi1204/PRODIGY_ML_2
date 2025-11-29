# insights.py
def print_cluster_insights(data):
    """Display business insights for each cluster"""
    summary = data.groupby('Cluster')[['Age', 'Annual Income (k$)', 'Spending Score (1-100)']].mean()
    print("\n📊 Cluster Summary:\n")
    print(summary)
    print("\n💡 Business Insights:")
    for i, row in summary.iterrows():
        print(f"\nCluster {i}:")
        if row['Annual Income (k$)'] > 70 and row['Spending Score (1-100)'] > 60:
            print("→ High income, high spending — Premium customers.")
        elif row['Annual Income (k$)'] > 70 and row['Spending Score (1-100)'] < 40:
            print("→ High income, low spending — Potential for upselling.")
        elif row['Annual Income (k$)'] < 40 and row['Spending Score (1-100)'] > 60:
            print("→ Low income, high spending — Loyal or budget-conscious customers.")
        else:
            print("→ Average customers — stable base group.")
