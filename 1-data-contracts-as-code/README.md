# Play 1: Data Contracts as Code

This directory contains a practical example of a **Data Contract**.

The contract is defined in `contract.yaml` using the JSON Schema standard. It specifies the required structure, data types, and semantic rules for a `user_signup` event. The Python script `validator.py` then uses this contract to programmatically validate data files.

## 🚀 How to Run

### 1. Setup

Ensure you have followed the **"Getting Started"** instructions in the main [README.md](../README.md) and have activated the virtual environment by running `source $(poetry env info -p)/bin/activate` from the root directory.

### 2. Run Validation

From the **root directory** of the repository, run the validator script:

**To validate the good data:**
```bash
python validator.py data/good_data.json
```

You should see a **`✅ VALIDATION SUCCESSFUL!`** message.

**To validate the bad data:**

```bash
python validator.py data/bad_data_user_id.json
python validator.py data/bad_data_email_missing.json
python validator.py data/bad_data_low_age.json
python validator.py data/bad_data_timestamp_format.json
python validator.py data/bad_data_unexpected_property.json
```

You will see a **`❌ VALIDATION FAILED!`** message. The script will print the *first* error it finds, explaining exactly which rule was violated. For example, it might tell you that the `email` field is missing. If you fix that and re-run, it will find the next error, and so on.