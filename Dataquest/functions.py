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
