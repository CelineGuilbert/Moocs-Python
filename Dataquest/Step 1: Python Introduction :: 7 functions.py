# Read the file dictionary.txt into a string variable named vocabulary.

vocabulary = pd.read_csv("dictionary.txt", delim_whitespace= False )
print(vocabulary)

#Tokenizing The Vocabulary

#Use the string method split() to split vocabulary on the whitespace character (' ').
#Assign the resulting list to tokenized_vocabulary.
#Display the first five elements in tokenized_vocabulary.

vocabulary = open("dictionary.txt", "r").read()
tokenized_vocabulary = str.split(vocabulary)
tokenized_vocabulary[0:4]

#Replacing special characters

f = open("story.txt", 'r')
story_string = f.read()

print(story_string)
story_string = story_string.replace(".","")

#utilisation du lower()

def clean_text(text_string):
    cleaned_string = text_string.replace(",","")
    cleaned_string = cleaned_string.replace(".","")
    cleaned_string = cleaned_string.replace("'", "")
    cleaned_string = cleaned_string.replace(";", "")
    cleaned_string = cleaned_string.replace("\n", "")
    cleaned_string = cleaned_string.lower()
    return(cleaned_string)
cleaned_story = clean_text(story_string)

# en utilisant une boucle :

#Modify the clean_text() function below in the following ways:
#Add another argument called special_characters.
#Modify the function body so that it loops over all special_characters that are punctuation marks, and removes each one:
#Assign the input variable text_string to cleaned_string.
#Write a for loop that:
#Iterates over the input variable special_characters.
#Uses replace() to remove all of the instances of the current special character in cleaned_string.
#Outside the loop, use lower() to make all the text in cleaned_string lowercase, and then return it.
#Once you've written the function, run clean_text():
#Pass in story_string as the first argument.
#Pass in clean_chars as the second argument.
#Assign the result to cleaned_story.
#Print cleaned_story.

f = open("story.txt", 'r')
story_string = f.read()
clean_chars = [",", ".", "'", ";", "\n"]

def clean_text(text_string, special_characters):
    cleaned_string = text_string
    for string in special_characters:
        cleaned_string = cleaned_string.replace(string, "")
    cleaned_string = cleaned_string.lower()
    return(cleaned_string)

cleaned_story = clean_text(story_string, clean_chars)
print(cleaned_story)


#let's tokenize it from a string into a list
#A whitespace character (\" \") separates each word in cleaned_story. 
#We can use the string method split() to split cleaned_story on a single whitespace character and return a list of tokens.
#The tokenize() function focuses on converting a string to a list of tokens.
#The clean_text() function focuses on cleaning a string.


def clean_text(text_string, special_characters):
    cleaned_string = text_string
    for string in special_characters:
        cleaned_string = cleaned_string.replace(string, "")
    cleaned_string = cleaned_string.lower()
    return(cleaned_string)

clean_chars = [",", ".", "'", ";", "\n"]
cleaned_story = clean_text(story_string, clean_chars)
def tokenize(text_string, special_characters):
    cleaned_story = clean_text(text_string, special_characters)
    story_tokens = cleaned_story.split(" ")
    return(story_tokens)

tokenized_story = tokenize(story_string, clean_chars)
print(tokenized_story[0:10])




#Finding Misspelled Words
#Create an empty list named misspelled_words.
#Write a for loop that:
#Iterates over tokenized_story.
#Uses an if statement that evaluates whether the current token is in tokenized_vocabulary and if it isn't, appends the current token to misspelled_words.
#Print misspelled_words.

def clean_text(text_string, special_characters):
    cleaned_string = text_string
    for string in special_characters:
        cleaned_string = cleaned_string.replace(string, "")
    cleaned_string = cleaned_string.lower()
    return(cleaned_string)

def tokenize(text_string, special_characters):
    cleaned_story = clean_text(text_string, special_characters)
    story_tokens = cleaned_story.split(" ")
    return(story_tokens)

misspelled_words = []
clean_chars = [",", ".", "'", ";", "\n"]
tokenized_story = tokenize(story_string, clean_chars)
tokenized_vocabulary = tokenize(vocabulary, clean_chars)
for ts in tokenized_story:
    if ts not in tokenized_vocabulary:
        misspelled_words.append(ts)
print(misspelled_words)
print(misspelled_words)



