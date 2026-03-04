import customtkinter as ctk

def loadingFrame(app):
    frame = ctk.CTkFrame(app, fg_color="#DDD5C9", width=1920, height=1080)

    logo_label = ctk.CTkLabel(frame, image=app.loadingImage, text="")
    logo_label.place(x = 960, y = 440, anchor = "center")

    app.loading_progress = ctk.CTkProgressBar(frame, width=600, height=20, fg_color="#DDD5C9", progress_color="#7B4B3A")
    app.loading_progress.place(x=960, y=1000, anchor="center")
    app.loading_progress.set(0)
    
    return frame
