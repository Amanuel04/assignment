houses = ['a','e','c','g','f','b','d']
question = input("What is your question: ").lower()
if question.find("between") != -1 and question.find("how") == -1:
    x = question.find("and")
    first_house = x-2
    second_house = x+4
    y = houses.index(question[first_house])
    z = houses.index(question[second_house])
    if y < z:
        answer = houses[y+1:z]
        print("The house between "+ question[first_house]+" and "+question[second_house]+" is")
        for i in answer:
            print(i)
    elif y > z:
        answer = houses[z+1:y]
        print("The house between " + question[first_house] + " and " + question[second_house] + " is")
        for i in answer:
            print(i)

elif question.find("neighbor") != -1 or question.find("besides") != -1:
    if question.find("neighbor") ==-1 and question.find("besides")!= -1:
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


        print(answer,"lives besides "+question[x+8])

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
            print(answer,"is the neighbor of "+question[x+3])
        else:
            print(answer, "are the neighbor of " + question[x + 3])


elif question.find("middle") != -1:
    x = len(houses)-1
    print("The middle house is "+ houses[int(x/2)])
elif question.find("how") != -1 and question.find("between") != -1:
    x = question.find("and")
    first_house = x-2
    second_house = x+4
    y = houses.index(question[first_house])
    z = houses.index(question[second_house])
    answer = houses[y+1:z]
    print("There are "+str(len(answer))+" houses between "+question[first_house]+" and "+ question[second_house])

elif question.find("corner") != -1:
    if question.find("first corner") != -1:
        print("The first corner house is "+ houses[0])
    elif question.find("second corner"):
        print("The second corner house is "+ houses[len(houses)-1])


input("")
