import tkinter as tk

groot = tk.Tk()
groot.title("True or False")
groot.geometry("650x700")
groot.configure(bg='red')

my_tkVar = tk.IntVar()
my_tkVar.set(2)


L1 = tk.Label(groot, text="Question", font=('arial', 25))
L1.grid(row = 0, column = 0, pady = 2)
#L1.pack()

L2 = tk.Label(groot, text=input("Question goes here"), font=('arial', 20))
L2.grid(row = 1, column = 0, pady = 2)
#L2.pack()

my_radio_1 = tk.Radiobutton(groot)
my_radio_1.config(text=input("write true answer here"), variable=my_tkVar, value=1, font=(50), height=2, width=5)
my_radio_1.grid(row = 40, column = 0, pady = 2)
my_radio_2 = tk.Radiobutton(groot)
my_radio_2.config(text=input("write false answer here"), variable=my_tkVar, value=2, font=(50), height=2, width=5)
my_radio_2.grid(row = 60, column = 0, pady = 2)
#my_radio_1.pack()
#my_radio_2.pack()

