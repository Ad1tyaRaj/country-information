from tkinter import *
from countryinfo import CountryInfo




def Info():
    country = CountryInfo(st_Enrty.get())
    st_Enrty.delete(0,END)
    wiki = country.wiki()
    name = country.name()
    population = country.population()
    region = country.region()
    provinces = country.provinces()
    borders = country.borders()
    area = country.area()
    capital = country.capital()
    currencies = country.currencies()
    languages = country.languages()




    st_1.set(wiki)
    st_2.set(name)
    st_3.set(population)
    st_4.set(region)
    st_5.set(provinces)
    st_6.set(borders)
    st_7.set(area)
    st_8.set(capital)
    st_9.set(currencies)
    st_10.set(languages)






root = Tk()
root.geometry("600x600")
root.title("Country Info")
root.config(background="#7ac5cd")
root.wm_iconbitmap("glob_1.ico")


f1 = Frame(root,bg="#6495ed",relief=SUNKEN,borderwidth=5)
f1.pack(fill="x",side=TOP,)
Lable_1= Label(f1,text="Country Infomation",font="Arial 18 bold",background="#6495ed")
Lable_1.pack()

st = StringVar()

st_Enrty = Entry(root,textvariable=st,relief=SUNKEN,width=40)
st_Enrty.pack(pady=10)

button = Button(root,text = "Submit",command=Info,bg="orange",font="Arial 10 bold")
button.pack()

# -----------------------

f2 = Frame(root,bg="#7ac5cd")


lable_2 = Label(f2,text="Wiki :",width=10)
lable_2.grid(row=0,column=0,padx=5)

st_1 = StringVar()

Lable_2 = Entry(f2,textvariable=st_1,relief=SUNKEN,width=40)
Lable_2.grid(row=0,column=5,pady=10,padx=40)


# ________________

lable_3 = Label(f2,text="Country :",width=10)
lable_3.grid(row=1,column=0,padx=5)

st_2 = StringVar()

Lable_3 = Entry(f2,textvariable=st_2,relief=SUNKEN,width=40)
Lable_3.grid(row=1,column=5,pady=10)

# ______________________

lable_4 = Label(f2,text="Population: ",width=10)
lable_4.grid(row=2,column=0,padx=5)

st_3 = StringVar()

Lable_4 = Entry(f2,textvariable=st_3,relief=SUNKEN,width=40)
Lable_4.grid(row=2,column=5,pady=10)

# ____________________


# ______________________

lable_5 = Label(f2,text="Region : ",width=10)
lable_5.grid(row=3,column=0,padx=5)

st_4 = StringVar()

Lable_5 = Entry(f2,textvariable=st_4,relief=SUNKEN,width=40)
Lable_5.grid(row=3,column=5,pady=10)

# ____________________

# ______________________

lable_6 = Label(f2,text="Provinces : ",width=10)
lable_6.grid(row=4,column=0,padx=5)

st_5 = StringVar()

Lable_6 = Entry(f2,textvariable=st_5,relief=SUNKEN,width=40)
Lable_6.grid(row=4,column=5,pady=10)

# ____________________

# ______________________

lable_7 = Label(f2,text="Borders : ",width=10)
lable_7.grid(row=5,column=0,padx=5)

st_6 = StringVar()

Lable_7 = Entry(f2,textvariable=st_6,relief=SUNKEN,width=40)
Lable_7.grid(row=5,column=5,pady=10)

# ____________________


# ______________________

lable_8 = Label(f2,text="Area : ",width=10)
lable_8.grid(row=6,column=0,padx=5)

st_7 = StringVar()

Lable_8 = Entry(f2,textvariable=st_7,relief=SUNKEN,width=40)
Lable_8.grid(row=6,column=5,pady=10)

# ____________________


# ______________________

lable_9 = Label(f2,text="Capital : ",width=10)
lable_9.grid(row=7,column=0,padx=5)

st_8 = StringVar()

Lable_9 = Entry(f2,textvariable=st_8,relief=SUNKEN,width=40)
Lable_9.grid(row=7,column=5,pady=10)

# ____________________


# ______________________

lable_10 = Label(f2,text="Currencies : ",width=10)
lable_10.grid(row=8,column=0,padx=5)

st_9 = StringVar()

Lable_10 = Entry(f2,textvariable=st_9,relief=SUNKEN,width=40)
Lable_10.grid(row=8,column=5,pady=10)

# ____________________


# ______________________

lable_11 = Label(f2,text="Languages : ",width=10)
lable_11.grid(row=9,column=0,padx=50)

st_10 = StringVar()

Lable_11 = Entry(f2,textvariable=st_10,relief=SUNKEN,width=40)
Lable_11.grid(row=9,column=5,pady=10)

# ____________________




f2.pack(fill="both",pady=40)
root.mainloop()