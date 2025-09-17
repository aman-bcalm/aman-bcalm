#!/usr/bin/env python3
"""
Matrix Terminal Animation Script
Creates a Matrix-style terminal animation for GitHub profile
"""

import random
import time
import sys

def matrix_rain():
    """Simulate Matrix code rain effect"""
    chars = "01"
    width = 80
    height = 20
    
    print("\033[32m")  # Green color
    print("=" * width)
    print("MATRIX TERMINAL ACTIVATED")
    print("=" * width)
    
    for _ in range(height):
        line = ""
        for _ in range(width):
            line += random.choice(chars)
        print(line)
        time.sleep(0.1)
    
    print("\033[0m")  # Reset color

def matrix_quote():
    """Display Matrix quotes"""
    quotes = [
        "Welcome to the real world.",
        "There is no spoon.",
        "The Matrix has you.",
        "Follow the white rabbit.",
        "What is the Matrix?",
        "You take the red pill...",
        "The Matrix is everywhere.",
        "Free your mind.",
        "There is no fate but what we make.",
        "I know kung fu."
    ]
    
    print("\033[32m" + random.choice(quotes) + "\033[0m")

def hacker_mode():
    """Simulate hacker terminal"""
    commands = [
        "sudo rm -rf /",
        "cat /dev/urandom",
        "while true; do echo 'HACKING...'; done",
        "nmap -sS target.com",
        "hydra -l admin -P passwords.txt target.com",
        "sqlmap -u target.com --dbs",
        "metasploit console",
        "aircrack-ng capture.cap",
        "john --wordlist=rockyou.txt hash.txt",
        "wireshark -i eth0"
    ]
    
    print("\033[31m[HACKER MODE ACTIVATED]\033[0m")
    for _ in range(5):
        print(f"$ {random.choice(commands)}")
        time.sleep(0.5)

if __name__ == "__main__":
    print("Matrix Terminal Simulator")
    print("1. Matrix Rain")
    print("2. Matrix Quote")
    print("3. Hacker Mode")
    
    choice = input("Choose option (1-3): ")
    
    if choice == "1":
        matrix_rain()
    elif choice == "2":
        matrix_quote()
    elif choice == "3":
        hacker_mode()
    else:
        print("Invalid choice!")
