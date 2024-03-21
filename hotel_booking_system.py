import customtkinter
def bookRoomButton():
    print("pressed")
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
mainWindow = customtkinter.CTk()
mainWindow.geometry("1000x700")
mainWindow.title("Booking Service")
book = customtkinter.CTkButton(mainWindow, text="Book a room", width=140, height=28, hover_color="#2057b0", command=bookRoomButton)
book.pack()
mainWindow.mainloop()
