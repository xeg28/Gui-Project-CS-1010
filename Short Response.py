import tkinter as tk

short = tk.Tk()
short.title("Short Response")
short.geometry("650x700")
short.configure(bg='red')

lbl1 = tk.Label(short, text="Question", font=('arial', 25))
lbl1.grid(row = 0, column = 0, pady = 2)

lbl2 = tk.Label(short, text=input("Write your question here"), font=('arial', 25))
lbl2.grid(row = 1, column = 0, pady = 40)

answer = tk.Entry(short)
answer.grid(row = 3, column = 0, pady = 20)

short.mainloop()
