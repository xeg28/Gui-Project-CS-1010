
#change the actual variables

# Mason Price
# Emmanuel Gonzalez
# Romario Sontay
# First Page
import tkinter as tk
import tkinter.messagebox
import random
from random import choice
root = tk.Tk()
root.geometry('650x700')
root.configure(bg = "indianred1")
root.title("Create Your Own Quiz")
#Check box variables


bool1=tk.BooleanVar()
bool1.set(False)
bool2=tk.BooleanVar()
bool2.set(True)
bool3=tk.BooleanVar()
bool3.set(False)

myBool1=tk.BooleanVar()
myBool1.set(False)
myBool2=tk.BooleanVar()
myBool2.set(False)
myBool3=tk.BooleanVar()
myBool3.set(False)
myBool4=tk.BooleanVar()
myBool4.set(False)
myBool5=tk.BooleanVar()
myBool5.set(False)

RadioVar = tk.IntVar()
RadioVar.set(0)

radioVar1 = tk.IntVar()
radioVar1.set(0)
#Lists and Variables(Very Important)
titleVar = 0
qTypes= []
questions = []
answers = []
quesType=0
randans = []
randAnswers = []
list1= []
options = []
i = -1
u = 0
q = 1
z = 2
n = 3
t = 4
score = 0


def doButton9():
    exit()

def results():
    global percent
    #RESULTS PAGE
    frame_8r.tkraise()
    frame_10 = tk.Frame(frame_8r, bg = 'deep sky blue')
    frame_10.place(relx=.22, rely=.12, width=365, height=261)
    frame_9 = tk.Frame(frame_8r, bg = '#f8f8f8')
    frame_9.place(relx=.25, rely=.15, width=325, height=220)

    TitleLabelr = tk.Label(frame_8r,text= "Quiz Results", relief='solid',borderwidth = 1, bg='deep sky blue',
                           font=('Times New Roman', '24', 'bold'))
    TitleLabelr.place(x=0, y=0, relwidth = 1, relheight = .08)

    L10r = tk.Label(frame_9, text = "Score:" + str(score) +'/'+ str(numOfQues),height = 2, width = 13,bg="white",
                    font=('Arial','30','bold'))
    L10r.grid(row = 0, column=0)

    L11r = tk.Label(frame_9, text = str(percent)+'%',height = 2, width = 13,bg="white",
                    font=('Arial','30','bold'))
    L11r.grid(row=1, column=0)
    B3 = tk.Button(frame_8r,text="EXIT",width=15,bg='limegreen',
               font=('Arial','16'), command = doButton9  )
    B3.place(rely=.65,relx=.60,relheight=.08, anchor='w')
def option(l,o,s,t):
    #radio buttons in frame 7
    global RadioVar

    radio1 = tk.Radiobutton(frame_7)
    radio1.config(text=options[l], variable=RadioVar, value=1,
                   bg='indianred1', font=('Arial', '16'))
    radio2 = tk.Radiobutton(frame_7)
    radio2.config(text=options[o], variable=RadioVar, value=2,
                   bg='indianred1', font=('Arial', '16'))
    radio3 = tk.Radiobutton(frame_7)
    radio3.config(text=options[s], variable=RadioVar, value=3,
                   bg='indianred1', font=('Arial', '16'))
    radio4 = tk.Radiobutton(frame_7)
    radio4.config(text=options[t], variable=RadioVar, value=4,
                   bg='indianred1', font=('Arial', '16'))
    radio1.place(rely = .25,relx= .1, relheight = .05, anchor = 'w')
    radio2.place(rely = .35,relx= .1, relheight = .05, anchor = 'w')
    radio3.place(rely = .45,relx= .1, relheight = .05, anchor = 'w')
    radio4.place(rely = .55,relx= .1, relheight = .05, anchor = 'w')

