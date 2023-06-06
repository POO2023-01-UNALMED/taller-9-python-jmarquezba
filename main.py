from tkinter import *

# Configuración ventana principal
root = Tk()
root.title("Calculadora POO")
root.resizable(0,0)
root.geometry("290x250")

# Configuración pantalla de salida 
pantalla = Entry(root, width=22, bg="black", fg="white", borderwidth=0, font=("arial", 18, "bold"))
pantalla.grid(row=0, column=0, columnspan=4, padx=1, pady=1)

# Configuración botones
boton_1 = Button(root, text="1", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_1.grid(row=1, column=0, padx=1, pady=1)
boton_2 = Button(root, text="2", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_2.grid(row=1, column=1, padx=1, pady=1)
boton_3 = Button(root, text="3", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_3.grid(row=1, column=2, padx=1, pady=1)
boton_4 = Button(root, text="4", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_4.grid(row=2, column=0, padx=1, pady=1)
boton_5 = Button(root, text="5", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_5.grid(row=2, column=1, padx=1, pady=1)
boton_6 = Button(root, text="6", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_6.grid(row=2, column=2, padx=1, pady=1)
boton_7 = Button(root, text="7", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_7.grid(row=3, column=0, padx=1, pady=1)
boton_8 = Button(root, text="8", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_8.grid(row=3, column=1, padx=1, pady=1)
boton_9 = Button(root, text="9", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_9.grid(row=3, column=2, padx=1, pady=1)
boton_igual = Button(root, text="=", width=20, height=3, bg="red", fg="white", borderwidth=0, cursor=" hand2")
boton_igual.grid(row=4, column=0, columnspan=2, padx=1, pady=1)
boton_punto = Button(root, text=".", width=9, height=3, bg="spring green", fg="black", cursor="hand2", borderwidth=0)
boton_punto.grid(row=4, column=2, padx=1, pady=1)
boton_mas = Button(root, text="+", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2")
boton_mas.grid(row=1, column=3, padx=1, pady=1)
boton_menos = Button(root, text="-", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2")
boton_menos.grid(row=2, column=3, padx=1, pady=1)
boton_multiplicacion = Button(root, text="*",  width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2")
boton_multiplicacion.grid(row=3, column=3, padx=1, pady=1)
boton_division = Button(root, text="/", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2")
boton_division.grid(row=4, column=3, padx=1, pady=1)

boton_1.bind("<Button>", lambda x: pantalla.insert(END, "1"))
boton_2.bind("<Button>", lambda x: pantalla.insert(END, "2"))
boton_3.bind("<Button>", lambda x: pantalla.insert(END, "3"))
boton_4.bind("<Button>", lambda x: pantalla.insert(END, "4"))
boton_5.bind("<Button>", lambda x: pantalla.insert(END, "5"))
boton_6.bind("<Button>", lambda x: pantalla.insert(END, "6"))
boton_7.bind("<Button>", lambda x: pantalla.insert(END, "7"))
boton_8.bind("<Button>", lambda x: pantalla.insert(END, "8"))
boton_9.bind("<Button>", lambda x: pantalla.insert(END, "9"))
boton_igual.bind("<Button>",lambda x: calcular())
boton_punto.bind("<Button>", lambda x: pantalla.insert(END, "."))
boton_mas.bind("<Button>", lambda x: pantalla.insert(END, "+"))
boton_menos.bind("<Button>", lambda x: pantalla.insert(END, "-"))
boton_multiplicacion.bind("<Button>", lambda x: pantalla.insert(END, "*"))
boton_division.bind("<Button>", lambda x: pantalla.insert(END, "/"))

def calcular():
    calculo = pantalla.get()
    pantalla.delete(0,END)

    if (calculo.find("+")!=-1):
        P1 = calculo.find("+")
        N1= float(calculo[0:P1])
        N2= float(calculo[P1+1:])
        pantalla.insert(END,str(N1+N2))

    elif (calculo.find("-")!=-1):
        P1 = calculo.find("-")
        N1= float(calculo[0:P1])
        N2= float(calculo[P1+1:])
        pantalla.insert(END,str(N1-N2))
    
    elif (calculo.find("*")!=-1):
        P1 = calculo.find("*")
        N1= float(calculo[0:P1])
        N2= float(calculo[P1+1:])
        pantalla.insert(END,str(N1*N2))

    elif (calculo.find("/")!=-1):
        P1 = calculo.find("/")
        N1= float(calculo[0:P1])
        N2= float(calculo[P1+1:])
        pantalla.insert(END,str(N1/N2))

root.mainloop()