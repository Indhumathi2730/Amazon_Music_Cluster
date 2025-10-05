# app.py

import streamlit as st
import pandas as pd
import plotly.express as px

# ------------------------------
# Page Config
# ------------------------------
st.set_page_config(
    page_title="Amazon Music Clustering 🎶",
    layout="wide"
)

st.title("🎶 Amazon Music Clustering Dashboard")
st.markdown("Explore song clusters generated using unsupervised machine learning (K-Means).")

# ------------------------------
# Load Data
# ------------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("output/amazon_music_clusters.csv")
    profile = pd.read_csv("output/cluster_profile.csv", index_col=0)
    return df, profile

df, cluster_profile = load_data()

# Sidebar Filters
st.sidebar.header("🔍 Filters")
cluster_options = sorted(df['cluster'].unique())
selected_clusters = st.sidebar.multiselect(
    "Select clusters",
    options=cluster_options,
    default=cluster_options
)

# Filter DataFrame
filtered_df = df[df['cluster'].isin(selected_clusters)]

# ------------------------------
# PCA Scatter Plot
# ------------------------------
st.subheader("📈 PCA Scatter Plot")
fig = px.scatter(
    filtered_df,
    x="pca_1",
    y="pca_2",
    color="cluster",
    hover_data=["name_song", "name_artists"] if "name_song" in df.columns else ["cluster"],
    title="Clusters visualized in 2D space (PCA)"
)
fig.update_traces(marker=dict(size=5))
st.plotly_chart(fig, use_container_width=True)

# ------------------------------
# Cluster Profile Heatmap
# ------------------------------
st.subheader("🔥 Cluster Profile (Feature Averages)")
st.dataframe(cluster_profile.style.format("{:.2f}"))

# Optional Plotly heatmap
profile_fig = px.imshow(
    cluster_profile,
    text_auto=True,
    aspect="auto",
    title="Cluster Feature Heatmap",
    color_continuous_scale="Blues"
)
st.plotly_chart(profile_fig, use_container_width=True)

# ------------------------------
# Song Explorer
# ------------------------------
st.subheader("🎧 Song Explorer")
st.write("Browse songs within the selected clusters.")

cols = ["name_song", "name_artists", "cluster"]
cols = [c for c in cols if c in df.columns]
st.dataframe(filtered_df[cols].head(1000))

# Run - streamlit run app.py 
