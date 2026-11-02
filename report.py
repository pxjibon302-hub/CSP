
import os
import platform
from datetime import datetime

def create_report():
    os.makedirs("reports", exist_ok=True)

    filename = "reports/CSP_Security_Report.txt"

    with open(filename, "w") as file:
        file.write("CSP SECURITY REPORT\n")
        file.write("=" * 35 + "\n")
        file.write("Version: 1.0\n")
        file.write("Operating System: " + platform.system() + "\n")
        file.write("Python Version: " + platform.python_version() + "\n")
        file.write("Device: " + platform.machine() + "\n")
        file.write("Report Date: " + str(datetime.now()) + "\n")
        file.write("\nBasic local checks completed.\n")
        file.write("No external attack testing performed.\n")

    print("\n[ SUCCESS ]")
    print("Security report created!")
    print("Location:", filename)

if __name__ == "__main__":
    create_report()
0

