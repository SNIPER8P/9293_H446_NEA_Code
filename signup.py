import customtkinter as ctk

def signupFrame(app):
    frame = ctk.CTkFrame(app, fg_color="#DDD5C9", width=1920, height=1080)

    #Images
    logo_label = ctk.CTkLabel(frame, image=app.logoImage, text="")
    logo_label.place(x=960, y=140, anchor="center")

    side_label = ctk.CTkLabel(frame, image=app.sideImage, text="")
    side_label.place(x=0, y=680)

    #Holds all GUI elements
    container = ctk.CTkFrame(frame, fg_color="#DDD5C9")
    container.place(relx=0.5, rely=0.5, anchor="center")

    #Creates text, labels, and buttons for GUI
    signup_section = ctk.CTkFrame(container, fg_color="#DDD5C9")
    create_word = ctk.CTkLabel(container, text="Create New Account", font=("DM Sans", 40, "bold"), text_color="#6D412A")
    existing_user = ctk.CTkLabel(signup_section, text="Already Registered? ", font=("DM Sans", 13), text_color="#6D412A")
    login_label = ctk.CTkLabel(signup_section,text="Login",font=("DM Sans", 13, "underline"),text_color="#3B76C4",cursor="hand2")
    username_tag = ctk.CTkLabel(container, text="U S E R N A M E", font=("DM Sans", 13), text_color="#6D412A")
    email_tag = ctk.CTkLabel(container, text="E M A I L", font=("DM Sans", 13), text_color="#6D412A")
    password_tag = ctk.CTkLabel(container, text="P A S S W O R D", font=("DM Sans", 13), text_color="#6D412A")
    signup_button = ctk.CTkButton(container,text="Sign Up",width=100,height=45,font=("DM Sans", 16),fg_color="#00BF6B",hover_color="#00a65c",command=app.signup_button)

    #Alerts
    app.feedback = ctk.CTkLabel(container,text="",font=("DM Sans", 13),text_color="red")

    #Entrys
    app.username_entry = ctk.CTkEntry(container,placeholder_text="Enter your username",width=300,height=40,font=("DM Sans", 16),border_color="#6D412A",border_width=2,text_color="#6D412A",fg_color="#FFFFFF",placeholder_text_color="#6D412A")
    app.email_entry = ctk.CTkEntry(container,placeholder_text="Enter your email",width=300,height=40,font=("DM Sans", 16),border_color="#6D412A",border_width=2,text_color="#6D412A",fg_color="#FFFFFF",placeholder_text_color="#6D412A")
    app.password_entry = ctk.CTkEntry(container,placeholder_text="Enter your password",width=300,height=40,font=("DM Sans", 16),border_color="#6D412A",border_width=2,text_color="#6D412A",fg_color="#FFFFFF",placeholder_text_color="#6D412A",show="*")
    app.confirm_entry = ctk.CTkEntry(container,placeholder_text="Confirm your password",width=300,height=40,font=("DM Sans", 16),border_color="#6D412A",border_width=2,text_color="#6D412A",fg_color="#FFFFFF",placeholder_text_color="#6D412A",show="*")
    
    #Packing
    existing_user.pack(side="left")
    create_word.pack()
    signup_section.pack(pady=(0, 10))
    login_label.pack(side="left")
    username_tag.pack(anchor="w", pady=(5, 0), padx=(42, 0))
    app.username_entry.pack(pady=(0, 8))
    email_tag.pack(anchor="w", pady=(5, 0), padx=(42, 0))
    app.email_entry.pack(pady=(0, 8))
    password_tag.pack(anchor="w", pady=(5, 0), padx=(42, 0))
    app.password_entry.pack(pady=(0, 8))
    app.confirm_entry.pack(pady=(0, 8))
    app.feedback.pack(pady=(5, 0))
    signup_button.pack(pady=(8, 150))

    #Transfer to login frame
    def transferLogin(e):
        app.show_frame(app.loginFrame)
    login_label.bind("<Button-1>", transferLogin)


    return frame 

