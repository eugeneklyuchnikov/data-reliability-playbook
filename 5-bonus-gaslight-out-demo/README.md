# Play 5: The "Gaslight Out" Demo

This directory contains a Jupyter Notebook to provide a live demonstration of the **"Garbage In, Gaslight Out"** concept.

The notebook, `gaslight_demo.ipynb`, feeds a Large Language Model (LLM) two subtly incorrect facts and prompts it to generate a summary. The result is a confident, plausible, and fundamentally wrong output that perfectly illustrates the modern risks of poor data quality in AI systems.

## 🚀 How to Run

### 1. Prerequisites

* Ensure you have followed the **"Getting Started"** instructions in the main [README.md](../README.md) and have activated the virtual environment. The `requests` library needed for this demo is already included in the root `pyproject.toml`.

### 2. Get and Set Your Gemini API Key

This demo requires a free Google Gemini API key.

1.  **Get a key**: Go to [Google AI Studio](https://aistudio.google.com/), click **"Get API key"**, and copy the key.
2.  **Set the key as an environment variable**: In your terminal, run the following command, replacing `your-api-key-here` with the key you just copied.

    ```bash
    export GEMINI_API_KEY='your-api-key-here'
    ```
    **Note**: This environment variable is only set for your current terminal session. You will need to set it again if you open a new terminal.

### 3. Launch Jupyter

From the **root directory** of the repository, launch the Jupyter environment:

```bash
poetry run jupyter notebook
```

### 4. Open and Run the Notebook

In your browser, navigate to the `5-bonus-gaslight-out-demo/` directory and open `gaslight_demo.ipynb`.

You can now run the cells in the notebook one by one to see the demonstration.
