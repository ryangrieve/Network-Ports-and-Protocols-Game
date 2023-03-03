import random

ports = {
    "ftp": "20/21",
    "ssh": "22",
    "sftp": "22",
    "telnet": "23",
    "smtp": "25",
    "dns": "53",
    "dhcp": "67/68",
    "tftp": "69",
    "http": "80",
    "pop3": "110",
    "ntp": "123",
    "netbios": "139",
    "imap": "143",
    "snmp": "161/162",
    "ldap": "389",
    "https": "443",
    "smb": "445",
    "syslog": "514",
    "smtptls": "587",
    "ldaps": "636",
    "imapssl": "993",
    "pop3ssl": "995",
    "sql": "1433",
    "sqlnet": "1521",
    "mysql": "3306",
    "rdp": "3389",
    "sip": "5060/5061",
}

print(
    """
Network Ports and Protocols Game
-----------------------------------------------------------------------
Instructions:
1) Type the port number for each port/protocol.
2) Use a slash if a port/protocol has more than two ports. (eg: FTP)
Examples: 20/21, 67/68, 161/162, 5060/5061
-----------------------------------------------------------------------"""
)


def get_port():
    used_ports = []
    while True:
        port_name = random.choice(list(ports.keys()))
        port = ports[port_name]
        if port not in used_ports:
            used_ports.append(port)
            break
    if type(port) == list:
        return random.choice(port), port_name
    else:
        return port, port_name


def begin_game():
    while True:
        try:
            num_questions = int(input("\n* How long should the quiz be? "))
        except Exception:
            print("\nInvalid quiz length. Please try again.")
            continue

        score = 0
        for i in range(num_questions):
            port, port_name = get_port()
            answer = input(f"\nWhat is the port number for {port_name}? ")
            if answer == (port):
                print("\n* Correct!")
                score += 1
            else:
                print(f"\n* Incorrect. The correct answer is {port}.")

        result = score / num_questions * 100
        print(f"\nResults:\n---------\n{score}/{num_questions} {result:.2f}%")
        if result >= 90:
            print("\nGreat work!")
        else:
            print("\nKeep practicing!")

        play_again = input("\nDo you want to play again? (y/n) ")
        if play_again.lower() == "y":
            continue
        else:
            quit("\nClosing game...\n")


begin_game()
