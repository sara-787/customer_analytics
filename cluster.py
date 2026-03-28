import sys
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

file_path = sys.argv[1]
df = pd.read_csv(file_path)

features = ['Age', 'Purchase Amount (USD)', 'Review Rating', 'Previous Purchases']
X = df[features].copy()
X.fillna(0, inplace=True)

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

kmeans = KMeans(n_clusters=4, random_state=42)
df['Cluster'] = kmeans.fit_predict(X_scaled)

cluster_counts = df['Cluster'].value_counts().sort_index()
cluster_summary = df.groupby('Cluster')[features].mean()

with open("clusters.txt", "w") as f:
    f.write("Number of samples per cluster:\n")
    for cluster, count in cluster_counts.items():
        f.write(f"Cluster {cluster}: {count} samples\n")

    f.write("\nCluster average features:\n")
    f.write(cluster_summary.to_string())

    f.write("\n\nCluster centroids (scaled):\n")
    f.write(str(kmeans.cluster_centers_))