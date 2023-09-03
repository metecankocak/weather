from tkinter import *
import requests
from PIL import Image, ImageTk


window = Tk()
window.title("Hava Durumu App.")
window.minsize(400,600)

my_image = Image.open("season.png")
my_photo = ImageTk.PhotoImage(my_image)
photo_label = Label(window, image=my_photo, width=100, height=100)
photo_label.pack()

my_label = Label(text= "lütfen şehir giriniz...")
my_label.pack()

my_entry = Entry()
my_entry.get()

my_entry.focus()

my_entry.pack()



def clicked_button():

    api_key = "my_api_key"   # To see how it's done, take a look at the 'readme'

    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={my_entry.get()}"


    response = requests.get(url)
    if response.status_code == 200:
        my_data = response.json()
        print(response.json())

        label1.config(text=f"Hava durumu {my_entry.get()} şehrinde şu an: {my_data['current']['condition']['text']}")

        label2.config(text=f"Sıcaklık: {my_data['current']['temp_c']} derece C")




        """if
            my_image = Image.open("season.png")
            my_photo = ImageTk.PhotoImage(my_image)
            photo_label = Label(window, image=my_photo, width=100, height=100)
            photo_label.pack()"""


my_button = Button(text="Ara", command=clicked_button)
my_button.pack()

label1 = Label(text="")
label1.pack()

"resim kontrollerini bunların altına üstüne yazman gerekiyor."

label2 = Label(text="")
label2.pack()



api_key = "5f15e35a1f7c41b29f2183640230309"

url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={my_entry}"

response = requests.get(url)

window.mainloop()

