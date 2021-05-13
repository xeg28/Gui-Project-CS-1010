# Mason Price
# First Page
import tkinter as tk

root = tk.Tk()
root.geometry('650x700')
root.configure(bg = "red")
root.title("Create Your Own Quiz")

my_bool1=tk.BooleanVar()
my_bool2=tk.BooleanVar()
my_bool3=tk.BooleanVar()
my_bool4=tk.BooleanVar()

def func_one():
    label_3.configure(text=my_bool1.get())
    label_4.configure(text=my_bool2.get())
    label_5.configure(text=my_bool3.get())

def doButton2():
    frame_3.tkraise()



L1 = tk.Label(root, text = "Number of Questions (1-25)",height = 2, width = 30)
L1.place(rely=.15,relx=.05,relheight=.05, anchor='w')

E1 = tk.Entry(root)
E1.place(rely=.20,relx=.05,relheight=.05, anchor='w')

L2 = tk.Label(root, text = "Quiz Timer (10-90min)(0 for no timer)",height = 2, width = 30)
L2.place(rely=.35,relx=.05,relheight=.05, anchor='w')

E2 = tk.Entry(root)
E2.place(rely=.40,relx=.05,relheight=.05, anchor='w')

L3 = tk.Label(root, text = "Quiz Features",height = 2, width = 30)
L3.place(rely=.50,relx=.05,relheight=.05, anchor='w')


label_3=tk.Label(root,text=" ")
label_4=tk.Label(root,text=" ")
label_5=tk.Label(root,text=" ")

my_checkbutton_1=tk.Checkbutton(root,text="Random Questions",var=my_bool1)
my_checkbutton_2=tk.Checkbutton(root,text="Quiz Results Page",var=my_bool2)
my_checkbutton_3=tk.Checkbutton(root,text="Random Options",var=my_bool3)

my_checkbutton_1.select()

my_checkbutton_1.place(rely=.55,relx=.05,relheight=.05, anchor='w')
my_checkbutton_2.place(rely=.60,relx=.05,relheight=.05, anchor='w')
my_checkbutton_3.place(rely=.65,relx=.05,relheight=.05, anchor='w')

B1 = tk.Button(root,text="Select Features", command = func_one)
B1.place(rely=.75,relx=.05,relheight=.05, anchor='w')


B2 = tk.Button(root,text="Next Page", command = doButton2 )
B2.place(rely=.85,relx=.85,relheight=.05, anchor='w')

#Frame 3
bottom_frame = tk.Frame(root, bg="red", padx=5, pady=5)
bottom_frame.grid(row=1, column=0, padx=10, pady=10, sticky=(tk.NSEW))

bottom_frame.columnconfigure(0, weight=1)
bottom_frame.rowconfigure(0, weight=1)

frame_3 = tk.Frame(bottom_frame, bg="red")
frame_3.place(x=0, y=0, relwidth=1, relheight=1)

L1 = tk.Label(frame_3, text = "Question:",height = 2, width = 30)
L1.place(rely=.05,relx=.05,relheight=.05, anchor='w')

E1 = tk.Entry(frame_3, width = 90)
E1.place(rely=.10,relx=.05,relheight=.05, anchor='w')

L2 = tk.Label(frame_3, text = "Option A:",height = 2, width = 30)
L2.place(rely=.20,relx=.05,relheight=.05, anchor='w')


L3 = tk.Label(frame_3, text = "Option B:",height = 2, width = 30)
L3.place(rely=.35,relx=.05,relheight=.05, anchor='w')

L4 = tk.Label(frame_3, text = "Option C:",height = 2, width = 30)
L4.place(rely=.50,relx=.05,relheight=.05, anchor='w')

L5 = tk.Label(frame_3, text = "Option D:",height = 2, width = 30)
L5.place(rely=.65,relx=.05,relheight=.05, anchor='w')


my_checkbutton_1=tk.Checkbutton(frame_3,var=my_bool1)
my_checkbutton_2=tk.Checkbutton(frame_3,var=my_bool2)
my_checkbutton_3=tk.Checkbutton(frame_3,var=my_bool3)
my_checkbutton_4=tk.Checkbutton(frame_3,var=my_bool4)



my_checkbutton_1.place(rely=.25,relx=.05,relheight=.05, anchor='w')
E2 = tk.Entry(frame_3, width = 90)
E2.place(rely=.25,relx=.10,relheight=.05, anchor='w')

my_checkbutton_2.place(rely=.40,relx=.05,relheight=.05, anchor='w')
E3 = tk.Entry(frame_3, width = 90)
E3.place(rely=.40,relx=.10,relheight=.05, anchor='w')

my_checkbutton_3.place(rely=.55,relx=.05,relheight=.05, anchor='w')
E4 = tk.Entry(frame_3, width = 90)
E4.place(rely=.55,relx=.10,relheight=.05, anchor='w')

my_checkbutton_4.place(rely=.70,relx=.05,relheight=.05, anchor='w')
E5 = tk.Entry(frame_3, width = 90)
E5.place(rely=.70,relx=.10,relheight=.05, anchor='w')



root.mainloop()