import pandas as pd
import numpy as np

# --- Configuration ---
NUM_ROWS = 200
BASELINE_PATH = "data/dataset_baseline.csv"
DRIFTED_PATH = "data/dataset_drifted_sentiment.csv"
PRODUCT_IDS = ['prod_a', 'prod_b', 'prod_c', 'prod_d']


def generate_baseline_data(num_rows):
    """Generates a dataframe of healthy, high-quality review data."""
    print(f"Generating {num_rows} rows of baseline data...")

    # Ratings are skewed high (4s and 5s are common)
    ratings = np.random.choice([1, 2, 3, 4, 5], num_rows, p=[0.05, 0.1, 0.2, 0.35, 0.3])

    # Review length is centered around 160 characters
    review_lengths = np.random.normal(loc=160, scale=40, size=num_rows).astype(int).clip(20)

    # Sentiment is strongly correlated with rating, with some positive noise
    sentiment_scores = (ratings / 5.0) - 0.1 + np.random.uniform(0, 0.15, num_rows)
    sentiment_scores = sentiment_scores.clip(-1.0, 1.0)

    data = {
        'review_id': [f'rev{i:04d}' for i in range(num_rows)],
        'product_id': np.random.choice(PRODUCT_IDS, num_rows),
        'rating': ratings,
        'review_length': review_lengths,
        'sentiment_score': np.round(sentiment_scores, 4)
    }
    return pd.DataFrame(data)


def generate_drifted_data(num_rows):
    """
    Generates a dataframe where sentiment has drifted to be neutral/negative,
    but other stats remain the same.
    """
    print(f"Generating {num_rows} rows of sentiment-drifted data...")

    # CRITICAL: Keep rating and length distributions the same as the baseline
    ratings = np.random.choice([1, 2, 3, 4, 5], num_rows, p=[0.05, 0.1, 0.2, 0.35, 0.3])
    review_lengths = np.random.normal(loc=160, scale=40, size=num_rows).astype(int).clip(20)

    # DRIFT: Sentiment is now decoupled from rating and centered around neutral/negative
    # This simulates low-quality, spammy, or angry reviews.
    sentiment_scores = np.random.normal(loc=0.1, scale=0.4, size=num_rows)
    sentiment_scores = sentiment_scores.clip(-1.0, 1.0)

    data = {
        'review_id': [f'rev{i + num_rows:04d}' for i in range(num_rows)],
        'product_id': np.random.choice(PRODUCT_IDS, num_rows),
        'rating': ratings,
        'review_length': review_lengths,
        'sentiment_score': np.round(sentiment_scores, 4)
    }
    return pd.DataFrame(data)


if __name__ == "__main__":
    baseline_df = generate_baseline_data(NUM_ROWS)
    baseline_df.to_csv(BASELINE_PATH, index=False)
    print(f"✅ Baseline data saved to {BASELINE_PATH}")

    drifted_df = generate_drifted_data(NUM_ROWS)
    drifted_df.to_csv(DRIFTED_PATH, index=False)
    print(f"✅ Drifted data saved to {DRIFTED_PATH}")