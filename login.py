import customtkinter as ctk

def loginFrame(app):
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
    login_section = ctk.CTkFrame(container, fg_color="#DDD5C9")
    login_word = ctk.CTkLabel(container, text="Login", font=("DM Sans", 40, "bold"), text_color="#6D412A")
    new_user = ctk.CTkLabel(login_section, text="New to Study Squirrel? ", font=("DM Sans", 13), text_color="#6D412A")
    create_label = ctk.CTkLabel(login_section,text="Create Account",font=("DM Sans", 13, "underline"),text_color="#3B76C4",cursor="hand2")
    username_tag = ctk.CTkLabel(container, text="U S E R N A M E", font=("DM Sans", 13), text_color="#6D412A")
    password_tag = ctk.CTkLabel(container, text="P A S S W O R D", font=("DM Sans", 13), text_color="#6D412A")
    login_button = ctk.CTkButton(container,text="Login",width=100,height=45,font=("DM Sans", 16),fg_color="#00BF6B", hover_color="#00a65c",command=app.login_button)

    #Entrys
    frame.password_entry = ctk.CTkEntry(container,placeholder_text="Enter your password",width=300,height=40,font=("DM Sans", 16),border_color="#6D412A",border_width=2,text_color="#6D412A",fg_color="#FFFFFF",placeholder_text_color="#6D412A",show="*")
    frame.username_entry = ctk.CTkEntry(container,placeholder_text="Enter your username",width=300,height=40,font=("DM Sans", 16),border_color="#6D412A",border_width=2,text_color="#6D412A",fg_color="#FFFFFF",placeholder_text_color="#6D412A")
    frame.feedback = ctk.CTkLabel(container, text="", font=("DM Sans", 13), text_color="red")

    #Packing
    new_user.pack(side="left")
    login_word.pack()
    login_section.pack(pady=(0, 10))
    create_label.pack(side="left")
    username_tag.pack(anchor="w", pady=(5, 0), padx=(1, 0))
    frame.username_entry.pack(pady=(0, 8))
    password_tag.pack(anchor="w", pady=(5, 0), padx=(1, 0))
    frame.password_entry.pack(pady=(0, 8))
    frame.feedback.pack(pady=(5, 0))
    login_button.pack(pady=(8, 280))
    
    #Transfer to create account frame
    def transferCreate(e):
        app.show_frame(app.signupFrame)
    create_label.bind("<Button-1>", transferCreate)



    return frame 