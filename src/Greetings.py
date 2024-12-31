from datetime import datetime
import pytz

# Creating some greetings based on different languages
greetings = {    # this defines the greetings in english 
    "en": {
        "morning": "Good morning",
        "afternoon": "Good afternoon",
        "evening": "Good evening",
    },
    "hi": {   # this defines the greetings in hindi 
        "morning": "सुप्रभात",
        "afternoon": "नमस्ते",
        "evening": "शुभ संध्या",
    },
    "gr": {   # this defines the greetings in greek
        "morning": "Καλημέρα",
        "afternoon": "Καλό απόγευμα",
        "evening": "Καληνύχτα"
    }
}


def log_greeting(username, greeting):
    # Log the greeting in a text file
    with open("greeting_log.txt", "a") as log_file:
        log_file.write(f"{datetime.now()}: {greeting} to {username}\n")


def greet_user(username, lang="en", timezone="Asia/Kolkata"):
    # Get the user's local time
    user_timezone = pytz.timezone(timezone)
    current_time = datetime.now(user_timezone).time()

    if current_time.hour < 12:
        greeting = greetings[lang]["morning"]
    elif 12 <= current_time.hour < 18:
        greeting = greetings[lang]["afternoon"]
    else:
        greeting = greetings[lang]["evening"]

    print(f"{greeting}, {username}!")
    log_greeting(username, greeting)


# Calling the function multiple times
# add_greeting()  Output: ['Hello!']
# add_greeting()  Output: ['Hello!', 'Hello!'] -> list continues to grow
# add_greeting()  Output: ['Hello!', 'Hello!', 'Hello!']

def add_greeting(usernames=[], new_greeting="Hello!"):  # Intentional mutable default issue
    usernames.append(new_greeting)
    print(f"Usernames: {usernames}")


def add_greeting_fixed(usernames=None, new_greeting="Hello!"):  # Correct approach
    if usernames is None:
        usernames = []
    usernames.append(new_greeting)
    print(f"Usernames: {usernames}")


def change_language(): # defines the process to get user input on language type 
    print("\nWhich language do you prefer?")
    print("1. English")
    print("2. Hindi")
    print("3. Greek")
    choice = input("Pick a number (1/2/3): ")

    if choice == "1":
        return "en"
    elif choice == "2":
        return "hi"
    elif choice == "3":
        return "gr"
    else:
        print("Not a valid option. Sticking with English.")
        return "en"


def change_timezone(): # defines the process for getting user input for time zone to determine which greeting to use 
    timezone = input("What’s your timezone? (like Asia/Kolkata, Europe/London): ")
    try:
        pytz.timezone(timezone)  # Check if the timezone is valid
        return timezone
    except pytz.UnknownTimeZoneError:
        print("Hmm, that doesn't look like a valid timezone. Defaulting to Asia/Kolkata.")
        return "Asia/Kolkata"


def display_menu(username, lang, timezone):
    while True:
        print("\nMenu:")
        print("1. Get Greeting")
        print("2. Change Language (English/Hindi/Greek)")
        print("3. Change Time Zone")
        print("4. Add Greeting with Mutable Default Argument")
        print("5. Quit")
        choice = input("What would you like to do? ")

        if choice == "1":
            greet_user(username, lang, timezone)
        elif choice == "2":
            lang = change_language()
        elif choice == "3":
            timezone = change_timezone()
        elif choice == "4":
            # Demonstrating the mutable default issue
            print("\nDemonstrating mutable default issue:")
            add_greeting()
            add_greeting()

            print("\nDemonstrating fixed version:")
            add_greeting_fixed()
            add_greeting_fixed()
        elif choice == "5":
            print("See you later!")
            break
        else:
            print("Oops! That's not a valid choice. Try again.")


def main():
    print("Hey there! Welcome to the Greeting Program!")
    username = input("What's your name? ")

    lang = "en"
    timezone = "Asia/Kolkata"

    display_menu(username, lang, timezone) # this defines what should be displayed as the final greeting 


if __name__ == "__main__":
    main()