def option2(w,e,r,t,y):
    #radio buttons in frame 8
    global radioVar1
    radioVar1 = tk.IntVar()
    radioVar1.set(0)
    Radio_1 = tk.Radiobutton(frame_8)
    Radio_1.config(text=options[w], variable=radioVar1, value=1,
                   bg='indianred1', font=('Arial', '16'))
    Radio_2 = tk.Radiobutton(frame_8)
    Radio_2.config(text=options[e], variable=radioVar1, value=2,
                   bg='indianred1', font=('Arial', '16'))
    Radio_3 = tk.Radiobutton(frame_8)
    Radio_3.config(text=options[r], variable=radioVar1, value=3,
                   bg='indianred1', font=('Arial', '16'))
    Radio_4 = tk.Radiobutton(frame_8)
    Radio_4.config(text=options[t], variable=radioVar1, value=4,
                   bg='indianred1', font=('Arial', '16'))
    Radio_5 = tk.Radiobutton(frame_8)
    Radio_5.config(text=options[y], variable=radioVar1, value=5,
                   bg='indianred1', font=('Arial', '16'))
    Radio_1.place(rely = .25,relx= .1, relheight = .05, anchor = 'w')
    Radio_2.place(rely = .35,relx= .1, relheight = .05, anchor = 'w')
    Radio_3.place(rely = .45,relx= .1, relheight = .05, anchor = 'w')
    Radio_4.place(rely = .55,relx= .1, relheight = .05, anchor = 'w')
    Radio_5.place(rely = .65,relx= .1, relheight = .05, anchor = 'w')
def question():
    global i
    global u
    global q
    global z
    global n
    global t
    global score
    global percent
    fVar=0
    if qTypes[i]==1:  
        if RadioVar.get() == answers[i]:
            score+=1
            fVar = 1
            fix = 0
    if qTypes[i]==2:  
        if radioVar1.get() == answers[i]:
            score+=1
            fVar=0
            fix = 1
    if qTypes[i]==3:
        print('')
        
    i += 1
    qTypes.append(100)
    if i != 0 and qTypes[i]==1:
        if fix != 0:
            u += 5
            q += 5
            z += 5
            n += 5
        else:
            u += 4
            q += 4
            z += 4
            n += 4
        fVar = 1
    if i != 0 and qTypes[i]==2:
        if fVar != 0:
            u += 4
            q += 4
            z += 4
            n += 4
            t += 4
        else:
            u += 5
            q += 5
            z += 5
            n += 5
            t += 5
    if i == numOfQues:
        percent = round(score/numOfQues*100,1)
        results()
     
    else:
        if qTypes[i] == 1:
            frame_7.tkraise()
            test(i)
            option(u,q,z,n)

        elif qTypes[i] == 2:
            frame_8.tkraise()
            test(i)
            option2(u,q,z,n,t)
            
      
    if qTypes[i] == 3:
        print('')
    elif qTypes[i] == 4:
        print('')

    print(score)
