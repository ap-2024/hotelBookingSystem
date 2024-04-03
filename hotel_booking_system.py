import csv
import customtkinter
def bookRoomButton():
    with open('hotelBookingList.csv') as csvfile:
        file = csv.reader(csvfile)
        for value in file:
            if value[1] == "open":
                print("Room", value[0], "is", value[1]+".")                
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
mainWindow = customtkinter.CTk()
mainWindow.geometry("1000x700")
mainWindow.title("Booking Service")
book = customtkinter.CTkButton(mainWindow, text="Book a room", width=140, height=28, hover_color="#2057b0", command=bookRoomButton)
book.pack()
book.place(x=430, y=310)
mainWindow.mainloop()
