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

frame_3 = tk.Frame(root, bg="red")
frame_3.place(x=0, y=0, relwidth=1, relheight=1)

bottom_frame = tk.Frame(root, bg="indianred1",)
bottom_frame.place(x=0, y=0, relwidth=1, relheight=1)

TitleLabel = tk.Label(bottom_frame,text= "Create Your Own Quiz", relief='solid',
                      borderwidth = 1, bg='deep sky blue', 
                      font=('Times New Roman', '24', 'bold'))
TitleLabel.place(x=0, y=0, relwidth = 1, relheight = .08)

L1 = tk.Label(bottom_frame, text = "Number of Questions (1-25)",height = 2, width = 25,
              bg='indianred1', font=('Arial','16'))
L1.place(rely=.15,relx=.045,relheight=.05, anchor='w')

E1 = tk.Entry(bottom_frame)
E1.place(rely=.20,relx=.08,relheight=.05, anchor='w')

L2 = tk.Label(bottom_frame, text = "Quiz Timer (10-90min)(0 for no timer)",height = 2,
              width = 30, bg='indianred1', font=('Arial','16'))
L2.place(rely=.35,relx=.06,relheight=.05, anchor='w')

E2 = tk.Entry(bottom_frame)
E2.place(rely=.40,relx=.08,relheight=.05, anchor='w')

L3 = tk.Label(bottom_frame, text = "Quiz Features",height = 2, width = 12,
               bg='indianred1', font=('Arial','16'))
L3.place(rely=.50,relx=.065,relheight=.05, anchor='w')



my_checkbutton_1=tk.Checkbutton(bottom_frame,text="Random Questions",var=my_bool1,
                                bg='indianred1', font=('Arial','12'))
my_checkbutton_2=tk.Checkbutton(bottom_frame,text="Quiz Results Page",var=my_bool2,
                                 bg='indianred1', font=('Arial','12'))
my_checkbutton_3=tk.Checkbutton(bottom_frame,text="Random Options",var=my_bool3,
                                 bg='indianred1', font=('Arial','12'))

my_checkbutton_1.place(rely=.55,relx=.08,relheight=.05, anchor='w')
my_checkbutton_2.place(rely=.60,relx=.08,relheight=.05, anchor='w')
my_checkbutton_3.place(rely=.65,relx=.08,relheight=.05, anchor='w')

B1 = tk.Button(bottom_frame,text="Select Features",font=('Arial','12'),
               command = func_one)
B1.place(rely=.72,relx=.08,relheight=.05, anchor='w')


B2 = tk.Button(bottom_frame,text="Next", bg='limegreen', width=7,
               font=('Arial','16'), command = doButton2  )
B2.place(rely=.85,relx=.8,relheight=.05, anchor='w')

#Frame 3



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
my_checkbutton_4=tk.Checkbutton(frame_3,var=my_bool3)



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
