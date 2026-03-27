# Study Squirrel

A desktop flashcard revision application for students, built with Python and CustomTkinter. Study Squirrel lets you create flashcard decks manually or generate them automatically using a local AI model (Ollama), then revise them using an active recall system — all fully offline.

---

## Features

- **Account system** — register and log in with username, email and password (passwords hashed with SHA-256)
- **Manual flashcard creation** — create decks and add question/answer cards
- **AI flashcard generation** — enter any topic and automatically generate flashcards using a locally running Ollama (llama3) model
- **Deck management** — view all your decks, search by keyword, and browse cards inside each deck
- **Revision window** — flip through cards with active recall (question shown first, flip to reveal answer)
- **Motivational quotes** — rotating study quotes on the home dashboard
- **Fully offline** — all data stored locally in `users.json`, no internet required (except for the Ollama model download)

---

## Requirements

- Python 3.10 or above
- Windows 10 or above
- [Ollama](https://ollama.com) installed and running locally with the `llama3` model pulled

### Python Libraries

Install all dependencies with:

```bash
pip install customtkinter pillow ollama
```

| Library | Purpose |
|---|---|
| `customtkinter` | GUI framework |
| `Pillow` | Image loading (logo, side image) |
| `ollama` | Local AI model integration |
| `hashlib` | Password hashing (built-in) |
| `json` | Data storage (built-in) |
| `threading` | Non-blocking AI generation (built-in) |
| `random` | Quote rotation (built-in) |

---

## Setup

**1. Clone or download the project**

```bash
git clone https://github.com/yourusername/study-squirrel.git
cd study-squirrel
```

**2. Install Python dependencies**

```bash
pip install customtkinter pillow ollama
```

**3. Install Ollama and pull the llama3 model**

Download Ollama from [https://ollama.com](https://ollama.com), install it, then run:

```bash
ollama pull llama3
```

Make sure Ollama is running in the background before launching the app.

**4. Run the application**

```bash
python Main.py
```

---

## File Structure

```
study-squirrel/
│
├── Main.py              # App entry point and controller — manages frames, login, signup and data methods
├── auth.py              # Authentication logic — validates signup/login, hashes passwords, reads/writes users.json
├── data.py              # Data management — get users, decks, cards, add decks and cards to users.json
├── loading.py           # Loading screen frame with progress bar
├── login.py             # Login page GUI
├── signup.py            # Account creation page GUI
├── dashboard.py         # Home dashboard GUI with stats boxes and motivational quotes
├── creation.py          # Flashcard creation GUI — manual creation and AI generation
├── decks.py             # Deck list and deck viewer GUI — search, browse cards, open revision window
├── quotes.py            # Motivational quote pool and random selection logic
│
├── logo.png             # App logo (used on loading screen, login, and nav bar)
├── side.png             # Decorative side image (used on login and signup screens)
│
└── users.json           # Local database — stores all user accounts, decks, and flashcards
```

---

## How Data is Stored

All data is saved locally in `users.json`. No external database or cloud storage is used.

Each user is stored as a dictionary inside a list. Decks are stored as a nested dictionary inside each user, and flashcards are stored as a list of question/answer pairs inside each deck.

```json
[
  {
    "username": "daniel",
    "email": "daniel@example.com",
    "password": "5e884898da...",
    "decks": {
      "A Level Computer Science": [
        { "question": "What is RAM?", "answer": "Random Access Memory — temporary storage used by the CPU." },
        { "question": "What is a binary search?", "answer": "An efficient search algorithm that halves the search space each step." }
      ]
    }
  }
]
```

Passwords are hashed using SHA-256 before being saved, so plain text passwords are never stored.

---

## How the AI Generation Works

1. The user enters a topic in the AI Generation section of the Create page
2. A structured prompt is sent to the locally running Ollama `llama3` model asking it to generate 5 flashcards in Q:/A: format
3. The response is parsed line by line — both standard `Q: / A:` format and combined `Q: ... | A: ...` format are supported
4. Duplicate detection uses a set of existing (question, answer) pairs so repeated generation on the same topic never adds duplicate cards
5. The entire generation runs in a background thread so the GUI stays fully responsive while the model is thinking

---

## Validation Rules

| Field | Rule |
|---|---|
| Username | 5–25 characters, must be unique |
| Email | Must contain `@` and `.` |
| Password | Minimum 6 characters |
| Confirm Password | Must match Password |
| Deck name | Cannot be empty |
| Question | Cannot be empty |
| Answer | Cannot be empty |

---

## Known Limitations

- Editing and deleting existing flashcards is not available through the GUI in the current version
- Progress tracking statistics on the dashboard are not yet dynamically populated
- Spaced repetition scheduling has not been implemented
- AI generation accuracy depends on the Ollama llama3 model and cannot be guaranteed for niche topics
- Generation speed depends on the hardware running the local model
- Currently tested on Windows only

---

## Author

**Daniel Hamzepour**  
Candidate No. 9293 — Glenthorne High School (Centre: 14713)  
OCR A Level Computer Science — H446 NEA
