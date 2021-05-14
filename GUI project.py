# Mason Price
# First Page
import tkinter as tk

root = tk.Tk()
root.geometry('650x700')
root.configure(bg = "indianred1")
root.title("Create Your Own Quiz")

my_bool1=tk.BooleanVar()
my_bool2=tk.BooleanVar()
my_bool3=tk.BooleanVar()
my_bool4=tk.BooleanVar()

def func_one():
    RandomQues = my_bool1.get()
    QuizResults = my_bool2.get()
    RandomOpt= my_bool3.get()

def doButton2():
    frame_3.tkraise()

def doButton3():
    frame_6.tkraise()

def doButton8():
    frame_8.tkraise()

def doButton9():
    bottom_frame.tkraise()

frame_3 = tk.Frame(root, bg="red")
frame_3.place(x=0, y=0, relwidth=1, relheight=1)

bottom_frame = tk.Frame(root, bg="indianred1",)
bottom_frame.place(x=0, y=0, relwidth=1, relheight=1)

TitleLabel = tk.Label(bottom_frame,text= "Create Your Own Quiz", relief='solid',borderwidth = 1, bg='deep sky blue', font=('Times New Roman', '24', 'bold'))
TitleLabel.place(x=0, y=0, relwidth = 1, relheight = .08)

L1 = tk.Label(bottom_frame, text = "Number of Questions (1-25)",height = 2, width = 25,bg='indianred1', font=('Arial','16'))
L1.place(rely=.15,relx=.045,relheight=.05, anchor='w')

E1 = tk.Entry(bottom_frame)
E1.place(rely=.20,relx=.08,relheight=.05, anchor='w')

L2 = tk.Label(bottom_frame, text = "Quiz Timer (10-90min)(0 for no timer)",height = 2,width = 30, bg='indianred1', font=('Arial','16'))
L2.place(rely=.35,relx=.06,relheight=.05, anchor='w')

E2 = tk.Entry(bottom_frame)
E2.place(rely=.40,relx=.08,relheight=.05, anchor='w')

L3 = tk.Label(bottom_frame, text = "Quiz Features",height = 2, width = 12,bg='indianred1', font=('Arial','16'))
L3.place(rely=.50,relx=.065,relheight=.05, anchor='w')



my_checkbutton_1=tk.Checkbutton(bottom_frame,text="Random Questions",var=my_bool1,bg='indianred1', font=('Arial','12'))
my_checkbutton_2=tk.Checkbutton(bottom_frame,text="Quiz Results Page",var=my_bool2, bg='indianred1', font=('Arial','12'))
my_checkbutton_3=tk.Checkbutton(bottom_frame,text="Random Options",var=my_bool3,bg='indianred1', font=('Arial','12'))

my_checkbutton_1.place(rely=.55,relx=.08,relheight=.05, anchor='w')
my_checkbutton_2.place(rely=.60,relx=.08,relheight=.05, anchor='w')
my_checkbutton_3.place(rely=.65,relx=.08,relheight=.05, anchor='w')

B1 = tk.Button(bottom_frame,text="Select Features",font=('Arial','12'),command = func_one)
B1.place(rely=.72,relx=.08,relheight=.05, anchor='w')


B2 = tk.Button(bottom_frame,text="Next", bg='limegreen', width=7,font=('Arial','16'), command = doButton2  )
B2.place(rely=.85,relx=.8,relheight=.05, anchor='w')

#Frame 3
bottom_frame = tk.Frame(root, bg="indianred1", padx=5, pady=5)
bottom_frame.grid(row=1, column=0, padx=10, pady=10, sticky=(tk.NSEW))

bottom_frame.columnconfigure(0, weight=1)
bottom_frame.rowconfigure(0, weight=1)

frame_3 = tk.Frame(root, bg="indianred1")
frame_3.place(x=0, y=0, relwidth=1, relheight=1)

TitleLabel = tk.Label(frame_3,text= "Create Your Own Quiz", relief='solid',borderwidth = 1, bg='deep sky blue', font=('Times New Roman', '24', 'bold'))
TitleLabel.place(x=0, y=0, relwidth = 1, relheight = .08)

L4 = tk.Label(frame_3, text = "Question:",height = 2, width = 30,bg="indianred1", font=('Arial','16'))
L4.place(rely=.11,relx=.05,relheight=.05, anchor='w')

E3 = tk.Entry(frame_3, width = 90)
E3.place(rely=.15,relx=.05,relheight=.05, anchor='w')

L5 = tk.Label(frame_3, text = "Option A:",height = 2, width = 30,bg="indianred1", font=('Arial','16'))
L5.place(rely=.20,relx=.05,relheight=.05, anchor='w')

L6 = tk.Label(frame_3, text = "Option B:",height = 2, width = 30,bg="indianred1", font=('Arial','16'))
L6.place(rely=.35,relx=.05,relheight=.05, anchor='w')

L7 = tk.Label(frame_3, text = "Option C:",height = 2, width = 30,bg="indianred1", font=('Arial','16'))
L7.place(rely=.50,relx=.05,relheight=.05, anchor='w')

L8 = tk.Label(frame_3, text = "Option D:",height = 2, width = 30,bg="indianred1", font=('Arial','16'))
L8.place(rely=.65,relx=.05,relheight=.05, anchor='w')