def test(y):
    #labels in frame 7
    text_1 = tk.Text(frame_7,bg='deep sky blue',
                      font=('Times New Roman', '20', 'bold'))
    text_1.tag_configure('center',justify='center', wrap='word')
    text_1.insert('1.0',questions[y])
    text_1.config(state='disabled',borderwidth=1,
                relief='solid')
    text_1.tag_add('center','1.0','end')
    text_1.place(x=0,y=0,relwidth=1,relheight=.15)
    label_2 = tk.Label(frame_7,text='A.',bg='indianred1',
                       font=('Arial','16'))
    label_2.place(rely=.25,relx=.05,relheight=.05, anchor='w')
    label_3 = tk.Label(frame_7,text='B.',bg='indianred1',
                       font=('Arial','16'))
    label_3.place(rely=.35,relx=.05,relheight=.05, anchor='w')
    label_4 = tk.Label(frame_7,text='C.',bg='indianred1',
                       font=('Arial','16'))
    label_4.place(rely=.45,relx=.05,relheight=.05, anchor='w')
    label_5 = tk.Label(frame_7,text='D.',bg='indianred1',
                       font=('Arial','16'))
    label_5.place(rely=.55,relx=.05,relheight=.05, anchor='w')
    #labels in frame 8
    text_2 = tk.Text(frame_8, borderwidth=1, relief='solid',
                      bg='deep sky blue', font=('Times New Roman', '20', 'bold'))
    text_2.tag_configure('center', justify='center', wrap='word')
    text_2.insert('1.0',questions[y])
    text_2.config(state='disabled')
    text_2.tag_add('center', '1.0', 'end')
    text_2.place(x=0,y=0,relwidth=1,relheight=.15)
    label_7 = tk.Label(frame_8,text='A.',bg='indianred1',
                       font=('Arial','16'))
    label_7.place(rely=.25,relx=.05,relheight=.05, anchor='w')
    label_8 = tk.Label(frame_8,text='B.',bg='indianred1',
                       font=('Arial','16'))
    label_8.place(rely=.35,relx=.05,relheight=.05, anchor='w')
    label_9 = tk.Label(frame_8,text='C.',bg='indianred1',
                       font=('Arial','16'))
    label_9.place(rely=.45,relx=.05,relheight=.05, anchor='w')
    label_10 = tk.Label(frame_8,text='D.',bg='indianred1',
                       font=('Arial','16'))
    label_10.place(rely=.55,relx=.05,relheight=.05, anchor='w')
    label_11 = tk.Label(frame_8,text='E.',bg='indianred1',
                       font=('Arial','16'))
    label_11.place(rely=.65,relx=.05,relheight=.05, anchor='w')


    #Buttons
    Button_1 = tk.Button(frame_7, text='Next', bg='limegreen',command = question,
                         font=('Arial','16'), width=7)
    Button_1.place(rely = .7, relx= .8)
    Button_2 = tk.Button(frame_8, text='Next', bg='limegreen',command = question,
                         font=('Arial','16'), width=7)
    Button_2.place(rely = .7, relx= .8)
    
def func_one():
    global RandomQues
    global QuizResults
    global RandomOpt
    global radioVar
    RandomQues = bool1.get()
    QuizResults = bool2.get()
    RandomOpt= bool3.get()

def doButton2():
    RandomQues = bool1.get()
    QuizResults = bool2.get()
    RandomOpt= bool3.get()
    var1 = E1.get()
    var2 = E2.get()
    global numOfQues
    global titleVar
    global QuizTimer
    if var1.isnumeric() and var2.isnumeric():
        numOfQues=int(var1)
        QuizTimer=int(var2)
        titleVar+=1
        label_1.configure(text='Customize Question #'+str(titleVar))
        if titleVar <= numOfQues: 
            frame_2.tkraise()
        if quesType == 1: 
            if (E3.get() == ''):
                tk.messagebox.showwarning(title='Input Error',
                                       message='Type in a question and/or select an answer.' )
                titleVar-=1
                frame_3.tkraise()
            elif(rVar.get() == 0):
                tk.messagebox.showwarning(title='Input Error',
                                       message='Type in a question and/or select an answer.' )
                titleVar-=1
                frame_3.tkraise()
            else: 
                questions.append(E3.get())
                print(questions)
                options.append(E4.get())
                options.append(E5.get())
                options.append(E6.get())
                options.append(E7.get())
                print('options = ', options)
                intLabel = int(rVar.get())
                qTypes.append(quesType)
                answers.append(rVar.get())
                qTypes.pop()
                
        if quesType == 2:
            if (E8.get() == ''):
                tk.messagebox.showwarning(title='Input Error',
                                       message='Type in a question and/or select an answer.' )
                titleVar-=1
                frame_4.tkraise()
            elif(myInt.get() == 0):
                tk.messagebox.showwarning(title='Input Error',
                                       message='Type in a question and/or select an answer.' )
                titleVar-=1
                frame_4.tkraise()
            else: 
                questions.append(E8.get())
                options.append(E9.get())
                options.append(E10.get())
                options.append(E11.get())
                options.append(E12.get())
                options.append(E13.get())
                print('options = ', options)                    
                intLabel = int(myInt.get())
                qTypes.append(quesType)
                answers.append(myInt.get())
                qTypes.pop()
        if quesType == 3:
            if (txtbox1.get() == ''):
                tk.messagebox.showwarning(title='Input Error',
                                       message='Type in a question and/or select an answer.' )
                titleVar-=1
                frame_5.tkraise()
            elif(mytkVar.get() == 0):
                tk.messagebox.showwarning(title='Input Error',
                                       message='Type in a question and/or select an answer.' )
                titleVar-=1
                frame_5.tkraise()
            else:
                questions.append(txtbox1.get())
                qTypes.append(quesType)
                answers.append(mytkVar.get())
                   

        if quesType == 4:
            if (txtBox1.get() == ''):
                tk.messagebox.showwarning(title='Input Error',
                                       message='Type in a question and/or select an answer.' )
                titleVar-=1
                frame_6.tkraise()
            elif(answer.get() == '' ):
                tk.messagebox.showwarning(title='Input Error',
                                       message='Type in a question and/or select an answer.' )
                titleVar-=1
                frame_6.tkraise()
            else: 
                questions.append(txtBox1.get())
                qTypes.append(quesType)
                answers.append(answer.get())
  
            print(questions)
        if titleVar > numOfQues:
            print('question types:',qTypes)
            question()

        
 
             
    else:
        tk.messagebox.showwarning(title='Input Error',
                                       message='Add a number to both text boxes.' )

    
