import sys
from importlib import metadata as im
from typing import Dict


def check_dependencies() -> bool:
    """Verifies all required dependencies for the matrix data analysis.

    Returns:
        bool: True if all critical dependencies are installed, False otherwise.
    """
    print("\nChecking dependencies:")

    dependencies: Dict[str, str] = {
        "pandas": "Data manipulation ready",
        "numpy": "Numerical computations ready",
        "matplotlib": "Visualization ready",
    }

    all_installed: bool = True
    for package, purpose in dependencies.items():
        try:
            version: str = im.version(package)
            print(f"[OK] {package} ({version}) - {purpose}")
        except im.PackageNotFoundError:
            print(f"[ERROR] {package} is missing. Required for: {purpose}")
            all_installed = False

    return all_installed


def analyze_matrix_data() -> None:
    """Generates and organizes matrix data and saves visualization.

    Raises:
        Exception: If data generation or plotting fails.
    """
    try:
        import numpy as np
        import pandas as pd
        from matplotlib import pyplot as plt

        print("\nAnalyzing Matrix data...")
        print("Processing 1000 data points...")

        time_points: np.NDArray[np.float64] = np.linspace(0, 2 * np.pi, 1000)
        signal_strengths: np.NDArray[np.float64] = np.sin(time_points)

        matrix_df: pd.DataFrame = pd.DataFrame({
            "Time": time_points,
            "Signal": signal_strengths
        })

        print("Generating visualization...")
        plt.figure(figsize=(10, 6))
        plt.plot(matrix_df["Time"], matrix_df["Signal"], color="green")
        plt.title("Matrix Data Analysis")
        plt.xlabel("Time")
        plt.ylabel("Signal")

        savefile: str = "matrix_analysis.png"

        for i in range(1, 6):
            try:
                plt.savefig(savefile)
                break
            except (PermissionError, IsADirectoryError):
                print(f"Error saving visualization in file {savefile}")
                savefile = f"matrix_analysis({i}).png"
                print(
                    f"Recovery program visualization saving in file {savefile}"
                )
                i += 1
        else:
            print("Saving visualization failed")

        print("\nAnalysis complete!")
        print(f"Results saved to: {savefile}")

    except Exception as error:
        print(f"Error during analysis: {error}")


def main() -> None:
    """Main execution function for the loading program."""
    print("\nLOADING STATUS: Loading programs...")
    if not check_dependencies():
        print("\nError: Missing required packages.")
        sys.exit(1)

    analyze_matrix_data()


if __name__ == "__main__":
    main()
