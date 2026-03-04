import customtkinter as ctk
from PIL import Image
import data

def decksFrame(app):
    frame = ctk.CTkFrame(app, fg_color="#DDD5C9", width=1920, height=1080)

    # Holds most GUI elements
    container = ctk.CTkFrame(frame, fg_color="#DDD5C9")
    container.place(x=60, y=280, relwidth=0.9, relheight=0.65, anchor="nw")

    # Creates text, labels, and buttons for GUI
    logo_label = ctk.CTkLabel(frame, image=ctk.CTkImage(Image.open("logo.png"), size=(90, 90)), text="")
    separator = ctk.CTkFrame(frame, fg_color="#6D4120", height=6)
    navigation_frame = ctk.CTkFrame(frame, fg_color="#DDD5C9")

    # Placing
    logo_label.place(x=60, y=60, anchor="center")
    separator.place(x=0, y=120, relwidth=1.0)
    navigation_frame.place(x=200, y=60, anchor="w")

    # ---------------- Navigation Bar Section ---------------- #
    links = ["Home", "Decks", "Create", "Logout"]

    def go_home():
        app.show_frame(app.dashboardFrame)

    def go_decks():
        app.show_frame(app.decksFrame)
        refresh_decks()

    def go_create():
        app.show_frame(app.creationFrame)
        app.creationFrame.refresh_decks()

    def do_logout():
        app.current_username = None
        app.show_frame(app.loginFrame)

    actions = {
        "Home": go_home,
        "Decks": go_decks,
        "Create": go_create,
        "Logout": do_logout
    }

    active_page = "Decks"
    for text in links:
        colour = "white" if text == active_page else "#6D4120"
        navigation_button = ctk.CTkButton(navigation_frame, text=text, font=("DM Sans", 26, "bold"), fg_color="#DDD5C9", text_color=colour, hover=False, command=actions[text])
        navigation_button.pack(side="left", padx=30, pady=10)

        if text == "Logout":
            navigation_button.pack(side="right", padx=950, pady=10)

    # ---------------- Revision Window Section ---------------- #
    def start_revision(deck_name):
        username = getattr(app, "current_username", None)
        cards = data.get_cards(username, deck_name)
        
        if not cards:
            return


        revision_window = ctk.CTkToplevel(app)
        revision_window.title("Revision")
        revision_window.geometry("900x500")
        revision_window.configure(fg_color="#DDD5C9")
        revision_window.attributes("-topmost", True) # Keeps window on top

        # Variables to track state (using a dictionary to avoid 'nonlocal' issues)
        state = {"index": 0, "show_answer": False}

        def updateDisplay():
            card = cards[state["index"]]
            prog_text.configure(text=f"Card {state['index'] + 1} of {len(cards)}")
            
            if state["show_answer"]:
                card_text.configure(text=f"A: {card.get('answer', '')}")
            else:
                card_text.configure(text=f"Q: {card.get('question', '')}")

        def next_card():
            if state["index"] < len(cards) - 1:
                state["index"] += 1
                state["show_answer"] = False
                updateDisplay()

        def previous_card():
            if state["index"] > 0:
                state["index"] -= 1
                state["show_answer"] = False
                updateDisplay()

        def flip_card():
            state["show_answer"] = not state["show_answer"]
            updateDisplay()

        # UI for Revision Window
        ctk.CTkLabel(revision_window, text=deck_name, font=("DM Sans", 24, "bold"), text_color="#6D4120").pack(pady=10)
        prog_text = ctk.CTkLabel(revision_window, text="", font=("DM Sans", 16), text_color="#6D4120")
        prog_text.pack()

        display_frame = ctk.CTkFrame(revision_window, fg_color="#DDD5C9", border_color="#6D4120", border_width=2)
        display_frame.pack(expand=True, fill="both", padx=40, pady=20)

        card_text = ctk.CTkLabel(display_frame, text="", font=("DM Sans", 20, "bold"), text_color="#6D4120", wraplength=700)
        card_text.pack(expand=True)

        btn_frame = ctk.CTkFrame(revision_window, fg_color="transparent")
        btn_frame.pack(pady=20)

        ctk.CTkButton(btn_frame, text="Prev", command=previous_card, fg_color="#6D4120").pack(side="left", padx=10)
        ctk.CTkButton(btn_frame, text="Flip", command=flip_card, fg_color="#6D4120").pack(side="left", padx=10)
        ctk.CTkButton(btn_frame, text="Next", command=next_card, fg_color="#6D4120").pack(side="left", padx=10)

        updateDisplay()

    # ---------------- Deck List Section ---------------- #
    top_bar = ctk.CTkFrame(container, fg_color="#DDD5C9")
    top_bar.pack(fill="x", pady=(0, 15))

    search_entry = ctk.CTkEntry(top_bar, fg_color="#DDD5C9", width=600, height=44, text_color="#6D4120", border_color="#6D4120", border_width=2, font=("DM Sans", 18), placeholder_text="Search Decks...")
    search_entry.pack(pady=10)

    screens = ctk.CTkFrame(container, fg_color="#DDD5C9")
    screens.pack(fill="both", expand=True)

    # Screen for the list of all decks
    list_screen = ctk.CTkFrame(screens, fg_color="#DDD5C9")
    list_screen.pack(fill="both", expand=True)
    decks_list_scroll = ctk.CTkScrollableFrame(list_screen, fg_color="#DDD5C9")
    decks_list_scroll.pack(fill="both", expand=True, padx=10, pady=10)

    # Screen for viewing cards inside one specific deck
    deck_view_screen = ctk.CTkFrame(screens, fg_color="#DDD5C9")
    
    deck_title = ctk.CTkLabel(deck_view_screen, text="", font=("DM Sans", 28, "bold"), text_color="#6D4120")
    deck_title.pack(anchor="w", padx=10)

    button_row = ctk.CTkFrame(deck_view_screen, fg_color="#DDD5C9")
    button_row.pack(fill="x", pady=10)

    def show_list():
        deck_view_screen.pack_forget()
        list_screen.pack(fill="both", expand=True)

    def show_deck(name):
        frame.current_deck_name = name
        list_screen.pack_forget()
        deck_view_screen.pack(fill="both", expand=True)

        # Clear existing cards and reload
        for widget in cards_scroll.winfo_children():
            widget.destroy()

        cards = data.get_cards(app.current_username, name)
        deck_title.configure(text=f"{name} • {len(cards)} cards")

        for card in cards:
            card_box = ctk.CTkFrame(cards_scroll, fg_color="#DDD5C9", border_color="#6D4120", border_width=2)
            card_box.pack(fill="x", pady=5, padx=5)
            ctk.CTkLabel(card_box, text=f"Q: {card['question']}", font=("DM Sans", 16, "bold"), text_color="#6D4120").pack(anchor="w", padx=15, pady=(10, 2))
            ctk.CTkLabel(card_box, text=f"A: {card['answer']}", font=("DM Sans", 16), text_color="#6D4120").pack(anchor="w", padx=15, pady=(0, 10))

    back_btn = ctk.CTkButton(button_row, text="Back", fg_color="#6D4120", command=show_list)
    back_btn.pack(side="right", padx=5)

    revise_btn = ctk.CTkButton(button_row, text="Revise", fg_color="#6D4120", command=lambda: start_revision(frame.current_deck_name))
    revise_btn.pack(side="right", padx=5)

    cards_scroll = ctk.CTkScrollableFrame(deck_view_screen, fg_color="#DDD5C9")
    cards_scroll.pack(fill="both", expand=True)

    def refresh_decks():
        for widget in decks_list_scroll.winfo_children():
            widget.destroy()

        username = getattr(app, "current_username", None)
        if not username: return

        query = search_entry.get().lower()
        names = data.getDeckNames(username)

        for name in names:
            if query and query not in name.lower():
                continue

            count = len(data.get_cards(username, name))
            
            box = ctk.CTkFrame(decks_list_scroll, fg_color="#DDD5C9", border_color="#6D4120", border_width=2, height=90)
            box.pack(fill="x", pady=10, padx=5)
            box.pack_propagate(False)

            ctk.CTkLabel(box, text=f"Flashcards: {count}", font=("DM Sans", 14), text_color="#6D4120").place(x=20, y=15)
            ctk.CTkButton(box, text=name, fg_color="transparent", text_color="#6D4120", font=("DM Sans", 22, "bold"), anchor="w", command=lambda n=name: show_deck(n)).place(x=15, y=40, relwidth=0.9)

    search_entry.bind("<KeyRelease>", lambda e: refresh_decks())
    frame.refresh_decks = refresh_decks
    frame.after(200, refresh_decks)

    return frame