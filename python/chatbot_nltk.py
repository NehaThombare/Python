from tkinter import *

from nltk.chat.util import Chat, reflections
root = Tk()
root.title("Chatbot")
def send():
    send = "You -> "+e.get()
    txt.insert(END, "\n"+send)
    user = e.get().lower()
    if(user == "hello good morning"):
        txt.insert(END, "\n" + "Bot -> Hii\n")
    elif(user == "hi" or user == "hii" or user == "hiiii"):
        txt.insert(END, "\n" + "Bot -> Hello\n")
    elif(user == "i am neha, and you are?"):
        txt.insert(END, "\n" + "Bot -> heyy i am harry.\n")
    elif(user == "how are you?"):
        txt.insert(END, "\n" + "Bot -> fine! and you\n")
    elif(user == "fine" or user == "i am good" or user == "i am doing good"):
        txt.insert(END, "\n" + "Bot -> Great! how can I help you.\n")
    elif(user == "how's the weather today?"):
        txt.insert(END, "\n" + "Bot -> it's quite rainy outside...\n")
    elif(user=="okk thanks!"):
        txt.insert(END, "\n"+"Bot-> No problem.Do you need anything else?")
    elif(user == "no thanks"):
        txt.insert(END, "\n" + "Bot -> okayy byee!!.\n")
    else:
        txt.insert(END, "\nn" + "Bot -> Sorry! I dind't get you\n")
    e.delete(0, END)
txt = Text(root)
txt.grid(row=0, column=0, columnspan=3)
e = Entry(root, width=100)
e.grid(row=1, column=0)
send = Button(root, text="Send", command=send).grid(row=1, column=1)
root.mainloop()


reflections = {
  "i am"       : "you are",
  "i was"      : "you were",
  "i"          : "you",
  "i'm"        : "you are",
  "i'd"        : "you would",
  "i've"       : "you have",
  "i'll"       : "you will",
  "my"         : "your",
  "you are"    : "I am",
  "you were"   : "I was",
  "you've"     : "I have",
  "you'll"     : "I will",
  "your"       : "my",
  "yours"      : "mine",
  "you"        : "me",
  "me"         : "you"
}






pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today ?",]
    ],
    
    [
        r"what is your name ?",
        ["I am a bot created by Neha. you can call me harry!",]
    ],
    [
        r"how are you ?",
        ["I'm doing good and what about You ?",]
    ],
    [
        r"sorry (.*)",
        ["Its alright","Its OK, never mind",]
    ],
    [
        r"I am fine",
        ["Great to hear that, How can I help you?",]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that","How can I help you?:)",]
    ],
   
    [
        r"how is weather in (.*)?",
        ["Weather in %1 is awesome like always","Too hot man here in %1","Too cold man here in %1","Never even heard about %1"]
    ],
   
    
    
    
    
    [
        r"quit",
        ["BBye take care. See you soon :) ","It was nice talking to you. See you soon :)"]
    ],
]



def chat():
    print("Hi! I am a chatbot created by Dipti Kodre  for your service")
    chat = Chat(pairs,reflections)
    chat.converse()
#initiate the conversation
if __name__ == "_main_":
    chat()