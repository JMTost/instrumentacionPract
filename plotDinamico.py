
import numpy as np
import serial
import matplotlib.pyplot as plt
from tkinter import Tk, Label, Button

class VentanaEjemplo:
    def __init__(self, master):
        self.master = master
        master.title("Interfaz Practica 3")

        self.etiqueta = Label(master, text="¿Quiere mostrar la grafica?")
        self.etiqueta.pack()

        self.botonSaludo = Button(master, text="mostrar", command=self.graficar)
        self.botonSaludo.pack()

        self.botonCerrar = Button(master, text="Cerrar conexión", command=self.salir)
        self.botonCerrar.pack()

        self.botonCerrar = Button(master, text="Cerrar ventana", command=master.quit)
        self.botonCerrar.pack()

    def graficar(self):
        #plt.axis([-5000,5000,-5000,5000])
        #fig = plt.figure()
        #ax = fig.add_subplot(5000,1,1)
        #ax.spines['left'].set_position('center')
        #ax.spines['bottom'].set_position('center')
        plt.show()
        while True:
            s = ser.readline()
            val1 = s.decode().strip()
            cords = val1.split(',')
            if cords[0]!='' or cords[-1]!='':
                    if int(cords[0])<50 and int(cords[-1])>50:
                        #consideramos que el eje de las x es negativo
                        x = (-10000*(int(cords[0])/100)+5000)*-1
                        y = 10000*(int(cords[-1])/100)-5000
                        #plot
                    elif int(cords[0])<50 and int(cords[-1])<50:
                        #Ambos numeros estan en el negativo
                        x = (-10000*(int(cords[0])/100)+5000)*-1
                        y = (-10000*(int(cords[-1])/100)+5000)*-1
                        #plot
                    elif int(cords[0])>50 and int(cords[-1])<50:
                        #solo el y es negativo
                        x = 10000*(int(cords[0])/100)-5000
                        y = (-10000*(int(cords[-1])/100)+5000)*-1
                    else:
                        x = 10000*(int(cords[0])/100)-5000
                        y = 10000*(int(cords[-1])/100)-5000
                    print(x,y)
                    #plt.scatter(x,y)
                    plt.xlim(-5000, 5000,1)
                    plt.ylim(-5000,5000,1)
                    plt.axhline(0, color="black")
                    plt.axvline(0, color="black")
                    plt.scatter(x,y)
                    plt.pause(0.01)
                    plt.clf()
                    #plt.axis([-5000,5000,-5000,5000])
                    #plt.scatter(x,y)
                    #plt.pause(0.05)
                    #plt.show()     
                    #plt.clf()       
                    # plt.axis([0, 10, 0, 1])
                    # for i in range(10):
                    #     y = np.random.random()
                    #     plt.scatter(i, y)
                    #     plt.pause(0.05)
                    # plt.show()
                
    def salir(self):
        ser.close()

root = Tk()
miVentana = VentanaEjemplo(root)
ser = serial.Serial('COM3', 9600, timeout=1)
#ser.open()
root.mainloop()
# import numpy as np
# import matplotlib.pyplot as plt

# plt.axis([-5000, 5000, -5000, 5000])

# for i in range(10):
#     y = np.sin(i*5)
#     plt.scatter(i, y)
#     plt.pause(0.05)

# plt.show()