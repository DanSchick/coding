##############
# Danny Schick
# CS 21
# sets.py
#############

def main():
    # Getting filenames
    file1 = input("Enter the filename of file 1 (in example.txt format): ")
    file2 = input("Enter the filename of file 2 (in example.txt format): ")
    try:
        file1 = open(file1, 'r')
        file2 = open(file2, 'r')
    except FileNotFoundError:
        print("Invalid filename. Enter again.")
        main()
    file1Words = set(file1.read().lower().split()) # populate set with all words in file, lowercase
    file2Words = set(file2.read().lower().split())
    allWords = file1Words.union(file2Words) # set with ALL words

    sharedWords = file1Words.intersection(file2Words) # find shared words
    f1unique = file1Words.symmetric_difference(file2Words) # find unique words in each file
    f2unique = file2Words.symmetric_difference(file1Words)
    allUnique = f1unique.union(f2unique) # all unique words

    ##### PRINTING DATA #######
    print("ALL UNIQUE WORDS: \n", allWords)
    print("\nWORDS THAT APPEAR IN BOTH FILES: \n", sharedWords)
    print("\nWORDS IN ONLY FIRST FILE: \n", f1unique)
    print("\nWORDS IN ONLY SECOND FILE: \n", f2unique)
    print("\nWORDS UNIQUE TO ONE FILE: \n", allUnique)


main()
