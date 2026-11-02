import hashlib
import os

HASH_FILE = "logs/file_hashes.txt"


def calculate_hash(filepath):
    sha256 = hashlib.sha256()

    with open(filepath, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            sha256.update(chunk)

    return sha256.hexdigest()


def save_hash():
    filepath = input("Enter file path: ").strip()

    if not os.path.isfile(filepath):
        print("[ ERROR ] File not found!")
        return

    file_hash = calculate_hash(filepath)

    os.makedirs("logs", exist_ok=True)

    with open(HASH_FILE, "a") as file:
        file.write(filepath + "|" + file_hash + "\n")

    print("\n[ SUCCESS ] Hash saved!")
    print("SHA-256:", file_hash)


def verify_hash():
    filepath = input("Enter file path: ").strip()

    if not os.path.isfile(filepath):
        print("[ ERROR ] File not found!")
        return

    if not os.path.isfile(HASH_FILE):
        print("[ ERROR ] No saved hashes found!")
        return

    current_hash = calculate_hash(filepath)

    with open(HASH_FILE, "r") as file:
        records = file.readlines()

    for record in reversed(records):
        parts = record.strip().split("|", 1)

        if len(parts) == 2 and parts[0] == filepath:
            if parts[1] == current_hash:
                print("[ SAFE ] File has not changed.")
            else:
                print("[ WARNING ] File has changed!")
            return

    print("[ ERROR ] No previous hash found for this file.")


def main():
    while True:
        print("\n==============================")
        print(" CSP FILE INTEGRITY CHECKER")
        print("==============================")
        print("1. Save File Hash")
        print("2. Verify File")
        print("3. Exit")

        choice = input("Select option: ")

        if choice == "1":
            save_hash()
        elif choice == "2":
            verify_hash()
        elif choice == "3":
            break
        else:
            print("Invalid option!")


if __name__ == "__main__":
    main()

