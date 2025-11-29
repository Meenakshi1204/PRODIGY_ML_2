# recommendations.py

def give_business_tips(data):
    """Provide business improvement suggestions for each cluster"""

    print("\n📈 Business Improvement Tips Based on Cluster Analysis:\n")

    summary = data.groupby('Cluster')[['Age', 'Annual Income (k$)', 'Spending Score (1-100)']].mean()

    for cluster_id, row in summary.iterrows():
        income = row['Annual Income (k$)']
        spend = row['Spending Score (1-100)']
        age = row['Age']

        print(f"\n💬 Cluster {cluster_id} (Avg Age: {age:.1f}, Income: {income:.1f}k$, Spending: {spend:.1f})")

        # Give smart, data-driven tips
        if income > 70 and spend > 60:
            print("→ These are premium customers. Offer exclusive memberships or loyalty rewards to retain them.")
        elif income > 70 and spend < 40:
            print("→ High-income but low-spending. Promote luxury products and personalized offers to boost spending.")
        elif income < 40 and spend > 60:
            print("→ Low-income but high-spending. Introduce affordable premium plans or referral discounts.")
        elif income < 40 and spend < 40:
            print("→ Low-income and low-spending. Attract with combo offers or festive discounts to increase sales.")
        else:
            print("→ Mid-range customers. Maintain their engagement with balanced deals and seasonal sales.")
