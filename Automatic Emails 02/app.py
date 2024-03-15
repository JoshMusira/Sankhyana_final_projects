import user_data
import getpass
from send_email import send_email

users = user_data.user_credentials

# Convert username values to lowercase for case-insensitive comparison
for user in users.values():
    user["username"] = user["username"].lower()


username = input('Enter your username: ').strip().lower()

password = getpass.getpass(prompt="Enter your password: ")

print("Entered Username (lowercase):", username)
print("Entered Password:", password)

# Find the user with the matching username
user_found = None
for key, value in users.items():
    if value["username"] == username:
        user_found = key
        break

# Verify if the entered username and password are correct
if user_found:
    if users[user_found]["password"] == password:
        print("Login successful!")

        # Send welcome email
        send_email(users[user_found]["email"])
    else:
        print("Password does not match.")
else:
    print("Username not found.")
