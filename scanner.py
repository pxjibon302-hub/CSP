
import os
import platform
import sys
from datetime import datetime

def security_scan():
    print("=" * 40)
    print("       CSP SECURITY SCANNER")
    print("=" * 40)

    print("\n[ BASIC SECURITY CHECK ]")

    print("Operating System:", platform.system())
    print("Python Version:", platform.python_version())
    print("Python Executable:", sys.executable)

    print("\n[ FILE CHECK ]")

    files = ["main.py", "network.py", "scanner.py"]

    for file in files:
        if os.path.isfile(file):
            print(file, "- Found")
        else:
            print(file, "- Missing")

    print("\n[ SECURITY STATUS ]")
    print("No external network attack test performed.")
    print("This is a basic local security check.")

    print("\nScan Time:", datetime.now())
    print("\n[ SCAN COMPLETE ]")

if __name__ == "__main__":
    security_scan()
0

