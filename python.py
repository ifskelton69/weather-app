from tkinter import *
from tkinter import ttk
import requests
def data_get():
    city = city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=3526b08f47d3c37af62f90461e2a0522").json()
    w_label1.config(text = data["weather"][0]["main"])
    wb_label1.config(text= data["weather"][0]["description"])
    temp_label1.config(text=str(int(data["main"]["temp"]-273.15)))
    per_label1.config(text = data["main"]["pressure"])

win = Tk()
win.title("WHEATER APPLICATION ")
win.config(bg  = "skyblue")
win.geometry("520x520")
name_label = Label(win,text="WEATHER APPLICATION",font=("Time New Roman",25,"bold"))
name_label.place(x=25,y=50,height=50,width=450)
city_name=StringVar()
list_name = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
com = ttk.Combobox(win, text="WEATHER APPLICATION",values=list_name,font=("Time New Roman",15,"bold"),textvariable=city_name)
com.place(x=25,y=120,height=50,width=450)

done_button = Button(win,text="Done",font=("Time New Roman",15,"bold"),command=data_get)
done_button.place(x=200,y=190,height=50,width=100)

w_label = Label(win,text="WEATHER CLIMATE",font=("Time New Roman",9,"bold"))
w_label.place(x=50,y=260,height=50,width=150)

w_label1 = Label(win,text="",font=("Time New Roman",9,"bold"))
w_label1.place(x=300,y=260,height=50,width=150)

wb_label = Label(win,text="WEATHER DESCRIPTION",font=("Time New Roman",9,"bold"))
wb_label.place(x=50,y=320,height=50,width=150)

wb_label1 = Label(win,text="",font=("Time New Roman",9,"bold"))
wb_label1.place(x=300,y=320,height=50,width=150)

temp_label = Label(win,text="WEATHER TEMPERATURE",font=("Time New Roman",9,"bold"))
temp_label.place(x=50,y=380,height=50,width=150)

temp_label1 = Label(win,text="",font=("Time New Roman",9,"bold"))
temp_label1.place(x=300,y=380,height=50,width=150)

per_label = Label(win,text="PRESSURE",font=("Time New Roman",9,"bold"))
per_label.place(x=50,y=440,height=50,width=150)

per_label1 = Label(win,text="",font=("Time New Roman",9,"bold"))
per_label1.place(x=300,y=440,height=50,width=150)

win.mainloop()