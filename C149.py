from tkinter import *
import random
root=Tk()
root.title("Country Capitals")
root.geometry("500x500")
input1=Entry(root)
input1.place(relx=0.5,rely=0.2,anchor=CENTER)
input2=Entry(root)
input2.place(relx=0.5,rely=0.3,anchor=CENTER)
countrylist=[]
capitallist=[]
def addcountry():
    countryname=input1.get()
    capitalname=input2.get()
    countrylist.append(countryname)
    capitallist.append(capitalname)
    label_countrylist["text"]="Country names are:  "+str(countrylist)
    label_capitallist["text"]="Capital names are:  "+str(capitallist)
    
 
def randomcountry():
    length1=len(countrylist)
    random_number1=random.randint(0,length1-1)
    randomcountry=countrylist[random_number1]
    label_countryrandom["text"]="Random country name "+str(randomcountry)
    length2=len(capitallist)
    random_number2=random.randint(0,length2-1)
    randomcapital=capitallist[random_number2]
    label_capitalrandom["text"]="Random capital name "+str(randomcapital)
button1=Button(root,bg="royalblue",fg="white",text="Add country and capital ", command=addcountry)
button1.place(relx=0.5,rely=0.4,anchor=CENTER)
label_countrylist=Label(root)
label_countrylist.place(relx=0.5,rely=0.5,anchor=CENTER)
label_capitallist=Label(root)
label_capitallist.place(relx=0.5,rely=0.6,anchor=CENTER)
button2=Button(root,bg="royalblue",fg="white", text="Random Capital and Country: ", command=randomcountry)
button2.place(relx=0.5,rely=0.7,anchor=CENTER)
label_countryrandom=Label(root)
label_countryrandom.place(relx=0.5,rely=0.8,anchor=CENTER)
label_capitalrandom=Label(root)
label_capitalrandom.place(relx=0.5,rely=0.9,anchor=CENTER)
root.mainloop()

