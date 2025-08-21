# Play 4: The Declarative Observability Sidecar

This directory demonstrates a realistic, two-service architecture for implementing a declarative observability sidecar.

### The Structure

This example is organized into two distinct services to clearly show the separation of concerns:

1.  **`generic_sidecar_engine/`**: This represents a **reusable service** built by a central platform team. Its Python code is a generic engine that knows how to process metrics based on an external configuration file.

2.  **`app_with_observability/`**: This represents a **specific application**. It contains the data producer (`producer.py`) and, crucially, the `config.yaml` which **declares** what metrics to track for this specific app.

The `docker-compose.yaml` file orchestrates this by building a container from the generic engine and then injecting the application-specific config into it at runtime. This perfectly illustrates how a generic tool can be customized for a specific use case without changing its code.

## 🚀 How to Run

### 1. Prerequisites
You must have **Docker** and **Docker Compose** installed.

### 2. Launch the Application
From **this directory** (`4-declarative-sidecar-pattern/`), run the following command:

```bash
docker-compose up --build
```

### 3. Observe the Output

You will see logs from the `application` service producing data, and a separate metrics report every 10 seconds from the `observability_sidecar`, which is being driven by the rules in `app_with_observability/config.yaml`.

### 4. Shut Down

Press `Ctrl + C`, then run `docker-compose down` to clean up.