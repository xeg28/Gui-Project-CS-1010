  
import tkinter as tk

root = tk.Tk()
root.title("True or False")
root.geometry("650x700")
root.configure(bg='red')

my_tkVar = tk.IntVar()
my_tkVar.set(2)

frame_4 = tk.Frame(root, bg='indianred1')
frame_4.place(x=0, y=0, relwidth=1, relheight=1)
#Labels and text entries
titleLabel2 = tk.Label(frame_4,text= "Type your question in the box.", relief='solid',
                      borderwidth = 1, bg='deep sky blue', 
                      font=('Times New Roman', '24', 'bold'))
titleLabel2.place(x=0,y=0,relwidth=1,relheight=.08)

txtbox1= tk.Entry(frame_4,font=('Raleway', '12'))
txtbox1.place(relx =.05, rely=.11, relheight=.10, relwidth=.9)


my_radio_1 = tk.Radiobutton(frame_4,text=("True"), variable=my_tkVar,
                            value=1, font=('Arial','16'),bg='indianred1')
my_radio_1.place(rely = .30,relx= .08, relheight = .05, anchor = 'w')
my_radio_2 = tk.Radiobutton(frame_4,text="False", variable=my_tkVar,
                            value=2, font=('Arial','16'),bg='indianred1')

my_radio_2.place(rely = .45,relx= .08, relheight = .05, anchor = 'w')
button_1 = tk.Button(frame_4, text='Next', bg='limegreen',
                     font=('Arial','16'), width=7)
button_1.place(rely = .8, relx= .8)
