
import socket
import platform
import subprocess

def network_analyzer():
    print("=" * 40)
    print("       CSP NETWORK ANALYZER")
    print("=" * 40)

    print("\n[ DEVICE INFORMATION ]")
    print("Device:", platform.node())
    print("System:", platform.system())

    print("\n[ NETWORK INFORMATION ]")

    try:
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
        print("Hostname:", hostname)
        print("Local IP:", ip)
    except Exception as error:
        print("IP Error:", error)

    print("\n[ INTERNET CONNECTION ]")

    try:
        connection = socket.create_connection(
            ("1.1.1.1", 443), timeout=5
        )
        connection.close()
        print("Internet: Connected")
    except OSError:
        print("Internet: Not Connected")

    print("\n[ NETWORK TEST COMPLETE ]")

if __name__ == "__main__":
    network_analyzer()
0