my_checkbutton_1=tk.Checkbutton(frame_3,var=my_bool1,bg="indianred1", font=('Arial','16'))
my_checkbutton_2=tk.Checkbutton(frame_3,var=my_bool2,bg="indianred1", font=('Arial','16'))
my_checkbutton_3=tk.Checkbutton(frame_3,var=my_bool3,bg="indianred1", font=('Arial','16'))
my_checkbutton_4=tk.Checkbutton(frame_3,var=my_bool4,bg="indianred1", font=('Arial','16'))



my_checkbutton_1.place(rely=.25,relx=.05,relheight=.05, anchor='w')
E4 = tk.Entry(frame_3, width = 90)
E4.place(rely=.25,relx=.10,relheight=.05, anchor='w')

my_checkbutton_2.place(rely=.40,relx=.05,relheight=.05, anchor='w')
E5 = tk.Entry(frame_3, width = 90)
E5.place(rely=.40,relx=.10,relheight=.05, anchor='w')

my_checkbutton_3.place(rely=.55,relx=.05,relheight=.05, anchor='w')
E6 = tk.Entry(frame_3, width = 90)
E6.place(rely=.55,relx=.10,relheight=.05, anchor='w')

my_checkbutton_4.place(rely=.70,relx=.05,relheight=.05, anchor='w')
E7 = tk.Entry(frame_3, width = 90)
E7.place(rely=.70,relx=.10,relheight=.05, anchor='w')

B3 = tk.Button(frame_3,text="Next", bg='limegreen', width=7,font=('Arial','16'), command = doButton2  )
B3.place(rely=.85,relx=.8,relheight=.05, anchor='w')

#Frame 6

bottom_frame = tk.Frame(root, bg="indianred1", padx=5, pady=5)
bottom_frame.grid(row=1, column=0, padx=10, pady=10, sticky=(tk.NSEW))

bottom_frame.columnconfigure(0, weight=1)
bottom_frame.rowconfigure(0, weight=1)

frame_6 = tk.Frame(root, bg="indianred1")
frame_6.place(x=0, y=0, relwidth=1, relheight=1)

my_tkVar = tk.IntVar()
my_tkVar.set(2)

TitleLabel = tk.Label(frame_6,text= "True or False Question Appearance", relief='solid',borderwidth = 1, bg='deep sky blue', font=('Times New Roman', '24', 'bold'))
TitleLabel.place(x=0, y=0, relwidth = 1, relheight = .08)

L9 = tk.Label(frame_6, text = "Type Question:",height = 2, width = 30,bg="indianred1", font=('Arial','16'))
L9.place(rely=.11,relx=.05,relheight=.05, anchor='w')

E8 = tk.Entry(frame_6, width = 90)
E8.place(rely=.15,relx=.05,relheight=.05, anchor='w')

my_radio_1 = tk.Radiobutton(frame_6,text=("True"), variable=my_tkVar,value=1, font=('Arial','16'),bg='indianred1')
my_radio_1.place(rely = .30,relx= .08, relheight = .05, anchor = 'w')

my_radio_2 = tk.Radiobutton(frame_6,text="False", variable=my_tkVar,value=2, font=('Arial','16'),bg='indianred1')
my_radio_2.place(rely = .45,relx= .08, relheight = .05, anchor = 'w')


B3 = tk.Button(frame_6,text="Next", bg='limegreen', width=7,font=('Arial','16'), command = doButton2  )
B3.place(rely=.85,relx=.8,relheight=.05, anchor='w')

#Frame 8

bottom_frame = tk.Frame(root, bg="indianred1", padx=5, pady=5)
bottom_frame.grid(row=1, column=0, padx=10, pady=10, sticky=(tk.NSEW))

bottom_frame.columnconfigure(0, weight=1)
bottom_frame.rowconfigure(0, weight=1)

frame_8 = tk.Frame(bottom_frame, bg="indianred1")
frame_8.place(x=0, y=0, relwidth=1, relheight=1)

TitleLabel = tk.Label(frame_8,text= "Quiz Results", relief='solid',borderwidth = 1, bg='deep sky blue', font=('Times New Roman', '24', 'bold'))
TitleLabel.place(x=0, y=0, relwidth = 1, relheight = .08)

L10 = tk.Label(frame_8, text = "Score:",height = 2, width = 30,bg="indianred1", font=('Arial','16'))
L10.place(rely=.11,relx=.01,relheight=.05, anchor='w')

L11 = tk.Label(frame_8, text = "Question:",height = 2, width = 30,bg="indianred1", font=('Arial','16'))
L11.place(rely=.16,relx=.01,relheight=.05, anchor='w')

def func_two():
    str_var1 = E1.get()
    L1.configure(text = str_var1)
    if str_var1 == int:
        L11.place(rely=.11,relx=.05,relheight=.05, anchor='w')*str_var1

B3 = tk.Button(frame_8,text="Show Questions",width=15,font=('Arial','16'), command = func_two  )
B3.place(rely=.85,relx=.01,relheight=.05, anchor='w')

B3 = tk.Button(frame_8,text="Reset", bg='limegreen', width=7,font=('Arial','16'), command = doButton9  )
B3.place(rely=.85,relx=.8,relheight=.05, anchor='w')

    


root.mainloop()