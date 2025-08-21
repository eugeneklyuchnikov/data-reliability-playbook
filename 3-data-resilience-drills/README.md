# Play 3: Data Resilience Drills (Chaos Engineering for Data)

This directory demonstrates "Data Drills"—a proactive approach to testing the resilience of your data pipelines, inspired by Chaos Engineering.

We have a standard pipeline defined in `simple_pipeline.py`. The `run_drill.py` script acts as a "chaos engine," intentionally injecting failures into the pipeline at runtime to see how it behaves under stress. This allows us to find weaknesses before they cause real production incidents.

## 🚀 How to Run

Ensure you have followed the **"Getting Started"** instructions in the main [README.md](../README.md) and have activated the virtual environment. The data from Play 2 is used as the source.

### 1. Run the Normal Pipeline

First, run the pipeline normally to see its expected behavior and generate a baseline `output.csv`.

```bash
python simple_pipeline.py
```
This should run successfully in a few seconds.

### 2. Run Data Drill 1: Null Injection

This drill tests how the `transform_data` function handles unexpected `null` values in its input. The drill script will temporarily replace the output of `extract_data` with a corrupted DataFrame.

```bash
python run_drill.py nulls
```
Observe the logs. You should see a `WARNING` message from the pipeline where it detects and handles the nulls, proving its resilience.

### 3. Run Data Drill 2: Latency Injection

This drill tests how the system behaves when an upstream process is slow. The drill script patches the `time.sleep` call inside the pipeline to simulate a much longer processing delay.

```bash
python run_drill.py latency
```
Observe the logs. You'll see the pipeline takes significantly longer to run, confirming that we can successfully simulate and measure latency.