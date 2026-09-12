import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# =========================================================
# Load Data
# =========================================================
file_path = r"C:\Users\saman\Downloads\Insurance+Customer+Feedback.xlsx"
df = pd.read_excel(file_path)

print("Original Data:")
print(df.head())

print("\nNumber of rows:", len(df))


# =========================================================
# Sentiment Analysis
# Get sentiment score for each feedback using VADER sentiment analysis
# Add new column "Sentiment Score" to the DataFrame
# =========================================================
analyzer = SentimentIntensityAnalyzer()

def get_sentiment_score(feedback):
    """
    Returns the sentiment score of the customer's review.
    -1 = very negative
    0 = neutral
    1 = very positive
    """
    sentiment = analyzer.polarity_scores(feedback)
    return sentiment["compound"]    


df["Sentiment Score"] = df["Feedback"].apply(get_sentiment_score)

# =========================================================
# Sentiment Groups
# 3 groups: Negative, Neutral, Positive
# Add new column "Sentiment Group" to the DataFrame
# =========================================================
def get_sentiment_group(score):
    """
    Positive: >= 0.05
    Negative: <= -0.05
    Neutral: between -0.05 and 0.05
    """

    if score >= 0.05:
        return "Positive"
    elif score <= -0.05:
        return "Negative"
    else:
        return "Neutral"


df["Sentiment Group"] = df["Sentiment Score"].apply(get_sentiment_group)

# =========================================================
# Print Updated Dataframe Results
# =========================================================

print("\nSentiment Results:")

print(
    df[[
            "Customer Name",
            "Feedback",
            "Sentiment Score",
            "Sentiment Group"]].head(10))


print("\nSentiment Counts:")
print(df["Sentiment Group"].value_counts())

# =========================================================
# Topic Analysis
# =========================================================
vectorizer = TfidfVectorizer(
    max_features=1000, 
    stop_words='english', 
    ngram_range=(1, 2), 
    min_df=2)

X = vectorizer.fit_transform(df["Feedback"])
print("\nTF-IDF matrix shape:", X.shape)

# =========================================================
# Test different number of topics (silhouette score) to 
# find the optimal number of topics
# =========================================================
silhouette_scores = {}

print("\nTesting number of topic clusters:")


# Test 2 through 6 topics
for k in range(2, 7):

    kmeans_test = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=20)

    labels = kmeans_test.fit_predict(X)
    score = silhouette_score(X, labels)
    silhouette_scores[k] = score

    print(f"k = {k}: " f"Silhouette Score = {score:.4f}")

best_k = max(silhouette_scores, key=silhouette_scores.get)
best_score = silhouette_scores[best_k]

print("\nBest number of topics:", best_k)
print("Best silhouette score:", best_score)

# Training final Model
kmeans = KMeans(
    n_clusters=best_k,
    random_state=42,
    n_init=20
)

df["Topic Cluster"] = kmeans.fit_predict(X)

# ========================================================
# Find the top keywords for each topic cluster
# ======================================================== 
terms = vectorizer.get_feature_names_out()

print("\nTOP WORDS FOR EACH TOPIC")
print("=" * 60)


topic_keywords = {}

for cluster in range(best_k):

    center = kmeans.cluster_centers_[cluster]

    # 10 strongest terms
    top_indices = (center.argsort()[-10:][::-1])
    top_words = [terms[i] for i in top_indices]
    topic_keywords[cluster] = top_words

    print(f"\nCluster {cluster}:")
    print(", ".join(top_words))

# =========================================================
# Sample Feedbacks for each topic cluster
# =========================================================
print("\n")
print("=" * 60)
print("SAMPLE FEEDBACK FROM EACH TOPIC")
print("=" * 60)

for cluster in range(best_k):
    print(f"\n--- Cluster {cluster} ---")
    examples = (df[df["Topic Cluster"] == cluster]["Feedback"].head(5))
    for example in examples:
        print("-", example)

# =========================================================
# Assigning Topic Names
# Based on the top keywords and the samples from each cluster,
# manually assign a broad topic name for each one.
# Note that this is a subjective process and may vary based on interpretation
# Some clusters may not have a clear, definite topic and may overlap with others 
# (i.e. Cluster 2).
# =========================================================
topic_names = {
    0: "Policy & Pricing",
    1: "Claims & Processes",
    2: "Digital Access & Coverage",
    3: "Customer Service",
    4: "Issue Resolution",
    5: "Overall Experience & Value"
}

df["Topic"] = df["Topic Cluster"].map(topic_names)


# =========================================================
#  Check the final DataFrame with all the new columns
# And export to Excel file for PowerBI
# =========================================================

print("\nFinal DataFrame with Sentiment and Topic Analysis:")
print(df.head())

output_file = r"C:\Users\saman\Downloads\Insurance_Feedback_Analyzed.xlsx"
df.to_excel(output_file,index=False)

print("Saved analyzed dataset as:", output_file)

import os
print("Saved to:")
print(os.path.abspath(output_file))





