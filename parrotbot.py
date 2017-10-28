
from sklearn.neural_network import MLPClassifier
clsf = MLPClassifier(activation='logistic', solver='lbfgs',
                    hidden_layer_sizes=2
                    )
movies = ['iron man', 'captain america', 'ant man', 'deadpool', 'guardians of the galaxy',
         'anchorman', 'hot tub time machine', 'kung fu panda', 'home again', 'smurfs', 
         ]
age = [20, 19, 21, 25, 17,
       27, 18, 15, 35, 12
      ]
year = [2010, 2016, 2015, 2016, 2014,
        2004, 2010, 2008, 2017, 2011
       ]
year = [item-2003 for item in year]
age  = [item-11 for item in age]
marvel = [1,1,1,1,1,
          0,0,0,0,0
         ]
comedy = [0,0,0,0,0,
          1,1,0,0,0]
cartoon = [0,0,0,0,0,
           0,0,1,0,1]
romance = [0,0,0,0,0,
          0,0,0,1,0]
clsf.fit(zip(age,year,marvel,comedy,cartoon,romance),movies)
import broize
class person:
    pass
    
def parrotback(inp, previous_out):
    if inp==None and previous_out==None:
        return 'hi'#broize.broback('')
    elif previous_out=="Hi, I'm parrotbot, I'm gonna help you find a movie to watch! First, let me get to know you a little bit -- how old are you?" or previous_out=="Hey there, Parrotbot here! Let's find you a film to watch tonight First, let me get to know you a little bit -- how old are you?":
        person.age = int(inp)
        return 'Great! Now, have you seen the new Thor movie? It was great, right?'
    elif previous_out=='Great! Now, have you seen the new Thor movie? It was great, right?':
        if 'yes' in inp:
            person.marvel=1
            return 'I thought so too! Now there is a lot of movies like that out there, do you like a comedy twist in your action movies?'
        elif 'no' in inp:
            person.marvel=0
            return 'Yeah, I did not like it either. Would you rather watch a romcom?'
    elif previous_out=='I thought so too! Now there is a lot of movies like that out there, do you like a comedy twist in your action movies?':
        if 'yes' in inp:
            person.comedy=1
            person.cartoon=0.2
            person.romance=0
        else:
            person.comedy=0
            person.cartoon=0.5
            person.romance=0.5
        return 'Final question, modern movies or old classics?'
    elif previous_out=='Final question, modern movies or old classics?':
        if 'old' in inp:
            person.year=0
        else:
            person.year=17
        find_movie(person)
        return "Sounds good, how about this one?"
    elif previous_out=='Yeah, I did not like it either. Would you rather watch a romcom?':
        if 'yes' in inp:
            person.romance=1
            person.cartoon=0
            person.comedy=1
        else:
            person.romance=0
            person.comedy=0
            person.cartoon=1
        return 'Final question, modern movies or old classics?'
    elif previous_out=="Sounds good, how about this one?" and "don't" in inp:
        find_movie(person)
        return 'how about this one?'
    else:
        return broize.broback(inp)
from tkinter import *
from PIL import ImageTk, Image
import os
import subprocess
import time
import urllib

#Start with no messages
messages = []
movie_pick = ""
prev_output = None

#Initializing the root and canvas
root = Tk()
root.title('Parrotbot')
w = 1300
h = 700
img_flag = 0

canvas = Canvas(root,width=w,height=h,bg="white")
canvas.grid()

#Inputs the user response and the question asked
def get_response(string, question):
    return "hello"

#Finds a movie for the person using the neural net
def find_movie(person):
    global img_flag, movie_pick
    tup = [(person.age,person.year,person.marvel,person.comedy,person.cartoon,person.romance)]
    img_flag = 1
    movie_pick = clsf.predict(tup)[0]
    open_img(movie_pick.replace(" ", ""))
    return movie_pick

#Uses the Verizon API to find the link to the trailer
def get_url(person):
    movie_name = movie_pick # output from neural net
    url = urllib.urlopen('http://api.vidible.tv/53c2870aee1353918d33d955d7b3f19e/video/search?query='
                         +movie_name+' trailer')
    string1 = url.read()
    match_string = re.match( r'.*?"videoUrl":"(.*?)".*', string1)
    link = match_string.group(1)
    return link

#Prints the text based on a user's input
def printtext(event):
    global img_flag, e, messages, root, prev_output
    string = e.get()
    e.delete(0, 'end')
    if (string == ""):
        return
    messages = [[string, 1]] + messages
    response = parrotback(string, prev_output)
    #if (prev_output=='Final question, modern movies or old classics?'):
    #    if (img_flag):
    #        open_img(movie_pick.replace(" ", ""))
    #    return
    messages = [[response, 0]] + messages
    prev_output = response
    update_text(root, messages)
    if (img_flag):
        open_img(movie_pick.replace(" ", ""))

#Updates the GUI text boxes
def update_text(root, texts):
    for i in range(min(16, len(texts))):
        t = Text(root)
        t.place(x = w * 0.5, y = h * 0.1 * (9 - (i+1)/2.0), anchor = "c",
                height = 25, width = w * 0.7)
        if (texts[i][1] == 1):
            img = Image.open("prof_pic.png")
            img = img.resize((30, 30), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(img)
            panel = Label(root, image=img)
            panel.image = img
            panel.pack()
            t.tag_configure('tag-right', justify='right')
            t.insert('end', texts[i][0], 'tag-right')
            panel.place(x = w * 0.9, y = h * 0.1 * (9 - (i+1)/2.0), anchor = "e")
        else:
            img = Image.open("Unknown")
            img = img.resize((35, 30), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(img)
            panel = Label(root, image=img)
            panel.image = img
            panel.pack()
            t.tag_configure('tag-left', justify='left')
            t.insert('end', texts[i][0], 'tag-left')
            panel.place(x = w * 0.1, y = h * 0.1 * (9 - (i+1)/2.0), anchor = "w")
        canvas.tag_lower(t)

#Bring up trailer link when the image is clicked on
def on_click(event=None):
    global movie_pick
    subprocess.Popen(['open', get_url(movie_pick)])

#Opens the image button for the movie poster
def open_img(x):
    if (x == ""):
        return
    img = Image.open(x)
    img = img.resize((250, 250), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Label(root, image=img)
    panel.image = img

    # bind click event to image
    panel.bind('<Button-1>', on_click)
    # button with image binded to the same function 
    b = Button(root, image=img, command=on_click)
    b.pack()
    b.place(x=w * 0.5, y=h * 0.5, anchor="c")

#This doesn't work
def open_gif():
    frames = [PhotoImage(file='partyparrot.gif',format = 'gif -index %i' %(i)) for i in range(10)]

    def update(ind):
        frame = frames[ind]
        ind += 1
        label.configure(image=frame)
        root.after(100, update, ind)
    label = Label(root)
    label.pack()
    root.after(0, update, 0)

#Make text box for user input
e = Entry(root)
e.place(x = w * 0.5, y = h * 0.9, anchor = "c", width = w * 0.8)
e.focus_set()
root.bind('<Return>',printtext)
update_text(root, messages)

root.mainloop()