def doButton3():
    global quesType
    global titleVar
    quesType = radioVar.get()
    if quesType == 1:
        qTypes.append(quesType)
        frame_3.tkraise()
        print(qTypes)
    elif quesType == 2:
        qTypes.append(quesType)
        frame_4.tkraise()
        print(qTypes)
    elif quesType == 3:
        qTypes.append(quesType)
        frame_5.tkraise()
    elif quesType == 4:
        qTypes.append(quesType)
        frame_6.tkraise()
    elif quesType == 0:
        tk.messagebox.showwarning(title='Input Error',
                                       message='Select one of the options.' )

#Defining Frames
frame_8r = tk.Frame(root, bg="indianred1")
frame_8r.place(x=0, y=0, relwidth=1, relheight=1)
    
frame_8 = tk.Frame(root,bg='indianred1')
frame_8.place(x=0, y=0, relwidth=1, relheight=1)

frame_7 = tk.Frame(root,bg='indianred1')
frame_7.place(x=0, y=0, relwidth=1, relheight=1)

frame_6= tk.Frame(root, bg='indianred1')
frame_6.place(x=0,y=0,relwidth=1, relheight=1)

frame_5 = tk.Frame(root, bg='indianred1')
frame_5.place(x=0, y=0, relwidth=1, relheight=1)

frame_4 = tk.Frame(root, bg="indianred1")
frame_4.place(x=0, y=0, relwidth=1, relheight=1)

frame_3 = tk.Frame(root, bg="indianred1")
frame_3.place(x=0, y=0, relwidth=1, relheight=1)

frame_2 = tk.Frame(root,bg='indianred1')
frame_2.place(x=0, y=0, relwidth=1, relheight=1)

bottom_frame = tk.Frame(root, bg="indianred1",)
bottom_frame.place(x=0, y=0, relwidth=1, relheight=1)

#Labels and entries
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



my_checkbutton_1=tk.Checkbutton(bottom_frame,text="Random Questions",var=bool1,
                                bg='indianred1', font=('Arial','12'))
my_checkbutton_2=tk.Checkbutton(bottom_frame,text="Quiz Results Page",var=bool2,
                                 bg='indianred1', font=('Arial','12'))
my_checkbutton_3=tk.Checkbutton(bottom_frame,text="Random Options",var=bool3,
                                 bg='indianred1', font=('Arial','12'))

my_checkbutton_1.place(rely=.55,relx=.08,relheight=.05, anchor='w')
my_checkbutton_2.place(rely=.60,relx=.08,relheight=.05, anchor='w')
my_checkbutton_3.place(rely=.65,relx=.08,relheight=.05, anchor='w')

