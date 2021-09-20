from tkinter import *

houses = ['a','e','c','g','f','b','d']

def answer_question():
    a = quest.get()
    question = a.lower()
    if question.find("between") != -1 and question.find("how") == -1:
        x = question.find("and")
        first_house = x-2
        second_house = x+4
        y = houses.index(question[first_house])
        z = houses.index(question[second_house])

        if y < z:
            answer = houses[y+1:z]
            output.configure(text="The house between {0} and {1} is ".format(question[first_house],question[second_house]))
            
            for item in answer:
                listbox.insert(END, item) 
        elif y > z:
            answer = houses[z+1:y]
            output.configure(text="The house between {0} and {1} is {2}.".format(question[first_house],question[second_house],str(answer)))

            for item in answer:
                listbox.insert(END, item)
                
    elif question.find("neighbor") != -1 or question.find("besides") != -1:
        if question.find("neighbor") ==-1 and question.find("besides") != -1:
            x = question.find("besides")
            y = houses.index(question[x+8])
            answer = []
            if y-1 < 0 and y+1 < len(houses):
                answer.append(houses[y+1])
            elif y-1 >= 0 and y+1 < len(houses):
                answer.append(houses[y-1])
                answer.append(houses[y+1])
            elif y-1 >= 0 and y+1 >= len(houses):
                answer.append(houses[y-1])


            output.configure(text="{0} lives besides {1}.".format(answer[0],question[x+8]))

        elif question.find("neighbor") != -1 and question.find("besides") == -1:
            x = question.find("of")
            y = houses.index(question[x+3])
            answer = []
            if y - 1 < 0 and y + 1 < len(houses):
                answer.append(houses[y + 1])
            elif y - 1 >= 0 and y + 1 < len(houses):
                answer.append(houses[y - 1])
                answer.append(houses[y + 1])
            elif y - 1 >= 0 and y + 1 >= len(houses):
                answer.append(houses[y - 1])


            if len(answer) == 1:
                output.configure(text="{0} is the neighbor of {1}.".format(answer[0],question[x+3]))
            else:
                output.configure(text="{0} and {1} are the neighbor of {2}.".format(answer[0],answer[1], question[x + 3]))


    elif question.find("middle") != -1:
        x = len(houses)-1
        output.configure(text="The middle house is {}".format(houses[int(x/2)]))

    elif question.find("how") != -1 and question.find("between") != -1:
        x = question.find("and")
        first_house = x-2
        second_house = x+4
        y = houses.index(question[first_house])
        z = houses.index(question[second_house])
        answer = houses[y+1:z]
        output.configure("There are {0} houses between {1} and {2}.".format(str(len(answer)),question[first_house], question[second_house]))

    elif question.find("corner") != -1:
        if question.find("first corner") != -1:
            output.configure(text="The first corner house is {}.".format(houses[0]))
        elif question.find("second corner"):
            output.configure(text="The second corner house is {}.".format(houses[len(houses)-1]))



root = Tk()

root.title("Finding House")

introduction1 = Label(text="There are 7 houses.",font=("Verdana",16))
introduction1.grid(row=0, column=0)

introduction2 = Label(text="A B C D E F G",font=("Verdana",16))
introduction2.grid(row=1, column=0)

introduction3 = Label(text="These houses are neighbours. They are arranged in random.",font=("Verdana",16))
introduction3.grid(row=2, column=0)

introduction4 = Label(text="You can ask questions like between, neighbour, corner and between. What is your question ",font=("Verdana",16))
introduction4.grid(row=3, column=0)

quest = Entry(width=75)
quest.insert(0,"Write your question")
quest.grid(row=4,column=0)

but = Button(text="Evaluate", font=("Verdana",16), command=answer_question)
but.grid(row=5,column=0)

output = Label(font=("Bauhaus 93", 16), fg='green')
output.grid(row=6, column =0)

listbox = Listbox(font=("Bauhaus 93", 16), fg='green')
listbox.grid(row=7, column=0,sticky="nwes")


mainloop()
