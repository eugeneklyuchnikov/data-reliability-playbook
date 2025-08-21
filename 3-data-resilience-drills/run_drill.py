import argparse
import logging
import pandas as pd
import time
from unittest.mock import patch

# Import the pipeline functions we want to test
from simple_pipeline import extract_data, transform_data, load_data

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - [DRILL] %(message)s')


def run_null_injection_drill():
    """
    DRILL 1: Test resilience against unexpected nulls.
    We patch the 'extract_data' function to return a DataFrame with nulls
    in the 'rating' column and see how 'transform_data' handles it.
    """
    logging.info("--- Starting Drill 1: Null Injection ---")
    source_file = "data/dataset_baseline.csv"
    destination_file = "data/output_null_drill.csv"

    # Original data is clean
    original_df = extract_data(source_file)

    # Create a corrupted version for our mock to return
    corrupted_df = original_df.copy()
    corrupted_df.loc[0:4, 'rating'] = None  # Inject nulls into the first 5 rows
    logging.warning("Created corrupted DataFrame with nulls in 'rating'.")

    # The 'patch' temporarily replaces the real function with our mock
    with patch('simple_pipeline.extract_data', return_value=corrupted_df) as mock_extract:
        logging.info("Patched 'extract_data'. Running pipeline...")
        try:
            # The pipeline thinks it's calling the real extract_data, but gets our corrupted data
            raw_data = mock_extract(source_file)
            transformed_data = transform_data(raw_data)
            load_data(transformed_data, destination_file)
            logging.info("--- Drill 1 Finished ---")
        except Exception as e:
            logging.error(f"--- Drill 1 Failed as expected or unexpectedly: {e} ---")


def run_latency_drill():
    """
    DRILL 2: Test system behavior with upstream latency.
    We patch 'time.sleep' inside the 'transform_data' function to simulate
    a much longer processing time.
    """
    logging.info("--- Starting Drill 2: Latency Injection ---")
    source_file = "data/dataset_baseline.csv"
    destination_file = "data/output_latency_drill.csv"

    # Save a reference to the original time.sleep function BEFORE the patch
    original_sleep = time.sleep

    # Patch 'time.sleep' to a longer duration (e.g., 8 seconds)
    with patch('simple_pipeline.time.sleep') as mock_sleep:
        # The side_effect now calls our saved, original function, breaking the loop.
        mock_sleep.side_effect = lambda seconds: original_sleep(8)

        logging.info("Patched 'time.sleep' to 8 seconds. Running pipeline...")

        try:
            start_time = time.time()
            raw_data = extract_data(source_file)
            transformed_data = transform_data(raw_data)
            load_data(transformed_data, destination_file)
            end_time = time.time()

            duration = end_time - start_time
            logging.info(f"Pipeline took {duration:.2f} seconds to run.")
            if duration > 7:
                logging.warning("Observed increased latency.")
            logging.info("--- Drill 2 Finished ---")
        except Exception as e:
            logging.error(f"--- Drill 2 Failed: {e} ---")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run Data Resilience Drills.")
    parser.add_argument("drill_name", choices=['nulls', 'latency'], help="The name of the drill to run.")
    args = parser.parse_args()

    if args.drill_name == 'nulls':
        run_null_injection_drill()
    elif args.drill_name == 'latency':
        run_latency_drill()