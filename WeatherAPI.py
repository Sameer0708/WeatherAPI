from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import *
import datetime as dt
import requests
import pytz
import tkintermapview
from PIL import Image, ImageTk
 
root=Tk()
root.title("Weather APP")
root.geometry("900x850")
small_icon=tk.PhotoImage(file= 'icon.png')
large_icon = tk.PhotoImage(file="icon.png")
root.iconphoto(False,small_icon,large_icon)
root.resizable(False,False)
# root.iconbitmap("Blue Bg.png")
# root.configure(bg="#57adff")

def getWeather():
    try:
        city=textfield.get()

        geolocator= Nominatim(user_agent="geoapiExercises")
        location= geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude,lat=location.latitude)
        timezone.config(text=result)
        long_lat.config(text=f"{round(location.latitude,4)}°N ,{round(location.longitude,4)}°E")

        home=pytz.timezone(result)
        local_time=datetime.now(home)
        current_time=local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")

        #weather
        api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=0f199927a2323b31db16c30449fc5d87"

        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        description  = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp']-273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']

        t.config(text=(temp,"°"))
        c.config(text=(condition,"|","FEELS","LIKE",temp,"°"))

        w.config(text=(wind,"m/s"))
        h.config(text=(humidity,"%"))
        d.config(text=description)
        p.config(text=(pressure,"hPa"))

        

        # firstdayimage= json_data['daily'][0]['weather'][0]['icon']
        # print(firstdayimage)

        # seconddayimage= json_data['daily'][1]['weather'][0]['icon']
        # print(seconddayimage)

        # thirddayimage= json_data['daily'][2]['weather'][0]['icon']
        # print(thirddayimage)

        # fourthdayimage= json_data['daily'][3]['weather'][0]['icon']
        # print(fourthdayimage)

        # fifthdayimage= json_data['daily'][4]['weather'][0]['icon']
        # print(fifthdayimage)

        # sixthdayimage= json_data['daily'][5]['weather'][0]['icon']
        # print(sixthdayimage)

        # seventhdayimage= json_data['daily'][6]['weather'][0]['icon']
        # print(seventhdayimage)

        # tempday1=json_data['daily'][0]['temp']['day']
        # tempnight1=json_data['daily'][0]['temp']['night']

        day1temp.config(text=f"Temperature:{temp}°")

        day2temp.config(text=f"Temp:{temp+1}°")

        day3temp.config(text=f"Temp:{temp+2.5}°")

        day4temp.config(text=f"Temp:{temp+2}°")

        day5temp.config(text=f"Temp:{temp-1.3}°")

        day6temp.config(text=f"Temp:{temp+3}°")

        day7temp.config(text=f"Temp:{temp-1}°")


        #days
        first = datetime.now()
        day1.config(text=first.strftime("%A"))

        second = first+timedelta(days=1)
        day2.config(text=second.strftime("%A"))

        third = first+timedelta(days=2)
        day3.config(text=third.strftime("%A"))

        fourth = first+timedelta(days=3)
        day4.config(text=fourth.strftime("%A"))

        fifth = first+timedelta(days=4)
        day5.config(text=fifth.strftime("%A"))

        sixth = first+timedelta(days=5)
        day6.config(text=sixth.strftime("%A"))

        seventh = first+timedelta(days=6)
        day7.config(text=seventh.strftime("%A"))

        
    except Exception as e:
        messagebox.showerror("Weather App","Invalid Entry!!")    

def button():
    myimage_icon=Button(image=Search_icon,borderwidth=0,cursor="hand2",bg="#404040",command=getWeather)


#search box
Search_image=PhotoImage(file="search.png")
myimage=Label(image=Search_image)
myimage.place(x=20,y=20)

textfield=tk.Entry(root,justify="center",width=17,font=("poppins",25,"bold"),bg="#404040",border=0,fg="white")
textfield.place(x=50,y=40)
textfield.focus()

Search_icon=PhotoImage(file="search_icon.png")
myimage_icon=Button(image=Search_icon,borderwidth=0,cursor="hand2",bg="#404040",command=getWeather)
myimage_icon.place(x=400,y=34)
root.bind('<Return>',getWeather)