B1 = tk.Button(bottom_frame,text="Select Features",font=('Arial','12'),
               command = func_one)
B1.place(rely=.72,relx=.08,relheight=.05, anchor='w')


B2 = tk.Button(bottom_frame,text="Next", bg='limegreen', width=7,
               font=('Arial','16'), command = doButton2)
B2.place(rely=.8,relx=.8,relheight=.05, anchor='w')

#Frame 2

#Text of label_1 will change
label_1 = tk.Label(frame_2,text ='Customize Question #',
                   borderwidth=1, relief= 'solid',bg='deep sky blue',
                   font=('Times New Roman', '24', 'bold'))
label_1.place(x=0,y=0,relwidth = 1, relheight = .08)
label_2 = tk.Label(frame_2,text = 'Type of Question', bg='indianred1',
                   relief='sunken', font=('Arial', '20', 'bold'))
label_2.place(rely=.125, relx=.32)
#radio buttons
radioVar = tk.IntVar()
radioVar.set(0)
radio_1 = tk.Radiobutton(frame_2)
radio_1.config(text="Multiple Choice Question (A-D)", variable=radioVar, value=1,
               bg='indianred1', font=('Arial', '16'))
radio_2 = tk.Radiobutton(frame_2)
radio_2.config(text="Multiple Choice Question (A-E)", variable=radioVar, value=2,
               bg='indianred1', font=('Arial', '16'))
radio_3 = tk.Radiobutton(frame_2)
radio_3.config(text="True or False", variable=radioVar, value=3,
               bg='indianred1', font=('Arial', '16'))
radio_4 = tk.Radiobutton(frame_2)
radio_4.config(text="Short Response", variable=radioVar, value=4,
               bg='indianred1', font=('Arial', '16'))
radio_1.place(rely = .25,relx= .25, relheight = .05, anchor = 'w')
radio_2.place(rely = .35,relx= .25, relheight = .05, anchor = 'w')
radio_3.place(rely = .45,relx= .25, relheight = .05, anchor = 'w')
radio_4.place(rely = .55,relx= .25, relheight = .05, anchor = 'w')
#Buttons
button_1 = tk.Button(frame_2, text='Next', bg='limegreen',
                     font=('Arial','16'), width=7, command=doButton3)
button_1.place(rely = .8, relx= .8)

#Frame 3 (Button will have the function doButton2)



TitleLabel = tk.Label(frame_3,text= "Create Your Own Quiz", relief='solid',
                      borderwidth = 1, bg='deep sky blue',
                      font=('Times New Roman', '24', 'bold'))
TitleLabel.place(x=0, y=0, relwidth = 1, relheight = .08)

L1 = tk.Label(frame_3, text = "Question:",height = 2, width = 10,
              bg="indianred1", font=('Arial','16'))
L1.place(rely=.11,relx=.05,relheight=.05, anchor='w')

E3 = tk.Entry(frame_3, width = 90)
E3.place(rely=.15,relx=.08,relheight=.05, anchor='w')

L2 = tk.Label(frame_3, text = "Option A:",height = 2, width = 10,
              bg="indianred1", font=('Arial','16'))
L2.place(rely=.20,relx=.05,relheight=.05, anchor='w')

L3 = tk.Label(frame_3, text = "Option B:",height = 2, width = 10,
              bg="indianred1", font=('Arial','16'))
L3.place(rely=.30,relx=.05,relheight=.05, anchor='w')

L4 = tk.Label(frame_3, text = "Option C:",height = 2, width = 10,
              bg="indianred1", font=('Arial','16'))
L4.place(rely=.40,relx=.05,relheight=.05, anchor='w')

L5 = tk.Label(frame_3, text = "Option D:",height = 2, width = 10,
              bg="indianred1", font=('Arial','16'))
L5.place(rely=.50,relx=.05,relheight=.05, anchor='w')

rVar = tk.IntVar()
rVar.set(0)


