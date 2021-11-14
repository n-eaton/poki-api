import tkinter as tk
import requests




def getPokemon(canvas):
    id_or_name = textfield.get()
    api = f"https://pokeapi.co/api/v2/pokemon/{id_or_name}"
    data = requests.get(api).json()

    name = data['name']
    weight = data['weight']
    abilities = data['abilities'][0]["ability"]['name']
    experience = data['base_experience']
    height = data['height']
    final_info = str(name.upper())


    final = "\n"+"WEIGHT   " +str(weight)+"\n"+"ABILITY   " +str(abilities.upper())+"\n"+"EXPERIENCE   " +str(experience)+"\n"+"HEIGHT   " +str(height)
    # + str(weight) +"\n"+"Ability"+str(ability)

    l1.config(text = final_info)
    l2.config(text = final)

canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Pokemon Api")

f = ("poppins", 15,"bold")
t = ("poppins", 35,"bold")


textfield = tk.Entry(canvas,justify="center", font=t)
textfield.pack(pady = 20)
textfield.focus()
textfield.bind('<Return>', getPokemon)

l1 = tk.Label(canvas, font=t)
l1.pack()

l2 = tk.Label(canvas, font=f)
l2.pack()

canvas.mainloop()
