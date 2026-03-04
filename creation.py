import customtkinter as ctk
from PIL import Image
import threading
import ollama  
import data

def creationFrame(app):
    frame = ctk.CTkFrame(app, fg_color="#DDD5C9", width=1920, height=1080)
    
    #Holds most GUI elements
    container = ctk.CTkFrame(frame, fg_color="#DDD5C9")
    container.place(x=60, y=200, relwidth=0.9, relheight=0.65, anchor="nw")

    #Creates text, labels, and buttons for GUI
    logo_label = ctk.CTkLabel(frame,image=ctk.CTkImage(Image.open("logo.png"), size=(90, 90)),text="")
    separator = ctk.CTkFrame(frame, fg_color="#6D4120", height=6)
    navigation_frame = ctk.CTkFrame(frame, fg_color="#DDD5C9")

    #Placing
    logo_label.place(x=60, y=60, anchor="center")
    separator.place(x=0, y=120, relwidth=1.0)
    navigation_frame.place(x=200, y=60, anchor="w")

    #---------------- Navigation Bar Section ----------------#
    links = ["Home", "Decks", "Create", "Logout"]

    def go_home():
        app.show_frame(app.dashboardFrame)

    def go_decks():
        app.show_frame(app.decksFrame)
        app.decksFrame.refresh_decks()

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

    active_page = "Create"
    for text in links:
        colour = "white" if text == active_page else "#6D4120"
        navigation_button = ctk.CTkButton(navigation_frame,text=text,font=("DM Sans", 26, "bold"),fg_color="#DDD5C9",text_color=colour,hover=False,command=actions[text])
        navigation_button.pack(side="left", padx=30, pady=10)

        if text == "Logout":
            navigation_button.pack(side="right", padx=950, pady=10)

    #---------------- Manual Creation Section ----------------#
    manual = ctk.CTkFrame(container, fg_color="#DDD5C9", border_color="#6D4120", border_width=2)
    manual.place(relx=0.0, rely=0.0, relwidth=0.49, relheight=1.0, anchor="nw")

    def add_card():
        deck_name = deck_select.get().strip()
        question = question_entry.get().strip()
        answer = answer_entry.get().strip()

        if deck_name == "No decks":
            status_label.configure(text="Add a deck first")
            return

        if "" in (deck_name, question, answer):
            status_label.configure(text="Fill in deck, question, answer")
            return

        app.add_card_current_user(deck_name, question, answer)

        status_label.configure(text="Card added")
        question_entry.delete(0, "end")
        answer_entry.delete(0, "end")

    def new_deck():
        name = new_deck_entry.get().strip()
        if not name:
            return

        app.add_deck_current_user(name)

        status_label.configure(text="Deck added")
        new_deck_entry.delete(0, "end")
        refresh_decks()
        deck_select.set(name)


    def refresh_decks():
        names = app.decks_current()

        if not names:
            deck_select.configure(values=["No decks"])
            deck_select.set("No decks")
            return

        deck_select.configure(values=names)
        if deck_select.get() not in names:
            deck_select.set(names[0])

    
    #Creates text, labels, and buttons for GUI
    manual_title = ctk.CTkLabel(manual,text="Manual Creation",font=("DM Sans", 24, "bold"),text_color="#6D4120")
    status_label = ctk.CTkLabel(manual,text="",font=("DM Sans", 16),text_color="#6D4120")
    deck_label = ctk.CTkLabel(manual,text="Deck",font=("DM Sans", 18, "bold"),text_color="#6D4120")
    deck_select = ctk.CTkOptionMenu(manual,values=["No decks"],width=260,height=40,fg_color="#DDD5C9",button_color="#6D4120",button_hover_color="#6D4120",text_color="#6D4120",font=("DM Sans", 18),dropdown_fg_color="#DDD5C9",dropdown_text_color="#6D4120")
    new_deck_entry = ctk.CTkEntry(manual,width=260,height=40,fg_color="#DDD5C9",text_color="#6D4120",border_color="#6D4120",border_width=2,font=("DM Sans", 18),placeholder_text="New deck name",placeholder_text_color="#6D4120")
    add_deck_btn = ctk.CTkButton(manual,text="Add deck",width=140,height=40,fg_color="#6D4120",hover_color="#5a361b",text_color="#DDD5C9",font=("DM Sans", 18, "bold"),command=new_deck)
    question_entry = ctk.CTkEntry(manual,width=520,height=44,fg_color="#DDD5C9",text_color="#6D4120",border_color="#6D4120",border_width=2,font=("DM Sans", 18),placeholder_text='Question',placeholder_text_color="#6D4120")
    answer_entry = ctk.CTkEntry(manual,width=520,height=44,fg_color="#DDD5C9",text_color="#6D4120",border_color="#6D4120",border_width=2,font=("DM Sans", 18),placeholder_text='Answer',placeholder_text_color="#6D4120")
    add_card_btn = ctk.CTkButton(manual,text="Add card",width=160,height=44,fg_color="#6D4120",hover_color="#5a361b",text_color="#DDD5C9",font=("DM Sans", 18, "bold"),command=add_card)

    #Placing
    manual_title.place(x=30, y=25, anchor="w")
    status_label.place(x=30, y=70, anchor="w")
    deck_label.place(x=30, y=120, anchor="w")
    deck_select.place(x=30, y=165, anchor="w")
    new_deck_entry.place(x=30, y=220, anchor="w")
    add_deck_btn.place(x=310, y=220, anchor="w")
    question_entry.place(x=30, y=310, anchor="w")
    answer_entry.place(x=30, y=370, anchor="w")
    add_card_btn.place(x=30, y=440, anchor="w") 

    #---------------- AI Generation Section ----------------#
    ai = ctk.CTkFrame(container, fg_color="#DDD5C9", border_color="#6D4120", border_width=2)
    ai.place(relx=0.51, rely=0.0, relwidth=0.49, relheight=1.0, anchor="nw")

    def set_status(text, color="#6D4120"):
        ai_status.after(0, lambda: ai_status.configure(text=text, text_color=color))

    def set_button(state, text):
        generate_btn.after(0, lambda: generate_btn.configure(state=state, text=text))


    #This function should call the ollama AI and generate flashcards based on the topic the user has entered
    #Need to use llama3 and need to format the promt to get the correct response
    def call_ollama(topic, deck_name):
        set_button("disabled", "Generating...")
        set_status("Squirrel is thinking...")

        model_name = "llama3" 

        try:
            #Getting existing cards in the deck
            existing_cards = data.get_cards(app.current_username, deck_name)
            existing = set((card["question"].strip().lower(), card["answer"].strip().lower())for card in existing_cards)

            #Create a promt for the AI that will generate flashcards in a certain format
            prompt = f"""
                Create 5 flashcards about {topic}.

                Format:
                Q: question
                A: answer

                Do not include numbering or extra commentary.
                """
            result = ollama.generate(model=model_name, prompt=prompt).get("response", "")

            # Initialize counters and temporary variables for question/answer parsing
            cards_added = 0
            questions = None
            answers = None

            # Process the AI response line by line
            for line in result.split("\n"):
                line = line.strip()  # Remove extra whitespace
                if line.startswith("Q:"):  # Line contains a question
                    questions = line[2:].strip()
                elif line.startswith("A:"):  # Line contains an answer
                    answers = line[2:].strip()
                elif "|" in line:  # Some AI outputs use "Q: ... | A: ..." format
                    parts = line.split("|", 1)
                    questions = parts[0].replace("Q:", "").strip()
                    answers = parts[1].replace("A:", "").strip()

                # If both question and answer are found
                if questions and answers:
                    key = (questions.lower(), answers.lower())  # Make lowercase to avoid duplicates
                    if key not in existing:  # Only add if not already in deck
                        app.add_card_current_user(deck_name, questions, answers)
                        existing.add(key)  # Track it to prevent duplicates in the same batch
                        cards_added += 1
                    # Reset temp variables for next flashcard
                    questions = None
                    answers = None

            # Update status depending on whether new cards were added
            if cards_added == 0:
                set_status("No more flashcards can be generated.", "red")
            else:
                set_status(f"Added {cards_added} cards to {deck_name}.", "green")

        
        except Exception as e:
            set_status(f"Error: {e}", "red")

        # Ensure the button is re-enabled at the end
        finally:
            set_button("normal", "Generate")

    #Create a function that gets the topic and current deck, then it should call the ollama function in a new thread to avoid freezing the GUI while waiting for the AI response
    def generation():
        topic = topic_box.get("1.0", "end").strip()  
        deck_name = deck_select.get()

        if not topic:
            set_status("Please enter a topic first!", "red")
            return

        if deck_name == "No decks":
            set_status("Create a deck on the left first!", "red")
            return

        set_button("disabled", "Generating...")
        set_status("Ollama is thinking...")

        threading.Thread(target=call_ollama, args=(topic, deck_name), daemon=True).start()


    #Creates text, labels, and buttons for GUI
    ai_title = ctk.CTkLabel(ai, text="AI Generation", font=("DM Sans", 24, "bold"), text_color="#6D4120")
    ai_status = ctk.CTkLabel(ai, text="", font=("DM Sans", 14), text_color="#6D4120")
    topic_box = ctk.CTkTextbox(ai, width=560, height=220, fg_color="#DDD5C9", text_color="#6D4120", border_color="#6D4120", border_width=2, font=("DM Sans", 18))
    generate_btn = ctk.CTkButton(ai, text="Generate", width=160, height=44, fg_color="#6D4120", hover_color="#5a361b", text_color="#DDD5C9", font=("DM Sans", 18, "bold"), command=generation)

    #Placing
    ai_title.place(x=30, y=25, anchor="w")
    ai_status.place(x=30, y=60, anchor="w")
    topic_box.place(x=30, y=90, anchor="nw")
    generate_btn.place(x=30, y=340, anchor="w")


    frame.refresh_decks = refresh_decks
    return frame