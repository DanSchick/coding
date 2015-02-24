#####################################
# Danny Schick
# CS 21A
# Grades HW
#####################################
def letterGrade(percent): # determine letter form
    if percent >= 90:
        return 'A'
    elif percent >= 80:
        return 'B'
    elif percent >= 70:
        return 'C'
    elif percent >= 60:
        return 'D'
    elif percent <= 60 and percent >= 0:
        return 'F'
    else:
        print("Invalid percent")

def gradeHist(letter, times): # given a letter grade and frequency, reformat to be written to file
    letter = "\n" + letter + ": " # format letter for later added *s
    for i in range(1, times+1):
        letter += "*"
    return letter

def main():
    grades = open('grades.dat', 'r')
    gradesOut = open('grades_out.dat', 'w')
    letters = []
    for line in grades: # write all grades in letter form
        line = float(line)
        grade = letterGrade(line) + "\n" # determine grade and add newline
        letters.append(grade.rstrip("\n")) # collect all letters with no newline for histogram later
        gradesOut.write(grade) # write to file
    (a, b, c, d, f) = 0, 0, 0, 0, 0
    for i in letters: # determine how many letter grades
        if i == 'A':
            a += 1
        elif i == 'B':
            b += 1
        elif i == 'C':
            c += 1
        elif i == 'D':
            d += 1
        elif i == 'F':
            f += 1
    ########## WRITING HISTOGRAM #############
    gradesOut.write(gradeHist('A', a))
    gradesOut.write(gradeHist('B', b))
    gradesOut.write(gradeHist('C', c))
    gradesOut.write(gradeHist('D', d))
    gradesOut.write(gradeHist('F', f))


main()



