# Play 2: Detecting Subtle Sentiment Drift

This directory demonstrates how to use data profiling to automatically detect a subtle but critical **semantic drift** in your data, a core concept of **Pillar 2: Behavior**.

We use the `whylogs` library to compare two datasets:
1.  `dataset_baseline.csv`: Represents our "normal," healthy product reviews.
2.  `dataset_drifted_sentiment.csv`: Represents a new batch of data where the `rating` and `review_length` distributions are stable, but the underlying **`sentiment_score`** has degraded significantly.

The `drift_detection_demo.ipynb` notebook walks through the process of loading these datasets, profiling them, and generating a drift report that automatically flags the problematic `sentiment_score` column.

## 🚀 How to Run

### 1. Generate the Data

First, run the data generation script from the **root directory** of the repository. This will create the two 200-row CSV files needed for the demo.
```bash
python generate_data.py
```

### 2. Launch Jupyter

Next, launch the Jupyter environment by running the following command from the **root directory**:
```bash
poetry run jupyter notebook
```
This will open a new tab in your browser.

### 3. Open and Run the Notebook

In the browser tab, navigate to the `2-automated-profiling-and-drift/` directory and click on `drift_detection_demo.ipynb`.

You can now run the cells in the notebook one by one to see the drift detection in action.