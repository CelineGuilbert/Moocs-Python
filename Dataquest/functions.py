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


