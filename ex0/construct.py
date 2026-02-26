import os
import sys
import site


class ConstructEnvironment:
    """Class to analyze and display the current Python environment status."""

    def __init__(self) -> None:
        """Initializes the environment checker."""
        self.is_venv: bool = sys.prefix != sys.base_prefix
        self.python_executable: str = sys.executable
        self.prefix_path: str = sys.prefix

    def display_status(self) -> None:
        """Displays the appropriate environment status."""
        if self.is_venv:
            self._print_construct()
        else:
            self._print_plugged_in()

    def _print_plugged_in(self) -> None:
        """Prints the status when running in the global environment."""
        print("\nMATRIX STATUS: You're still plugged in")
        print(f"\nCurrent Python: {self.python_executable}")
        print("Virtual Environment: None detected")
        print("\nWARNING: You're in the global environment!")
        print("The machines can see everything you install.")
        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env")
        print("Scripts")
        print("activate # On Windows")
        print("\nThen run this program again.")

    def _print_construct(self) -> None:
        """Prints the status when running inside a virtual environment."""
        print("\nMATRIX STATUS: Welcome to the construct")
        print(f"\nCurrent Python: {self.python_executable}")

        venv_name: str = os.path.basename(self.prefix_path)
        print(f"Virtual Environment: {venv_name}")
        print(f"Environment Path: {self.prefix_path}")

        print("\nSUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.")
        print("\nPackage installation path:")

        site_packages: list[str] = site.getsitepackages()
        if site_packages:
            print(site_packages[0])


def main() -> None:
    """Main execution function."""
    try:
        env_checker: ConstructEnvironment = ConstructEnvironment()
        env_checker.display_status()
    except Exception as e:
        print(f"Error: {e}")


if __name__ == '__main__':
    main()
