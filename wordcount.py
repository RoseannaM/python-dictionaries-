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

    # initiate empty dictionary
    word_count_dict = {}

    for line in the_text:
        words_in_text.extend(line.rstrip().split(" "))
   
    # iterate over list, see if in dictionary, if not initiate with count of zero
    # increment by one
    for word in words_in_text:
        word_count_dict[word] = word_count_dict.get(word, 0) + 1

    # print all words with counts in dictionary
    for key, value in word_count_dict.items():
        print(f"{key} {value}")
    
    #close file
    the_text.close()
