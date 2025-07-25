import socket

def scan_ports(host, start_port, end_port):
    print(f"\n🔍 Scanning ports {start_port}-{end_port} on {host}...\n")
    for port in range(start_port, end_port + 1):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(0.5)
                result = sock.connect_ex((host, port))
                status = "OPEN" if result == 0 else "CLOSED"
                print(f"Port {port:5}: {status}")
        except socket.error as e:
            print(f"⚠️ Error on port {port}: {e}")

while True:
    print("\n" + "="*50)
    print("🖥️  Python Port Scanner Menu")
    print("="*50)
    print("1. Scan ports")
    print("2. Exit")
    
    choice = input("Select an option [1/2]: ").strip()
    
    if choice == '2':
        print("🚪 Exiting... Stay curious, Connor!")
        break
    elif choice != '1':
        print("⚠️ Invalid choice. Please enter 1 or 2.")
        continue

    target_host = input("\n🔹 Enter target IP or domain: ").strip()
    
    try:
        start = int(input("🔹 Enter starting port (e.g. 1): "))
        end = int(input("🔹 Enter ending port (e.g. 1024): "))
        if start > end or start < 1 or end > 65535:
            raise ValueError
    except ValueError:
        print("⚠️ Invalid port range. Use values between 1 and 65535.")
        continue

    scan_ports(target_host, start, end)
    input("\n🔁 Scan complete. Press Enter to return to menu...")
