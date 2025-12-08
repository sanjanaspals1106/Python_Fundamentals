# main.py

from utils import login, register_user

def main():
    while True:
        print("\n====== LOGIN SYSTEM ======")
        print("1. Login")
        print("2. Register")
        print("3. Exit")

        choice = input("Choose an option (1/2/3): ").strip()

        if choice == "1":
            login()

        elif choice == "2":
            register_user()

        elif choice == "3":
            print("Exiting program...")
            break

        else:
            print("Invalid option. Try again.\n")


if __name__ == "__main__":
    main()
