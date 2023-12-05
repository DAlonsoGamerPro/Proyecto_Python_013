from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
root = Tk()
root.title("POV:AntesDeSerAsaltado")
root.geometry("400x400")
root.config(bg="gray32")

input_box = Entry(root)
input_box.pack()
input_box.place(relx=0.5,rely=0.3,anchor=CENTER)

img = ImageTk.PhotoImage(Image.open('credit.jpg'))
label = Label(root, image = img)

def insertarcodigo():
    try:
        input_value = int(input_box.get())
        messagebox.showinfo("Código aceptado","El código es correcto, sacando $1,000,000...")
    except(ValueError):
        messagebox.showinfo("Error","ERROR: El código está mal, solo se permiten números, vuela a introducier el código correctamente")
        
        
btn = Button(root, text="Comprobar código", command=insertarcodigo)
btn.pack()
btn.place(relx=0.5,rely=0.4,anchor=CENTER)
label.place(relx=0.5,rely=0.7,anchor=CENTER)

root.mainloop()