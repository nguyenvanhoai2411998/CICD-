import subprocess
import shutil
import pytest

def pytest_sessionfinish(session, exitstatus):
    # Optional: Only run if an allure report directory or results exist
    allure_results_dir = "allure-results"
    allure_report_dir = "allure-report"

    print("\n--- Generating Allure Report ---")
    try:
        # Step A: Generate standard allure report from raw results
        subprocess.run(
            ["allure", "generate", "--clean", allure_results_dir, "-o", allure_report_dir],
            check=True,
            shell=True  # shell=True ensures Windows finds CLI executables like 'allure.cmd'
        )

        # Step B: Combine report into a single HTML file
        print("--- Bundling into Single HTML File ---")
        subprocess.run(
            ["allure-combine", allure_report_dir],
            check=True,
            shell=True
        )
        print(f"Done! Standalone report created at: {allure_report_dir}/combined_index.html")

    except subprocess.CalledProcessError as e:
        print(f"Failed to generate combined Allure report: {e}")
    except FileNotFoundError:
        print("Error: 'allure' or 'allure-combine' CLI is not found in system PATH.")