my_radiobutton_1=tk.Radiobutton(frame_3,var=rVar,value = 1,
                                bg="indianred1", font=('Arial','16'))
my_radiobutton_2=tk.Radiobutton(frame_3,var=rVar,value = 2,
                                bg="indianred1", font=('Arial','16'))
my_radiobutton_3=tk.Radiobutton(frame_3,var=rVar,value = 3,
                                bg="indianred1", font=('Arial','16'))
my_radiobutton_4=tk.Radiobutton(frame_3,var=rVar,value = 4,
                                bg="indianred1", font=('Arial','16'))



my_radiobutton_1.place(rely=.25,relx=.03,relheight=.05, anchor='w')
E4 = tk.Entry(frame_3, width = 90)
E4.place(rely=.25,relx=.08,relheight=.05, anchor='w')

my_radiobutton_2.place(rely=.35,relx=.03,relheight=.05, anchor='w')
E5 = tk.Entry(frame_3, width = 90)
E5.place(rely=.35,relx=.08,relheight=.05, anchor='w')

my_radiobutton_3.place(rely=.45,relx=.03,relheight=.05, anchor='w')
E6 = tk.Entry(frame_3, width = 90)
E6.place(rely=.45,relx=.08,relheight=.05, anchor='w')

my_radiobutton_4.place(rely=.55,relx=.03,relheight=.05, anchor='w')
E7 = tk.Entry(frame_3, width = 90)
E7.place(rely=.55,relx=.08,relheight=.05, anchor='w')

B3 = tk.Button(frame_3,text="Next", bg='limegreen', width=7,font=('Arial','16'), command = doButton2  )
B3.place(rely=.8,relx=.8, anchor='w')

# Frame 4
TitleLabel = tk.Label(frame_4,text= "Create Your Own Quiz", relief='solid',
                      borderwidth = 1, bg='deep sky blue',
                      font=('Times New Roman', '24', 'bold'))
TitleLabel.place(x=0, y=0, relwidth = 1, relheight = .08)

L1 = tk.Label(frame_4, text = "Question:",height = 2, width = 10,
              bg="indianred1", font=('Arial','16'))
L1.place(rely=.11,relx=.05,relheight=.05, anchor='w')

E8 = tk.Entry(frame_4, width = 90)
E8.place(rely=.15,relx=.08,relheight=.05, anchor='w')

L2 = tk.Label(frame_4, text = "Option A:",height = 2, width = 10,
              bg="indianred1", font=('Arial','16'))
L2.place(rely=.20,relx=.05,relheight=.05, anchor='w')

L3 = tk.Label(frame_4, text = "Option B:",height = 2, width = 10,
              bg="indianred1", font=('Arial','16'))
L3.place(rely=.30,relx=.05,relheight=.05, anchor='w')

L4 = tk.Label(frame_4, text = "Option C:",height = 2, width = 10,
              bg="indianred1", font=('Arial','16'))
L4.place(rely=.40,relx=.05,relheight=.05, anchor='w')

L5 = tk.Label(frame_4, text = "Option D:",height = 2, width = 10,
              bg="indianred1", font=('Arial','16'))
L5.place(rely=.50,relx=.05,relheight=.05, anchor='w')

L6 = tk.Label(frame_4, text = "Option E:",height = 2, width = 10,
              bg="indianred1", font=('Arial','16'))
L6.place(rely=.60,relx=.05,relheight=.05, anchor='w')

myInt = tk.IntVar()
myInt.set(0)

my_Radiobutton_1=tk.Radiobutton(frame_4,var=myInt, value=1,
                                bg="indianred1", font=('Arial','16'))
my_Radiobutton_2=tk.Radiobutton(frame_4,var=myInt, value=2,
                                bg="indianred1", font=('Arial','16'))
my_Radiobutton_3=tk.Radiobutton(frame_4,var=myInt, value=3,
                                bg="indianred1", font=('Arial','16'))
my_Radiobutton_4=tk.Radiobutton(frame_4,var=myInt, value=4,
                                bg="indianred1", font=('Arial','16'))
