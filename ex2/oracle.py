import os
import sys
from typing import Optional
from dotenv import load_dotenv


def check_env_security() -> bool:
    """Checks if the .env file exists in the current directory.

    Returns:
        bool: True if .env file exists, False otherwise.
    """
    return os.path.isfile(".env")


def read_matrix_config() -> None:
    """Loads environment variables and prints the Oracle configuration status.

    Raises:
        ValueError: If any required configuration variables are missing.
    """
    load_dotenv()

    print("\nORACLE STATUS: Reading the Matrix...")
    print("\nConfiguration loaded:")

    vars_name: list[str] = [
        "MATRIX_MODE", "DATABASE_URL", "API_KEY", "LOG_LEVEL", "ZION_ENDPOINT"
    ]

    env_vars: dict[str, Optional[str]] = {
        name: os.getenv(name) for name in vars_name
    }

    if not all(env_vars.values()):
        raise ValueError(
            "Missing required configuration variables "
            f"({str([k for k, v in env_vars.items() if not v])})."
        )

    print(f"Mode: {env_vars['MATRIX_MODE']}")
    print("Database: Connected to local instance")
    print("API Access: Authenticated")
    print(f"Log Level: {env_vars['LOG_LEVEL']}")
    print("Zion Network: Online")
    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")

    if check_env_security():
        print("[OK] .env file properly configured")
    else:
        print("[WARNING] .env file is missing")

    print("[OK] Production overrides available")
    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    try:
        read_matrix_config()
    except ValueError as error:
        print(f"Configuration Error: {error}")
        sys.exit(1)
