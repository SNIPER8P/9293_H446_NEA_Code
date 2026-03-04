import customtkinter as ctk
from PIL import Image
import loading
import login
import signup
import auth
import dashboard
import creation
import decks
import data


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("Study Squirrel")
        self.geometry("1920x1080")
        self.resizable(False, False)
        self.attributes("-fullscreen", True)
        self.configure(fg_color="#DDD5C9")

        self.logoImage = ctk.CTkImage(Image.open("logo.png"), size=(150,150))
        self.loadingImage = ctk.CTkImage(Image.open("logo.png"), size=(500,500))
        self.sideImage = ctk.CTkImage(Image.open("side.png"), size=(250,400))

        #Frames
        self.loadingFrame = loading.loadingFrame(self)
        self.loginFrame = login.loginFrame(self)
        self.signupFrame = signup.signupFrame(self)
        self.dashboardFrame = dashboard.dashboardFrame(self)
        self.creationFrame = creation.creationFrame(self)
        self.decksFrame = decks.decksFrame(self)

        self.current_frame = None
        self.current_username = None

        self.show_frame(self.loadingFrame)
        self.run_progress()



    #-------------- Frame Management --------------#
    def show_frame(self, frame):
        if self.current_frame:
            self.current_frame.place_forget()
        self.current_frame = frame
        self.current_frame.place(x=0, y=0)

    #-------------- Progress Bar --------------#
    def run_progress(self):
        import time
        for i in range(101):
            self.loading_progress.set(i / 100)
            self.update()
            time.sleep(0.015)
        else:
            self.show_frame(self.loginFrame)



    #-------------- Authentication --------------#
    def signup_button(self):
        username = self.username_entry.get().strip()
        email = self.email_entry.get().strip().lower()
        password = self.password_entry.get().strip()
        confirm = self.confirm_entry.get().strip()
        self.handle_signup(username, email, password, confirm)
    
    def handle_signup(self, username, email, password, confirm):
        error = auth.checkSignup(username, email, password, confirm)
        if error:
            self.feedback.configure(text=error, text_color="red")
            return

        auth.addUser(username, email, password)
        self.clear_signup()
        self.feedback.configure(text="Account created successfully!",text_color="green")

    def clear_signup(self):
        for entry in [self.username_entry, self.email_entry, self.password_entry, self.confirm_entry]:
            entry.delete(0, 'end')

    def login_button(self):
        username = self.loginFrame.username_entry.get().strip()
        password = self.loginFrame.password_entry.get().strip()
        self.handle_login(username, password)
    
    def handle_login(self, username, password):
        error = auth.checkLogin(username, password)
        if error:
            self.loginFrame.feedback.configure(text=error, text_color="red")
        else:
            self.loginFrame.feedback.configure(text="")
            self.clear_login()
            self.current_username = username
            self.dashboardFrame.welcome_label.configure(text=f"Welcome back {username}!")
            self.show_frame(self.dashboardFrame)

    def clear_login(self):
        for entry in [self.loginFrame.username_entry, self.loginFrame.password_entry]:
            entry.delete(0,'end')



    #-------------- Data Management --------------#
    def decks_current(self):
        return data.getDeckNames(self.current_username)

    def add_deck_current_user(self, deck_name):
        return data.add_deck(self.current_username, deck_name)

    def add_card_current_user(self, deck_name, question, answer):
        return data.add_card(self.current_username, deck_name, question, answer)    

if __name__ == "__main__":
    app = App()
    app.mainloop()