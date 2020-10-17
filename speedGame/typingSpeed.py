import random

def sliderText():
    global count,slidertext
    text = 'Start Playing'

    if(count>=len(text)):
        count=0
        slidertext=''

    slidertext += text[count]
    count += 1
    fontlabel.configure(text=slidertext)
    fontlabel.after(100,sliderText)

def setWord(event):

    global score,miss
    if(time==60):
         times()
    gameDetailsLabel.configure(text='')
    if(entrybox.get()==wordlabel['text']):
        print('Matched')
        score +=1
        scorelableCount.configure(text=score)
    else:
        print('Not Matched')
        miss +=1

    random.shuffle(word)
    wordlabel.configure(text=word[0])
     #print(entrybox.get())
    entrybox.delete(0,END)

def times():
    global time,score,miss
    if(time<11):
        timelableCount.configure(fg='red')

    if(time>0):
        time -= 1
        timelableCount.configure(text=time)
        timelableCount.after(1000,times)
    else:
        gameDetailsLabel.configure(text='Hit={} | Miss={} | Total Score={}'.format(score,miss,score-miss))
        message = messagebox.askretrycancel('Notification','Retry Again')
        if(message==True):
            score=0
            time=60
            miss=0
            timelableCount.configure(text=time)
            wordlabel.configure(word[0])
            scorelableCount.configure(text=score)





#####################################################################Game Start

from tkinter import *
from tkinter import messagebox

box = Tk()
box.geometry('800x600+400+100')
box.configure(bg='powder blue')
box.title('TypingSpeed')
box.iconbitmap('cali.ico')

######################################################################Variables
score=0
time=60
count=0
slidertext=''
miss=0
word=['Shaping','Research','Irritating','Humble','Polite','Good','Aggresive','Repulsive','Arrogante','Homofile','Astrology',
      'Astronomy','Science','SpaceX','Apple','History','Freedom','Budget','Income','Savings','Tax','Learning','Digest','Compound','Compulsive',
      'Assault','Awel','Pyche','Cabinet','Cheeze','Blossom','Concure','Peter','Musk','Ellen','Jobs','Steve','Pichi','Sunder','Nadella']

########################################################################Labels

fontlabel= Label(box,text='',font=('arial',30,'italic bold'),bg='powder blue',fg='black',width=10)
fontlabel.place(x=250,y=10)
sliderText()

random.shuffle(word)
wordlabel = Label(box,text=word[0],font=('arial',20,'italic bold'),bg='powder blue')
wordlabel.place(x=350,y=200)

scorelable =Label(box,text='Score',font=('arial',20,'italic bold'),bg='powder blue',bd=5)
scorelable.place(x=100,y=100)

scorelableCount =Label(box,text=score,font=('arial',20,'italic bold'),bg='powder blue',fg='blue')
scorelableCount.place(x=110,y=150)

timelable =Label(box,text='Timer',font=('arial',20,'italic bold'),bg='powder blue',bd=5)
timelable.place(x=600,y=100)

timelableCount =Label(box,text=time,font=('arial',20,'italic bold'),bg='powder blue',fg='blue')
timelableCount.place(x=610,y=150)

gameDetailsLabel=Label(box,text='Enter and Hit',font=('arial',20,'italic bold'),bg='powder blue',fg='grey')
gameDetailsLabel.place(x=300,y=370)


###########################################################################################Textarea
entrybox = Entry(box,font=('arial',20,'italic bold'),bg='white',bd=10,justify='center')
entrybox.place(x=280,y=300)
entrybox.focus_set()

entrybox.bind('<Return>',setWord)

box.mainloop();