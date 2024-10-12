from datetime import datetime

def greet_user():
    # Get the current time
    current_time = datetime.now().time()

    # Determine the greeting based on the current hour
    if current_time.hour < 12:
        greeting = "Good morning!"
    elif 12 <= current_time.hour < 18:
        greeting = "Good afternoon!"
    else:
        greeting = "Good evening!"

    # Display the greeting
    print(greeting)

# Call the function to greet the user
greet_user()
