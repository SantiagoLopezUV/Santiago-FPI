import tkinter as tk


matriz = [
    ["Valle", 23.2, 88.9, 6.9, 22.8, 11.8, 5.5],
    ["Cauca", 12.3, 90.4, 13.5, 44.3, 10.8, 27.4],
    ['Nariño', 45.6, 66.4, 57.9, 87.2, 3.4, 15.6]
]


def months():
    pass
    

def state():
    data1 = []
    data2 = []
    data3 = []
    
    numerator1 = 0
    for i in matriz[0]:
        data1.append(i)
    data1.pop(0)
    cant1 = len(data1)
    for j in data1:
        numerator1 += j
    prom1 = numerator1/cant1
    print("El Promedio del Departamento: {} es: {}".format(matriz[0][0],
                                                            prom1))
    
    numerator2 = 0
    for k in matriz[1]:
        data2.append(k)
    data2.pop(0)
    cant2 = len(data2)
    for l in data2:
        numerator2 += l
    prom2 = numerator2/cant2
    print("El Promedio del Departamento: {} es: {}".format(matriz[1][0],
                                                            prom2))
    
    numerator3 = 0
    for m in matriz[2]:
        data3.append(m)
    data3.pop(0)
    cant3 = len(data3)
    for n in data3:
        numerator3 += n
    prom3 = numerator3/cant3
    print("El Promedio del Departamento: {} es: {}".format(matriz[2][0],
                                                            prom3))
    lbl_state1.config(text="El Promedio del Departamento: {} es: {}".\
        format(matriz[0][0],prom1))
    lbl_state2.config(text="El Promedio del Departamento: {} es: {}".\
        format(matriz[1][0],prom2))
    lbl_state3.config(text="El Promedio del Departamento: {} es: {}".\
        format(matriz[2][0],prom3))
    

def precipitation():
    pass





if __name__ == '__main__':
    global exit2
    root = tk.Tk()
    root.title("Control de Precipitaciones")
    root.geometry('800x800')
    
    bottom_months = tk.Button(root, text="Promedio Mes",
                            command=lambda: months())
    bottom_months.pack(pady=15)
    
    bottom_state = tk.Button(root, text="Promedio Departamento",
                            command=lambda: state())
    bottom_state.pack(pady=10)
    
    bottom_precipitation = tk.Button(root, text="Mayor Precipitacion",
                                    command=lambda: precipitation())
    bottom_precipitation.pack(pady=20)
    
    window = tk.Frame(root)
    window.pack()
    
    lbl_state1 = tk.Label(window, text="")
    lbl_state2 = tk.Label(window, text="")
    lbl_state3 = tk.Label(window, text="")
    
    lbl_state1.pack(pady=10)
    lbl_state2.pack(pady=10)
    lbl_state3.pack(pady=10)
    
    lbl_months = tk.Label(window)
    lbl_precipitation = tk.Label(window)
    lbl_precipitation.pack()

    root.mainloop()