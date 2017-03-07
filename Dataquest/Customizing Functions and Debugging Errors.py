#improve our spell checker 'voir feuille functions.py

#Recall that our spell checker works by:
#Reading in a file of correctly spelled words, tokenizing it into a list, and assigning it to the variable vocabulary
#Reading in, cleaning, and tokenizing the text we want to spell check
#Comparing each word (token) in the text with each word in vocabulary, and returning the ones it doesn't find


f = open("story.txt", 'r')
story_string = f.read()
vocabulary = open("dictionary.txt", "r").read()

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


# using Clean
def tokenize(text_string, special_characters, clean=False):
    # If `clean` is `True`.
    if clean:
        cleaned_story = clean_text(text_string, special_characters)
        story_tokens = cleaned_story.split(" ")
        return(story_tokens)
    # If `clean` not equal to `True`, no cleaning.
    story_tokens = text_string.split(" ")
    return(story_tokens)

clean_chars = [",", ".", "'", ";", "\n"]
tokenized_story = tokenize(story_string, clean_chars, True)
tokenized_vocabulary = tokenize(vocabulary, clean_chars)

for ts in tokenized_story:
    if ts not in tokenized_vocabulary:
        misspelled_words.append(ts)
        
## using Clean en parametre
def tokenize(text_string, special_characters, clean=False):
    if clean:
        cleaned_story = clean_text(text_string, special_characters)
        story_tokens = cleaned_story.split(" ")
        return(story_tokens)
    story_tokens = text_string.split(" ")
    return(story_tokens)
    
clean_chars = [",", ".", "'", ";", "\n"]
tokenized_story = tokenize(story_string,clean_chars,True)
tokenized_vocabulary = tokenize(vocabulary,clean_chars)
               
for ts in tokenized_vocabulary:
    if ts not in tokenized_vocabulary:
        misspelled_words.append(ts)
