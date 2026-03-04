import json
import auth

#Create a function to get user data from 
def get_user(username):
    users = auth.getUsers()
    for user in users:
        if user["username"].lower() == username.lower():
            return user


def getDeckNames(username):
    user = get_user(username)
    return list(user.get("decks", {}).keys())


def add_deck(username, deck_name):
    users = auth.getUsers()

    for user in users:
        if user["username"].lower() == username.lower():
            user.setdefault("decks", {})
            user["decks"][deck_name] = []
            break

    with open("users.json", "w") as f:
        json.dump(users, f, indent=2)


def add_card(username, deck_name, question, answer):
    users = auth.getUsers()

    for user in users:
        if user["username"].lower() == username.lower():
            user["decks"][deck_name].append({
                "question": question,
                "answer": answer
            })
            break

    with open("users.json", "w") as f:
        json.dump(users, f, indent=2)


def get_cards(username, deck_name):
    user = get_user(username)
    return user["decks"][deck_name]


