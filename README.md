# 🎶 Amazon Music Clustering Project

> Automatically group songs into meaningful clusters (e.g., genres, moods, styles) based on audio features using unsupervised machine learning.

---

## 📌 **Table of Contents**
- [📖 Problem Statement](#-problem-statement)
- [🎯 Objectives](#-objectives)
- [🧠 Skills & Tools](#-skills--tools)
- [🧰 Dataset](#-dataset)
- [📊 Approach](#-approach)
- [📈 Results](#-results)
- [📂 Project Structure](#-project-structure)
- [🚀 How to Run](#-how-to-run)
- [✨ Future Work](#-future-work)
- [🤝 Acknowledgements](#-acknowledgements)

---

## 📖 **Problem Statement**

With millions of songs on platforms like Amazon Music, manually categorizing tracks into genres or moods is impractical.  
The goal of this project is to **automatically group similar songs** based on their **audio characteristics** using clustering techniques.  

By analyzing features such as danceability, energy, loudness, and more, we aim to:
- Discover hidden patterns
- Identify natural song groupings (e.g., party vs chill)
- Enable recommendation systems and playlist curation

---

## 🎯 **Objectives**
- Perform data cleaning & preprocessing on audio feature data
- Scale numerical features for clustering
- Use **K-Means clustering** to group similar songs
- Determine optimal number of clusters using **Elbow** and **Silhouette** methods
- Visualize clusters using **PCA**
- Analyze cluster profiles to interpret musical characteristics

---

## 🧠 **Skills & Tools**

| Category             | Tools / Skills |
|----------------------|---------------|
| Programming          | Python, Pandas, NumPy |
| Machine Learning     | K-Means Clustering, PCA, Unsupervised Learning |
| Visualization        | Matplotlib, Plotly |
| Evaluation           | Silhouette Score, Davies–Bouldin Index |
| Workflow             | Jupyter Notebook, VS Code, Git & GitHub |

---

## 🧰 **Dataset**

- **Source:** Amazon Music (provided dataset)  
- **File:** `single_genre_artists.csv`  
- **Rows:** ~95,000 songs  
- **Features:**  
  - Numerical audio features: `danceability`, `energy`, `loudness`, `speechiness`, `acousticness`, `instrumentalness`, `liveness`, `valence`, `tempo`, `duration_ms`  
  - Text columns: song name, artist name, genre, etc.

---

## 📊 **Approach**

1. **Data Exploration & Cleaning**
   - Removed duplicates, handled missing values
   - Selected relevant audio features
   - Scaled data using StandardScaler

2. **Model Selection**
   - Used Elbow and Silhouette methods to find best `k`
   - Chose optimal number of clusters based on Silhouette peak

3. **Clustering**
   - Applied K-Means with the selected `k`
   - Evaluated clusters using Silhouette Score and Davies–Bouldin Index

4. **Visualization & Interpretation**
   - Reduced data to 2D using PCA for visualization
   - Created scatter plots and cluster profile heatmaps
   - Interpreted clusters by dominant audio characteristics

5. **Export & Reporting**
   - Saved clustered dataset and cluster profiles
   - Generated README summary for reproducibility

---

## 📈 **Results**

| Metric                    | Value          |
|---------------------------|---------------|
| Optimal Number of Clusters| `k = X` *(replace with your best_k)* |
| Silhouette Score          | `0.XXX` |
| Davies–Bouldin Index      | `X.XXX` |

**Cluster Examples**:
- 🟠 **Cluster 0**: High energy + danceability → *Party / Pop songs*  
- 🔵 **Cluster 1**: High acousticness + low loudness → *Chill / Acoustic*  
- 🟢 **Cluster 2**: High speechiness → *Rap / Spoken word*  

📌 These clusters can be used for:
- Personalized playlist curation
- Improved song discovery & recommendations
- Artist/market analysis

---

## 📂 **Project Structure**

