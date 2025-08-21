# The Data Reliability Playbook

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Welcome! This repository contains the code examples and practical demos from my **Data+AI 2025** presentation, **"The Data Reliability Ceiling: A Technical Playbook for AI-Ready Observability."**

The goal of this playbook is to provide tangible, runnable code that brings the concepts from the talk to life. You can explore each concept in its own self-contained directory.

---

## 🚀 The Core Concepts

This playbook is built around a few key ideas:

* **The Data Reliability Ceiling**: The core thesis that your AI model's reliability is fundamentally capped by your data's reliability ($R_{model} \le R_{data}$).
* **Garbage In, Gaslight Out**: The modern evolution of GIGO, where subtly flawed data is synthesized by AI into confident, plausible, and dangerously misleading outputs.
* **The Four Pillars of Data Reliability**: A framework for building a robust data foundation based on **Specification**, **Behavior**, **Timeliness**, and **Provenance**.

---

## 🚀 Getting Started

This repository uses [Poetry](https://python-poetry.org/) to manage dependencies and virtual environments, ensuring a reproducible setup.

1.  **Install Poetry**: If you don't have it, follow the [official installation instructions](https://python-poetry.org/docs/#installation).

2.  **Clone the Repository**:
    ```bash
    git clone git@github.com:eugeneklyuchnikov/data-reliability-playbook.git
    cd data-reliability-playbook
    ```

3.  **Install Dependencies**: This command will create a virtual environment, detect the correct Python version, and install all the libraries defined in `pyproject.toml`.
    ```bash
    poetry install
    ```

4.  **Activate the Virtual Environment**: To run any scripts, you must first activate the environment managed by Poetry.
    ```bash
    source $(poetry env info -p)/bin/activate
    ```

Now you are ready to run the individual plays!

---

## 🛠️ The Plays: Code Examples

Below are the practical examples discussed in the presentation. Each directory contains its own `README.md` with specific instructions on how to run the code.

### ▶️ [1. Data Contracts as Code](./1-data-contracts-as-code/)

**Concept**: Pillar 1: Specification.
**Demo**: A simple Python script validates data files against a declarative `contract.yaml`, showing how to enforce explicit rules programmatically.

### ▶️ [2. Automated Profiling and Drift Detection](./2-automated-profiling-and-drift/)

**Concept**: Pillar 2: Behavior.
**Demo**: A Jupyter Notebook using `whylogs` to generate statistical profiles of datasets and automatically detect distributional drift between a "baseline" and a "drifted" dataset.

### ▶️ [3. Data Resilience Drills](./3-data-resilience-drills/)

**Concept**: Proactive reliability testing (Chaos Engineering for data).
**Demo**: A Python script (`run_drill.py`) uses mocking to inject failures (e.g., nulls, latency) into a simple data pipeline (`simple_pipeline.py`) to test its resilience without altering the source code.

### ▶️ [4. The Observability Sidecar Pattern](4-declarative-sidecar-pattern/)

**Concept**: A modern, decentralized architectural pattern for observability.
**Demo**: A `docker-compose` setup that simulates a `app_with_observability` and a separate `generic_sidecar_engine` container that profiles the data in a decoupled way.

### ▶️ [Bonus: The "Gaslight Out" Demo](./5-bonus-gaslight-out-demo/)

**Concept**: Illustrating the core problem.
**Demo**: A Jupyter Notebook that feeds an LLM two subtly incorrect facts and shows how it confidently synthesizes them into a plausible but completely false statement.

---

##  License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.