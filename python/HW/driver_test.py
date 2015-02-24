#########################
# Danny Schick
# CS 21A
# Driver's Liscence
#########################

def main():
    infile = open('student_solution.txt','r')
    answernum = 0 # defining variables
    answers = []
    correct = ['a','c','a','a','d','b','c','a','c','b','a','d','c','a','d','c','b','b','d','a'] # list of correct answers
    right = 0
    wrong = 0
    wrongNum = [] # list for the number of wrong answers
    for i in infile:
        i = i.rstrip("\n") # reformating string
        i = i.lstrip(" ")
        answers.append(i)
        if i == correct[answernum]:
            right += 1
        else:
            wrong += 1
            question = answernum + 1
            wrongNum.append(question)
        answernum += 1
    if right >= 15:
        print("You Pass!")
    else:
        print("You Fail...")
    print("Number of correct answers: ", right, "\nNumber of wrong answers: ", wrong, "List of all wrong questions: \n", wrongNum)

main()