my_Radiobutton_5=tk.Radiobutton(frame_4,var=myInt, value=5,
                                bg="indianred1", font=('Arial','16'))


my_Radiobutton_1.place(rely=.25,relx=.03,relheight=.05, anchor='w')
E9 = tk.Entry(frame_4, width = 90)
E9.place(rely=.25,relx=.08,relheight=.05, anchor='w')

my_Radiobutton_2.place(rely=.35,relx=.03,relheight=.05, anchor='w')
E10 = tk.Entry(frame_4, width = 90)
E10.place(rely=.35,relx=.08,relheight=.05, anchor='w')

my_Radiobutton_3.place(rely=.45,relx=.03,relheight=.05, anchor='w')
E11 = tk.Entry(frame_4, width = 90)
E11.place(rely=.45,relx=.08,relheight=.05, anchor='w')

my_Radiobutton_4.place(rely=.55,relx=.03,relheight=.05, anchor='w')
E12 = tk.Entry(frame_4, width = 90)
E12.place(rely=.55,relx=.08,relheight=.05, anchor='w')

my_Radiobutton_5.place(rely=.65,relx=.03,relheight=.05, anchor='w')
E13 = tk.Entry(frame_4, width = 90)
E13.place(rely=.65,relx=.08,relheight=.05, anchor='w')

B4 = tk.Button(frame_4,text="Next", bg='limegreen', width=7,font=('Arial','16'), command = doButton2  )
B4.place(rely=.8,relx=.8, anchor='w')

# Frame 5
mytkVar = tk.IntVar()
mytkVar.set(0)


#Labels and text entries
titleLabel2 = tk.Label(frame_5,text= "Type your question in the box.", relief='solid',
                      borderwidth = 1, bg='deep sky blue', 
                      font=('Times New Roman', '24', 'bold'))
titleLabel2.place(x=0,y=0,relwidth=1,relheight=.08)

txtbox1= tk.Entry(frame_5,font=('Raleway', '12'))
txtbox1.place(relx =.05, rely=.11, relheight=.10, relwidth=.9)

ansLabel=tk.Label(frame_5,text='Choose the correct answer', relief='solid',
                  font=('Arial', '20'), bg='indianred1',borderwidth = 1)
ansLabel.place(rely=.27, relx=.08, anchor = 'w')

my_radio_1 = tk.Radiobutton(frame_5,text=("True"), variable=mytkVar,
                            value=1, font=('Arial','16'),bg='indianred1')
my_radio_1.place(rely = .35,relx= .08, relheight = .05, anchor = 'w')
my_radio_2 = tk.Radiobutton(frame_5,text="False", variable=mytkVar,
                            value=2, font=('Arial','16'),bg='indianred1')

my_radio_2.place(rely = .50,relx= .08, relheight = .05, anchor = 'w')
button_1 = tk.Button(frame_5, text='Next', bg='limegreen',
                     font=('Arial','16'), width=7, command = doButton2)
button_1.place(rely = .8, relx= .8)

# Frame 6


# Labels and text boxes
txtBox1= tk.Entry(frame_6,font=('Raleway', '12'))
txtBox1.place(relx =.05, rely=.11, relheight=.10, relwidth=.9)
Label_1 = tk.Label(frame_6,text= "Type your question in the box.", relief='solid',
                      borderwidth = 1, bg='deep sky blue', 
                      font=('Times New Roman', '24', 'bold'))
Label_1.place(x=0,y=0,relwidth=1, relheight=.08)

Label_2 = tk.Label(frame_6, text=("Type your answer here."),
                   font=('arial', 16), bg='indianred1')
Label_2.place(relx=.075,rely=.25)

answer = tk.Entry(frame_6)
answer.place(relx=.08,rely=.31)

button_2 = tk.Button(frame_6, text='Next', bg='limegreen',
                     font=('Arial','16'), width=7, command = doButton2)
button_2.place(rely = .8, relx= .8)








root.mainloop()


















