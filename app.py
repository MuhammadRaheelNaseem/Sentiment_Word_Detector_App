# First install library tkinter like this pip3 install tkinter
# Then install 2nd library vadersentiment like pip3 install vaderSentiment
# Then import one by one
from tkinter import *
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

gui = Tk()

gui.title("App")
gui.minsize(310,380)
gui.maxsize(310,380)
gui.configure(bg='#00003c')
gui.geometry('310x380')

#____________Main_Function_for_Analyse____________
def detectSentiment():
    sentence=entry.get()
    
    text.delete(0.0,END)
    
    sid_obj=SentimentIntensityAnalyzer()
    
    sentiment_dict=sid_obj.polarity_scores(sentence)
    
    negative_string=str(sentiment_dict['neg']*100)+'% Negative'
    
    text.insert(END,negative_string+'\n')
    
    neutral_string=str(sentiment_dict['neu']*100)+"% Neutral"
    text.insert(END,neutral_string+'\n')
    
    positive_string=str(sentiment_dict['pos']*100)+"% Positive"
    text.insert(END,positive_string+'\n')
    
    if sentiment_dict['compound'] >=0.05:
        strint='Positive'
        
    elif sentiment_dict['compound'] <= - 0.05:
        string='Negative'
        
    else:
        string="Neutral"
        text.insert(END,"Overall Result : "+string)


#____________End_Of_The_Function__________________

#______heading______
heading=Label(gui,
             text='Sentiment Detector App',
             font='Times 15 bold',
             bg='#00003c',
             fg='white')
heading.place(x=50,
             y=15)
#______Entry_Box________
entry=Entry(gui,
            width=20,
            font='arial 14'
           )
entry.place(x=5,
            y=60)
#______Button______
btn=Button(gui,
           text='Analyse',
           bg='#201d2e',
           width=6,
           fg='white',
           font='arial 10',
           command=detectSentiment
          )
btn.place(x=235,
          y=60
         )
#_______Frame_______
frame=Frame(gui,
            bd=2,
            relief=RIDGE,
            bg='#201d23'
            )
frame.place(x=5,
            y=100,
            height=250,
            width=300
           )
#_______FRAME.Label____
label=Label(frame,
            text='Result',
            bg='#201d2e',
            fg='white',
            font='arial 12 bold',
            )
label.place(x=10,
            y=5
           )
#________FRAME.Text_Box___
text=Text(frame,
         bd=2,
         relief=SUNKEN,
         font='calibri 12 bold'
         )
text.place(x=5,
          y=30,
          width=285,
          height=150)
#______FRAME.Title_____
title_label=Label(frame,
                 text="mraheel.naseem@gmail.com",
                 font='arial 12 bold',
                 fg='#ffffff',
                 bg='#201d2e')
title_label.place(x=35,
                  y=185)
title_label2=Label(frame,
                 text="github.com/muhammadraheelnaseem",
                 font='arial 11 bold',
                 fg='#ffffff',
                 bg='#201d2e')
title_label2.place(x=15,
                  y=215)
#______Close_GUI____
gui.mainloop()
