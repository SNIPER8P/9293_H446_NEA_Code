import customtkinter as ctk
from PIL import Image
from quotes import get_new_quote

def dashboardFrame(app):
    frame = ctk.CTkFrame(app, fg_color="#DDD5C9", width=1920, height=1080)
    
    #Holds all GUI elements
    container = ctk.CTkFrame(frame, fg_color="#DDD5C9")
    container.place(x=60, y=280, relwidth=0.9, relheight=0.65, anchor="nw")

    #Creates text, labels, and buttons for GUI
    logo_label = ctk.CTkLabel(frame, image=ctk.CTkImage(Image.open("logo.png"), size=(90, 90)), text="")
    separator = ctk.CTkFrame(frame, fg_color="#6D4120", height=6)
    navigation_frame = ctk.CTkFrame(frame, fg_color="#DDD5C9")
    frame.welcome_label = ctk.CTkLabel(frame, text="Welcome back!", font=("DM Sans", 30), fg_color="#DDD5C9", text_color="#6D4120")
    study_box = ctk.CTkFrame(container,fg_color="#DDD5C9",border_color="#6D4120",border_width=3,corner_radius=28,width=430,height=160)
    study_word = ctk.CTkLabel(study_box,text="Today’s Study Time",font=("DM Sans", 16, "bold"),fg_color="#DDD5C9",text_color="#6D4120")
    accuracy_box = ctk.CTkFrame(container,fg_color="#DDD5C9",border_color="#6D4120",border_width=3,corner_radius=28,width=430,height=140)
    accuracy_word = ctk.CTkLabel(accuracy_box,text="Accuracy",font=("DM Sans", 16, "bold"),fg_color="#DDD5C9",text_color="#6D4120")
    streak_box = ctk.CTkFrame(container,fg_color="#DDD5C9",border_color="#6D4120",border_width=3,corner_radius=28,width=430,height=140)
    streak_word = ctk.CTkLabel(streak_box,text="Streak",font=("DM Sans", 16, "bold"),fg_color="#DDD5C9",text_color="#6D4120")
    quote_label = ctk.CTkLabel(container,text=get_new_quote(),font=("DM Sans", 40, "bold"),fg_color="#DDD5C9",text_color="#6D4120",justify="center",wraplength=700)

    #Placing
    logo_label.place(x=60, y=60, anchor="center")
    separator.place(x=0, y=120, relwidth=1.0)
    navigation_frame.place(x=200, y=60, anchor="w")
    frame.welcome_label.place(x=200,y=200, anchor="w")
    study_box.place(x=100, y=40)
    study_word.place(x=42, y=18, anchor="w")
    accuracy_box.place(x=100, y=235)
    accuracy_word.place(x=42, y=18, anchor="w")
    streak_box.place(x=100, y=410)
    streak_word.place(x=42, y=18, anchor="w")
    quote_label.place(x=950, y=260)

    def refresh_quote():
        quote_label.configure(text=get_new_quote())
        frame.after(15000, refresh_quote)
    refresh_quote()

    
    #-------------------- Navigation bar section--------------------#
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

    active_page = "Home"
    for text in links:
        colour = "white" if text == active_page else "#6D4120"
        navigation_button = ctk.CTkButton(navigation_frame, text=text, font=("DM Sans", 26, "bold"), fg_color="#DDD5C9", text_color=colour, hover=False, command=actions[text])
        navigation_button.pack(side="left", padx=30, pady=10)

        if text == "Logout":
            navigation_button.pack(side="right", padx=950, pady=10)

    #---------------------------------------------------------------#

    return frame