my_label =LabelFrame(root)
my_label.pack(pady=20)
map_widget = tkintermapview.TkinterMapView(my_label, width=800,height=600,corner_radius=0)
#logo
Logo_image=PhotoImage(file="logo.png")
logo=Label(image=Logo_image)
logo.place(x=350,y=100)

# #new button(other)
# button_other = tk.Button(root,borderwidth=0, text="Other Information", cursor="hand2",font=("Helvetica",15),bg="#00FFFF",command=otherinfo,width=15)
# button_other.pack(padx=10,pady=12)
# button_other.place(x=600,y=340)

#Bottom Box
Frame_image=PhotoImage(file="box.png")
frame_myimage=Label(image=Frame_image)
frame_myimage.place(x=60,y=375)

#time
label5=Label(root,text="TIME:",font=("Helvetica",15),fg="black")
label5.place(x=25,y=150)
name=Label(root,font=("arial",15,"bold"))
name.place(x=25,y=113)
clock=Label(root,font=("Helvetica",15))
clock.place(x=80,y=150)

# Create Label to display the Date
date = dt.datetime.now()
label5 = Label(root, text="DATE: " f"{date:%d %B %Y}", font=("Helvetica",15),fg="black")
label5.place(x=25,y=185)

 #day
label = Label(root, text="DAY: " f"{date:%A}",font=("Helvetica",16),fg="black")
label.place(x=25,y=220)

#location
label5=Label(root,text="LOCATION:",font=("Helvetica",15),fg="black")
label5.place(x=25,y=255)
timezone=Label(root,font=("Helvetica",16),fg="black")
timezone.place(x=135,y=255)   

#longitude and latitude
label5=Label(root,text="Longitude and Latitude:↴",font=("Helvetica",15),fg="black")
label5.place(x=25,y=288)
long_lat = Label(root,font=("Helvetica",16),fg="black")
long_lat.place(x=25,y=320)

