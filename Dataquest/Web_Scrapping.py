# Write your code here.
response = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
content = response.content
##retourne: 
#b'<!DOCTYPE html>\n<html>\n    <head>\n        <title>A simple example page</title>\n    </head>\n    <body>\n        
#<p>Here is some simple content for this page.</p>\n    </body>\n</html>'


#We'll use the BeautifulSoup library to parse the Web page with Python. This library allows us to extract tags from an HTML document.

from bs4 import BeautifulSoup

# Initialize the parser, and pass in the content we grabbed earlier.
parser = BeautifulSoup(content, 'html.parser')

# Get the body tag from the document.
# Since we passed in the top level of the document to the parser, we need to pick a branch off of the root.
# With BeautifulSoup, we can access branches by using tag types as attributes.
body = parser.body

# Get the p tag from the body.
p = body.p

# Print the text inside the p tag.
# Text is a property that gets the inside text of a tag.
print(p.text)

#Get the text inside the title tag, and assign the result to title_text.
head = parser.head
title = head.title
title_text = title.text

##4: Using Find All
#This method will find all occurrences of a tag in the current element, and return a list.

parser = BeautifulSoup(content, 'html.parser')

# Get a list of all occurrences of the body tag in the element.
body = parser.find_all("body")

# Get the paragraph tag.
p = body[0].find_all("p")

# Get the text.
print(p[0].text)

head = parser.find_all('head')
title = head[0].find_all('title')
title_text = title[0].text

##This method will find all occurrences of a tag in the current element, and return a list.

##5: Element IDs
# Get the page content and set up a new parser.
response = requests.get("http://dataquestio.github.io/web-scraping-pages/simple_ids.html")
content = response.content
parser = BeautifulSoup(content, 'html.parser')

# Pass in the ID attribute to only get the element with that specific ID.
second_paragraph = parser.find_all("p", id="second")[0]
second_paragraph_text = second_paragraph.text



##6: Element Classes




