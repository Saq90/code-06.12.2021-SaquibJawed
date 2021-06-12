from tkinter import *

def BMI():
    kg=int(e2.get())
    m=int(e1.get())/100
    res=kg/(m*m)
    myText.set(res)

window = Tk()
window.wm_title("BODY MASS INDEX Calculator")

l1 = Label(window,text = "HEIGHT (cm)",bg="steel blue")
l1.grid(row = 0, column =0)

l2 = Label(window,text = "WEIGHT (kg)",bg="steel blue")
l2.grid(row = 2, column = 0)

l3 = Label(window,text = "BMI result(kg/m)",bg="steel blue")
l3.grid(row = 4, column = 0)

l4 = Label(window,text = "BMI Category",bg="steel blue")
l4.grid(row = 0, column = 1)

l4 = Label(window,text = "Underweight")
l4.grid(row = 1, column = 1)

l4 = Label(window,text = " Normal weight")
l4.grid(row = 2, column = 1)

l4 = Label(window,text = "Overweight")
l4.grid(row = 3, column = 1)

l4 = Label(window,text = "Moderately obese")
l4.grid(row = 4, column = 1)

l4 = Label(window,text = "Severely obese")
l4.grid(row = 5, column = 1)

l4 = Label(window,text = "severely obese Very")
l4.grid(row = 6, column = 1)

l5 = Label(window,text = "BMI Range (kg/m2)",bg="steel blue")
l5.grid(row = 0, column = 2)

l5 = Label(window,text = "below 18.4")
l5.grid(row = 1, column = 2)

l5 = Label(window,text = "18.4 and below 18.5 - 24.9")
l5.grid(row = 2, column = 2)

l5 = Label(window,text = "25 - 29.9")
l5.grid(row = 3, column = 2)

l5 = Label(window,text = "30 - 34.9")
l5.grid(row = 4, column = 2)

l5 = Label(window,text = "35 - 39.9")
l5.grid(row = 5, column = 2)

l5 = Label(window,text = "40 and above")
l5.grid(row = 6, column = 2)

l6 = Label(window,text = "BMI Health risk",bg="steel blue")
l6.grid(row = 0, column = 3)

l6 = Label(window,text = "Malnutrition risk")
l6.grid(row = 1, column = 3)

l6 = Label(window,text = " Low risk")
l6.grid(row = 2, column = 3)

l6 = Label(window,text = " Enhanced risk")
l6.grid(row = 3, column = 3)

l6 = Label(window,text = " Medium risk")
l6.grid(row = 4, column = 3)

l6 = Label(window,text = " High risk")
l6.grid(row = 5, column = 3)

l6 = Label(window,text = "Very high risk")
l6.grid(row = 6, column = 3)

myText = StringVar()
e1 = Entry(window,textvariable= myText)
e1.grid(row = 1 , column=0)

myText = StringVar()
e2 = Entry(window,textvariable= myText)
e2.grid(row = 3 , column=0)

myText = StringVar()
result=Label(window, text="", textvariable=myText).grid(row=5,column=0)
b = Button(window, text="Calculate",bg="steel blue", command=BMI)
b.grid(row=6, column=0)


window.mainloop()