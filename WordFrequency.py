import random

#takes a string and removes all punctuation and numbers then returns a list of each individual word
#in all lowercase letters
def create_list(txt):
    #split the txt into a list of words
    words = txt.split(' ')
    #list of each individual word
    new_list = []
    for word in words:
        #make each word lowercase
        word = word.lower()
        #checks for endline, tab, and dash characters
        #will replace the characters with a space then split the words into two
        #the words will be separately added to the end of the list and the program
        #will skip to the next iteration
        if "\n" in word:
            word = word.replace("\n", " ")
            two_words = word.split(' ')
            #makes sure two_words is a list of two words
            if len(two_words) == 2:
                #add the words to the end of the list and skip to next iteration
                words.append(two_words[0])
                words.append(two_words[1])
            continue
        if "\t" in word:
            word = word.replace("\t", " ")
            two_words = word.split(' ')
            if len(two_words) == 2:
                words.append(two_words[0])
                words.append(two_words[1])
            continue
        if "-" in word:
            word = word.replace("-", " ")
            two_words = word.split(' ')
            if len(two_words) == 2:
                words.append(two_words[0])
                words.append(two_words[1])
            continue

        #removes all possible punctation and numbers
        punctuation_nums = "1234567890`~!@#$%^&*()-_=+[{]}\|;:'\",<.>/?"
        for char in word:
            if char in punctuation_nums:
                word = word.replace(char, "")

        #appends the list of indiviual words
        new_list.append(word)

    return new_list
    

#returns a dictionary of each individual word of a book as the key and the
#frequency of that words occurence as the value
def word_freq_dict(txt):
    words = create_list(txt)
    new_dict = {}
    #adds one to the value of the word
    for word in words:
        if word in new_dict:
            new_dict[word] += 1
        else:
            new_dict[word] = 1
    return new_dict

#returns a list of 100 random unique words from a given txt
def random_words(txt):
    words = create_list(txt)
    #makes a set so no words will be repeated
    unique_words = set(words)
    #uses the random function to create a random list of 100 words
    rand = random.sample(unique_words, 100)
    return rand
    
def random_dict(sample_txt):
    #read the books and create a dictionary
    txt = read_book("frankenstein.txt")
    frank_dict = word_freq_dict(txt)
    txt = read_book("WarOfTheWorlds.txt")
    war_dict = word_freq_dict(txt)
    txt = read_book("TheMurderOnTheLinks.txt")
    murder_dict = word_freq_dict(txt)
    rand_set = random_words(sample_txt)
    new_dict = {}
    #creates a dictionary storing a random word as the key and a list of that
    #words occurence in each book as the value
    for word in rand_set:
        #if the word is not present set the value to 0 for that book
        if word in frank_dict:
            frank_num = frank_dict[word]
        else:
            frank_num = 0
        if word in war_dict:
            war_num = war_dict[word]
        else:
            war_num = 0
        if word in murder_dict:    
            murder_num = murder_dict[word]
        else:
            murder_num = 0
        #add the key and list value for each random word
        new_dict[word] = [frank_num, war_num, murder_num]
    return new_dict

#returns a string read from a txt file
def read_book(name):
    try:
        with open(name, encoding="latin-1") as book:
            text = book.read()
    except Exception as inst:
        print("Error", inst, "opening/reading the book", name)
    finally:
        return text

#read the book and test the functions
txt = read_book("frankenstein.txt")
my_dict = random_dict(txt)
print(my_dict)

