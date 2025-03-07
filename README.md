# ArcherSploit Framework

The ArcherSploit framework was developed as a Proof of Concept to research and exploit vulnerabilities in the TP-Link Archer C50v1 router. The script guides the user through the necessary steps to execute various attacks on this specific router. This exploit framework is modular and consists of four main components:

ArcherSploit.py - The main menu and control unit of the framework.

BruteForcer.py - Module for brute-forcing passwords.

DosWrapper.py - Module for executing DoS attacks.

PasswordStealer.py - Module for intercepting HTTP traffic to retrieve login credentials.

## ArcherSploit.py - The Main Menu

The ArcherSploit.py script serves as the control center of the framework and should be executed first. It provides a menu-driven interface that allows the user to navigate between different attack methods easily. Upon startup, the user is prompted to enter the target IP address. Once provided, the user is directed to the main menu, where the available attack techniques are clearly presented.

Main Menu Options:

  1. Bruteforce Passwords - Calls the BruteForcer module.

  2. HTTP Password Stealing - Launches the PasswordStealer module.

  3. DoS Attack - Starts the DosWrapper module to overload the router.

  4. Change Target IP - Modify the target IP address.

  5. Exit - Close the framework.

## BruteForcer.py - Password Brute-Forcing

The BruteForcer module is designed to perform brute-force attacks on the TP-Link Archer C50v1 router by exploiting a weakness in its authentication mechanism. Instead of interacting with the standard login page, this module uses the Archer Web Interface API to bypass the login screen and gain direct access to the main page.

### Menu Options:

  1. Start Bruteforce Attack - Select a password file and start the attack.

  2. Change Username (default: admin) - Modify the username (default: admin).

  3. Go Back to Main Menu - Return to the main menu.

### How It Works:

The module sends GET requests to the main page of the web interface using an Authorization cookie. This cookie contains the username and password encoded in Base64. The router has a security flaw where login restrictions apply only to the login page and not to direct requests to the main page.

For each password attempt, the module generates a Base64-encoded combination of username:password. Example for admin:password123:

Authorization=Basic YWRtaW46cGFzc3dvcmQxMjM=

The router directly verifies this cookie without tracking login attempts. If correct, the user is logged in instantly without seeing the login page or triggering any block mechanisms. This process repeats for every password in the provided wordlist until a valid login is found or all options are exhausted.

## DosWrapper.py - DoS Attacks

The DosWrapper.py module executes Denial of Service (DoS) attacks on the TP-Link Archer C50v1 router using the hping3 command. It functions as a wrapper, meaning it does not generate packets itself but rather calls hping3 to flood the router with SYN packets, overloading its open ports and making it unresponsive.

### Menu Options:

  1. Start DoS Attack – Launches the attack on open ports using the current settings.

  2. Change Port Range – Modify the port range to scan and attack.

  3. Change Number of Threads – Define the number of concurrent attack threads.

  4. Go Back to Main Menu – Returns to the main menu.

### How It Works:

The module first scans the specified port range to identify open ports. It then launches a SYN flood attack on each open port using multi-threading, allowing simultaneous attacks on multiple ports. The number of concurrent attacks is controlled by the Number of Threads option. This method ensures that the router remains inaccessible for as long as the script is running.

To stop the attack, press CTRL+C. It may take some time for the attack to fully terminate, as all threads need to close properly.

## PasswordStealer.py - HTTP Credentials Sniffer

The PasswordStealer.py module in ArcherSploit monitors HTTP traffic to the TP-Link Archer C50v1 web interface to intercept login credentials. Since the router uses Basic HTTP authentication, all login data is sent unencrypted, making it possible to extract usernames and passwords from network traffic.

### Menu Options:

  1. Start Sniffing for HTTP Credentials – Starts monitoring HTTP traffic on the selected network interface and port.

  2. Go Back to Main Menu – Returns to the main menu.

### How It Works:

The module listens for Authorization headers in HTTP requests. When detected, the Base64-encoded login credentials are extracted and decoded into plaintext. These credentials are then displayed in real-time.

This method is effective because the Archer C50v1 router does not use encryption (no HTTPS) for its authentication process, making it highly vulnerable to credential theft.

# ⚠ Disclaimer

This project is developed for educational and research purposes only. Unauthorized access or exploitation of network devices without explicit permission is illegal and punishable by law. The authors are not responsible for any misuse of this tool.

# 🔧 Installation & Usage

To use ArcherSploit, clone this repository and run ArcherSploit.py:

# Clone the repository
git clone https://github.com/Kedvama/archersploit.git
cd archersploit

# Run the main script
python3 ArcherSploit.py

Make sure you have the required dependencies installed:

pip install -r requirements.txt

📌 Requirements

Python 3.x

hping3 (for DoS attacks)

scapy (for packet sniffing)

To install missing dependencies:

sudo apt install hping3
pip install scapy

This README provides a comprehensive overview of ArcherSploit and its modules. Use it responsibly and only in controlled environments. 🚀

