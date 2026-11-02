import os
from datetime import datetime

LOG_FILE = "logs/csp_activity.log"


def write_log(message):
    os.makedirs("logs", exist_ok=True)

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(LOG_FILE, "a") as file:
        file.write(f"[{current_time}] {message}\n")

    print("[SUCCESS] Activity logged!")


def view_logs():
    if not os.path.exists(LOG_FILE):
        print("[INFO] No logs found yet.")
        return

    print("\n====== CSP ACTIVITY LOGS ======")

    with open(LOG_FILE, "r") as file:
        print(file.read())


def main():
    while True:
        print("\n==============================")
        print(" CSP SECURITY LOG SYSTEM")
        print("==============================")
        print("1. Add Activity Log")
        print("2. View Activity Logs")
        print("3. Exit")

        choice = input("Select option: ")

        if choice == "1":
            message = input("Enter activity: ")
            write_log(message)

        elif choice == "2":
            view_logs()

        elif choice == "3":
            break

        else:
            print("Invalid option!")


if __name__ == "__main__":
    main()

