import os
import shutil
import smtplib
from email.mime.text import MIMEText
from bs4 import BeautifulSoup
import requests

def menu():
    print("\nWelcome to Python Automation Suite")
    print("1. File Organizer")
    print("2. Web Scraper (Titles from a webpage)")
    print("3. Send Email")
    print("4. Exit")
    choice = input("Enter your choice: ")
    return choice

# File Organizer
def organize_files():
    print("\nOrganizing files in the current directory...")
    files = os.listdir(".")
    for file in files:
        if os.path.isfile(file):
            ext = file.split('.')[-1]
            folder = ext.upper()
            if not os.path.exists(folder):
                os.mkdir(folder)
            shutil.move(file, f"{folder}/{file}")
    print("Files organized into folders by type.")

# Web Scraper
def web_scraper():
    url = input("\nEnter a URL to scrape titles from: ")
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        titles = soup.find_all('title')
        print("\nScraped Titles:")
        for title in titles:
            print(f" - {title.text}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Email Sender
def send_email():
    print("\nSend an Email")
    sender = input("Your email: ")
    password = input("Your email password: ")
    receiver = input("Recipient email: ")
    subject = input("Subject: ")
    body = input("Message: ")

    try:
        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = sender
        msg["To"] = receiver

        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender, password)
            server.sendmail(sender, receiver, msg.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Main Program Loop
def main():
    while True:
        choice = menu()
        if choice == "1":
            organize_files()
        elif choice == "2":
            web_scraper()
        elif choice == "3":
            send_email()
        elif choice == "4":
            print("Exiting Python Automation Suite. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()