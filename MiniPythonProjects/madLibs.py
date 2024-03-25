import tkinter as tk

def madlibs1():
    animals = input("Enter an animal: ")
    profession = input("Enter a profession: ")
    cloth = input("Enter a piece of clothing: ")
    print(f"Once upon a time, there was a {animals} who wanted to be a {profession}.")
    print(f"The {animals} wore a {cloth} to work every day.")

def madlibs2():
    food = input("Enter a food: ")
    color = input("Enter a color: ")
    place = input("Enter a place: ")
    print(f"I love to eat {food} that is {color} in color.")
    print(f"I would love to visit {place} one day.")

def madlibs3():
    verb = input("Enter a verb: ")
    noun = input("Enter a noun: ")
    adjective = input("Enter an adjective: ")
    print(f"I love to {verb} my {noun} in the {adjective} morning.")

app = tk.Tk()

app.geometry("400x400")
app.title("Mad Libs")
tk.Label(app, text='Mad Libs Generator \n Have Fun!', font='arial 20 bold').pack()
tk.Label(app, text='Click Any One :', font='arial 15 bold').place(x=40, y=80)

tk.Button(app, text= 'The Photographer', font ='arial 15', command= madlibs1, bg = 'ghost white').place(x=60, y=120)
tk.Button(app, text= 'apple and apple', font ='arial 15', command = madlibs2 , bg = 'ghost white').place(x=70, y=180)
tk.Button(app, text= 'The Butterfly', font ='arial 15', command = madlibs3, bg = 'ghost white').place(x=80, y=240)

app.mainloop()
