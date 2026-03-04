import json
import hashlib


#loads user account data from users.json
def getUsers():
    try:
        with open("users.json", 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

#Checks sign-form input before creating an account and returns an error message if something is wrong.
def checkSignup(username, email, password, confirm_password):
    username = username.strip()
    email = email.strip().lower()

    if not all([username, email, password, confirm_password]):
        return "Please fill in all the fields"
    if len(username) < 5:
        return "Username must be at least 5 characters long"
    if len(username) > 25:
        return "Username cannot exceed 25 characters"
    if len(password) < 6:
        return "Password must be at least 6 characters long"
    if password != confirm_password:
        return "Passwords don't match"
    if "@" not in email or "." not in email:
        return "Invalid email address"

    #Checking for any duplicates
    users = getUsers()

    for user in users:
        if user['username'].lower() == username.lower():
            return "That username is already taken, try a different one"

        if user['email'].lower() == email:
            return "That email is already registered, try logging in instead"

    return None

#Adds a new user to the JSON file after validation succeeds.
# Passwords are hashed for security.
def addUser(username, email, password):

    users = getUsers()
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    new_user = {
        "username": username,
        "email": email,
        "password": hashed_password,
        "decks": {}
    }

    users.append(new_user)

    with open("users.json", 'w') as f:
        json.dump(users, f, indent=2)



# Verifies login credentials.
# Returns None if login successful.
# Returns error message if login fails.



def checkLogin(username, password):

    users = getUsers()

    # Hash entered password so it can be compared
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    for user in users:

        # Username comparison is case-insensitive for convenience
        if user['username'].lower() == username.lower():

            if user['password'] == hashed_password:
                return None

            else:
                return "Incorrect password"

    # Username not found after checking all users
    return "Username not found"
