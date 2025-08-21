import json
import yaml
import argparse
from jsonschema import validate, ValidationError, FormatChecker


def validate_data(contract_path: str, data_path: str) -> None:
    """
    Validates a JSON data file against a YAML data contract.

    Args:
        contract_path: Path to the YAML contract file.
        data_path: Path to the JSON data file to be validated.
    """
    print(f"─" * 50)
    print(f"▶️  Loading contract from: {contract_path}")
    print(f"▶️  Loading data from:    {data_path}")

    try:
        # Load the contract (schema) from the YAML file
        with open(contract_path, 'r') as f:
            contract = yaml.safe_load(f)

        # Load the data from the JSON file
        with open(data_path, 'r') as f:
            data = json.load(f)

        print("\n▶️  Performing validation...")

        # The core validation step!
        validate(
            instance=data,
            schema=contract,
            format_checker=FormatChecker()
        )

    except FileNotFoundError as e:
        print(f"\n❌ ERROR: File not found - {e.filename}")
    except ValidationError as e:
        # If validation fails, jsonschema raises a ValidationError.
        print(f"\n❌ VALIDATION FAILED!")
        print(f"─" * 20)
        print(f"Error: {e.message}")
        print(f"Path to error in data: {list(e.path)}")
        print(f"Validator that failed: '{e.validator}' = {e.validator_value}")
        print(f"─" * 20)
    except Exception as e:
        print(f"\n❌ An unexpected error occurred: {e}")
    else:
        # If no exception was raised, the data is valid.
        print(f"\n✅ VALIDATION SUCCESSFUL! The data conforms to the contract.")

    print(f"─" * 50)


if __name__ == "__main__":
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description="Validate data against a contract.")
    parser.add_argument("data_file", help="Path to the JSON data file.")
    parser.add_argument(
        "--contract",
        default="contract.yaml",
        help="Path to the YAML contract file (default: contract.yaml)"
    )
    args = parser.parse_args()

    # Run the validation function
    validate_data(contract_path=args.contract, data_path=args.data_file)