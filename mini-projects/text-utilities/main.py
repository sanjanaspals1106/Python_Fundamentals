from utils import (
    reverse_text,
    count_vowels,
    is_palindrome,
    char_frequency,
    remove_extra_spaces,
    find_substring
    )

def main():
    # Print menu options for the user
    print("=== Text Utilities Toolkit ===")
    print("1. Reverse text")
    print("2. Count vowels")
    print("3. Check palindrome")
    print("4. Character frequency")
    print("5. Remove extra spaces")
    print("6. Count substring occurrences")
    print("7. Exit")

    # Infinite loop to handle menu choices
    while True:
        choice = input("\nEnter your choice (1-7): ")

        # based on choice, call functions
        if choice == "1":
            word=input("Enter a word: ")
            result=reverse_text(word)
            print(result)

        elif choice == "2":
            word=input("Enter a word: ")
            result=count_vowels(word)
            print(result)

        elif choice == "3":
            word=input("Enter a word: ")
            if is_palindrome(word):
                print("Yes")
            else:
                print("No")

        elif choice == "4":
            string=input("Enter a string: ")
            print(char_frequency(string))

        elif choice == "5":
            text=input("Enter a text: ")
            print(remove_extra_spaces(text))
            

        elif choice == "6":
            string=input("Enter a string: ")
            sub_string=input("Enter substring: ")
            print(find_substring(string, sub_string))

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
