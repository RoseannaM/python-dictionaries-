# put your code here.

# Write a program, wordcount.py, that opens a file and counts how many times each 
# space-separated word occurs in that file. Your program should then print 
# those counts to the screen.

# We’ve included a small file, test.txt, that you can use for testing 
#out your script. The file contains this poem:

def count_words(filename):
    """Prints a list of the words in a text with how many times they appear"""

    #open file
    the_text = open(filename)

    # split text based on spaces (will generate a list)
    words_in_text = []

    for line in the_text:
        words_in_text.extend(line.rstrip().split(" "))

    # initiate empty dictionary

    # iterate over list, see if in dictionary, if not initiate with count of zero
    # increment by one

    # print all words with counts in dictionary

    #close file
    the_text.close()
