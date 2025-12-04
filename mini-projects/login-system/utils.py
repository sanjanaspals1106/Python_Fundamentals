# utils.py

import json
import os

# -----------------------------
# Load users from JSON file
# -----------------------------
def load_users():
    if not os.path.exists("users.json"):
        return {}

    try:
        with open("users.json", "r") as f:
            return json.load(f)
    except:
        return {}


# -----------------------------
# Save users to JSON file
# -----------------------------
def save_users(users):
    with open("users.json", "w") as f:
        json.dump(users, f, indent=4)


# -----------------------------
# Load users into memory
# -----------------------------
users = load_users()

# -----------------------------
# DEBUG — DO NOT REMOVE YET
# -----------------------------
print("DEBUG → Loaded users:", users)
print("DEBUG → Using JSON file at:", os.path.abspath("users.json"))
print("-----------------------------------------")

# -----------------------------
# Check username
# -----------------------------
def user_exists(username):
    return username in users


# -----------------------------
# Register user
# -----------------------------
def register_user():
    print("====== REGISTER USER ======")
    username = input("Create username: ").strip().lower()

    if user_exists(username):
        print("User already exists, try logging in.")
        return

    while True:
        pwd1 = input("Create password: ").strip()
        pwd2 = input("Confirm password: ").strip()

        if pwd1 == pwd2:
            users[username] = pwd1
            save_users(users)
            print(f"User '{username}' created successfully!")
            return
        else:
            print("Passwords do not match! Try again.")


# -----------------------------
# Login user
# -----------------------------
def login():
    print("====== USER LOGIN ======")
    username = input("Enter username: ").strip().lower()

    if not user_exists(username):
        print("User does not exist!")
        choice = input("Do you want to register? (Yes/No): ").strip().lower()
        if choice == "yes":
            register_user()
        else:
            print("Returning to main menu.")
        return

    attempts = 3

    while attempts > 0:
        pwd = input("Enter Password: ").strip()

        if users[username] == pwd:
            print("Login Successful!")
            return
        else:
            attempts -= 1
            print(f"Wrong password! {attempts} attempts left")

    print("Too many failed attempts. LOGIN BLOCKED.")
