import os
import platform
import subprocess
from datetime import datetime


def system_info():
    print("\n--- SYSTEM INFORMATION ---")
    print("System:", platform.system())
    print("Python:", platform.python_version())
    print("Device:", platform.machine())
    print("Date:", datetime.now())


def password_security():
    print("\n--- PASSWORD SECURITY TEST ---")
    password = input("Enter a TEST password: ")

    score = 0
    score += len(password) >= 8
    score += any(c.isupper() for c in password)
    score += any(c.islower() for c in password)
    score += any(c.isdigit() for c in password)
    score += any(not c.isalnum() for c in password)

    print("Security Score:", score, "/ 5")

    if score >= 4:
        print("Result: Strong")
    elif score >= 3:
        print("Result: Medium")
    else:
        print("Result: Weak")


def run_module(filename):
    if os.path.exists(filename):
        subprocess.run(["python", filename])
    else:
        print("Module not found:", filename)


def show_menu():
    while True:
        print("\n==============================")
        print("       CSP SECURITY v1.2")
        print("==============================")
        print("1. System Information")
        print("2. Password Security Test")
        print("3. Network Analyzer")
        print("4. Security Scanner")
        print("5. Generate Security Report")
        print("6. Exit")
        print("7. File Integrity Checker")
        print("8. Security Log System")

        choice = input("\nSelect option: ")

        if choice == "1":
            system_info()
        elif choice == "2":
            password_security()
        elif choice == "3":
            run_module("network.py")
        elif choice == "4":
            run_module("scanner.py")
        elif choice == "5":
            run_module("report.py")
        elif choice == "7":
            run_module("integrity.py")
        elif choice == "8":
            run_module("logger.py")
        elif choice == "6":
            print("CSP closed. Goodbye!")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    show_menu()