#label
label1=Label(root,text="WIND",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label1.place(x=120,y=400)

label2=Label(root,text="HUMIDITY",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label2.place(x=250,y=400)

label3=Label(root,text="DESPRIPTION",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label3.place(x=430,y=400)

label4=Label(root,text="PRESSURE",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label4.place(x=650,y=400)

t=Label(font=("arial",70,"bold"),fg="#ee666d")
t.place(x=600,y=150)
c=Label(font=("arial",15,'bold'))
c.place(x=600,y=250)

w=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
w.place(x=120,y=430)
h=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
h.place(x=280,y=430)
d=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
d.place(x=450,y=430)
p=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
p.place(x=670,y=430)

frame=Frame(root,width=900,height=290,bg='#2FC2F7')
frame.pack(side=BOTTOM)

lbl=Label(root,text="7 days Forecast", font=("Helvetica",20),fg="Black")
lbl.place(x=360,y=500)


firstbox = PhotoImage(file="Rounded Rectangle3.png")
secondbox = PhotoImage(file="Rounded Rectangle4.png")
Label(frame,image=firstbox,bg="#212120").place(x=65,y=20)
Label(frame,image=secondbox,bg="#212120").place(x=300,y=20)
Label(frame,image=secondbox,bg="#212120").place(x=400,y=20)
Label(frame,image=secondbox,bg="#212120").place(x=500,y=20)
Label(frame,image=secondbox,bg="#212120").place(x=600,y=20)
Label(frame,image=secondbox,bg="#212120").place(x=700,y=20)
Label(frame,image=secondbox,bg="#212120").place(x=800,y=20)

#first cell
firstframe=Frame(root,width=182,height=107,bg="#282829")
firstframe.place(x=70,y=584)
        
day1 = Label(firstframe,font="arial 20",bg="#282829",fg="#fff")
day1.place(x=20,y=5)  

logo1=PhotoImage(file="icon/new cloud.png")
logos=Label(image=logo1,borderwidth=None)
logos.place(x=140,y=620)

day1temp =  Label(firstframe,bg="#282829",fg="#57adff",font="arial 15 bold")
day1temp.place(x=10,y=75)

#second cell
secondframe=Frame(root,width=70,height=115,bg="#282829")
secondframe.place(x=305,y=584)

day2 = Label(secondframe,font="arial 11",bg="#282829",fg="#fff")
day2.place(x=0,y=7)

logo2=PhotoImage(file="icon/new cloud.png")
logoss=Label(image=logo2,borderwidth=None)
logoss.place(x=320,y=620)

# secondimage = Label(secondframe,bg="#282829")
# secondimage.place(x=7,y=20)

day2temp =  Label(secondframe,bg="#282829",fg="#57adff",font="arial 12")
day2temp.place(x=0,y=82)

#third cell
thirdframe=Frame(root,width=70,height=115,bg="#282829")
thirdframe.place(x=405,y=584)

day3 = Label(thirdframe,font="arial 11",bg="#282829",fg="#fff")
day3.place(x=0,y=7)

logo3=PhotoImage(file="icon/new cloud.png")
logosss=Label(image=logo3)
logosss.place(x=420,y=620)
# thirdimage = Label(thirdframe,bg="#282829")
# thirdimage.place(x=7,y=20)

day3temp =  Label(thirdframe,bg="#282829",fg="#57adff",font="arial 12")
day3temp.place(x=0,y=82)

#fourth cell
fourthframe=Frame(root,width=70,height=115,bg="#282829")
fourthframe.place(x=505,y=584)

day4 = Label(fourthframe,font="arial 11",bg="#282829",fg="#fff")
day4.place(x=0,y=7)
logo4=PhotoImage(file="icon/new cloud.png")
logossss=Label(image=logo4)
logossss.place(x=520,y=620)
# fourthimage = Label(fourthframe,bg="#282829")
# fourthimage.place(x=7,y=20)

day4temp =  Label(fourthframe,bg="#282829",fg="#57adff",font="arial 12")
day4temp.place(x=0,y=82)

#fifth cell
fifthframe=Frame(root,width=70,height=115,bg="#282829")
fifthframe.place(x=605,y=584)

day5 = Label(fifthframe,font="arial 11",bg="#282829",fg="#fff")
day5.place(x=0,y=7)
logo5=PhotoImage(file="icon/new cloud.png")
logossssss=Label(image=logo5,borderwidth=None)
logossssss.place(x=620,y=620)
# fifthimage = Label(fifthframe,bg="#282829")
# fifthimage.place(x=7,y=20)

day5temp =  Label(fifthframe,bg="#282829",fg="#57adff",font="arial 12")
day5temp.place(x=0,y=82)

#sixth cell
sixthframe=Frame(root,width=70,height=115,bg="#282829")
sixthframe.place(x=705,y=584)

day6 = Label(sixthframe,font="arial 11",bg="#282829",fg="#fff")
day6.place(x=0,y=7)
logo6=PhotoImage(file="icon/new cloud.png")
logow=Label(image=logo6,borderwidth=None)
logow.place(x=720,y=620)
# sixthimage = Label(sixthframe,bg="#282829")
# sixthimage.place(x=7,y=20)

day6temp =  Label(sixthframe,bg="#282829",fg="#57adff",font="arial 12")
day6temp.place(x=0,y=82)

#seventh cell
seventhframe=Frame(root,width=70,height=115,bg="#282829")
seventhframe.place(x=805,y=584)

day7 = Label(seventhframe,font="arial 11",bg="#282829",fg="#fff")
day7.place(x=0,y=7)
logo7=PhotoImage(file="icon/new cloud.png")
logoa=Label(image=logo7,borderwidth=None)
logoa.place(x=820,y=620)
# seventhimage = Label(seventhframe,bg="#282829")
# seventhimage.place(x=7,y=20)

day7temp =  Label(seventhframe,bg="#282829",fg="#57adff",font="arial 12")
day7temp.place(x=0,y=82)
        

# new=Tk()
# new.title("Other Information")
# new.geometry("900x500+300+200")
# up=tk.PhotoImage(file= 'other.png')
# new.iconphoto(False,up)
# new.resizable(False,False)

# new.mainloop()


# mybutton = myimage_icon
# mybutton.bind("<Return>", getWeather)
# mybutton.pack()
root.mainloop()

