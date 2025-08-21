import pandas as pd
import time
import logging

# Configure basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def extract_data(source_path: str) -> pd.DataFrame:
    """Reads data from a source CSV file."""
    logging.info(f"Extracting data from {source_path}...")
    try:
        df = pd.read_csv(source_path)
        logging.info("Extraction complete.")
        return df
    except FileNotFoundError:
        logging.error(f"Source file not found at {source_path}")
        raise


def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """Applies a simple transformation to the data."""
    logging.info("Starting data transformation...")

    # Simple check for required columns
    required_cols = ['rating', 'review_length']
    if not all(col in df.columns for col in required_cols):
        logging.error(f"Missing one of the required columns: {required_cols}")
        raise ValueError("Input DataFrame is missing required columns.")

    # Handle potential nulls before calculation
    if df['rating'].isnull().any():
        logging.warning("Null values found in 'rating' column. Filling with 0.")
        df['rating'] = df['rating'].fillna(0)

    # Calculate a 'priority_score'
    # This calculation is intentionally sensitive to nulls or low values.
    df['priority_score'] = (df['rating'] / 5.0) * df['review_length']

    # Simulate a time-consuming operation
    logging.info("Simulating a 2-second processing delay...")
    time.sleep(2)

    logging.info("Transformation complete.")
    return df


def load_data(df: pd.DataFrame, destination_path: str) -> None:
    """Saves the transformed data to a destination CSV file."""
    logging.info(f"Loading data to {destination_path}...")
    df.to_csv(destination_path, index=False)
    logging.info(f"Load complete. Data saved to {destination_path}")


def main():
    """Main function to run the full ETL pipeline."""
    logging.info("--- Starting Simple ETL Pipeline ---")
    source_file = "data/dataset_baseline.csv"
    destination_file = "data/output.csv"

    try:
        raw_data = extract_data(source_file)
        transformed_data = transform_data(raw_data)
        load_data(transformed_data, destination_file)
        logging.info("--- Simple ETL Pipeline Finished Successfully ---")
    except Exception as e:
        logging.error(f"--- Simple ETL Pipeline Failed: {e} ---")


if __name__ == "__main__":
    main()