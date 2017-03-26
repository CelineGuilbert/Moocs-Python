##2: Wildcards In Regular Expressions
#we use the special character "." to indicate that any character can be put in its place
strings = ["bat", "robotics", "megabyte"]
regex = ""
regex = "b.t"

##3: Searching The Beginnings And Endings Of Strings
#We can use the caret symbol ("^") to match the beginning of a string, 
#and the dollar sign ("$") to match the end of a string.

strings = ["better not put too much", "butter in the", "batter"]
bad_string = "We also wouldn't want it to be bitter"
regex = "^b.tter"

##4: Introduction To The AskReddit Data Set
#Reddit is a content and community website where users can submit links, text posts, and other types of content to groups of people with
#similar interests. 
#These groups are called subreddits, and each one specializes in a particular topic.
#For example, AskReddit is a popular subreddit where you can pose questions to the entire Reddit community.
#Users answer the questions by commenting on them.

##5: Reading And Printing The Data Set
import csv
f= open('askreddit_2015.csv','r')
csvreader = csv.reader(f)
posts_with_header = list(csvreader)

posts=posts_with_header[1:] #exclude the first row
for post in posts:
    print(post[0:10])

##6: Counting Simple Matches In The Data Set With Re()
#With re.search(regex, string), we can check whether string is a match for regex. 
#If it is, the expression will return a match object. If it isn't, it will return None

if re.search("needle", "haystack") is not None:
    print("We found it!")
else:
    print("Not a match")
#The code above will print Not a match, because "haystack" is not a match for the regex "needle".

##exercice
import re

of_reddit_count = 0
for row in posts:
    if re.search("of Reddit", row[0]) is not None:
        of_reddit_count += 1
        
##7: Using Square Brackets To Match Multiple Characters
#For example, the regex "[bcr]at" would match the substrings "bat", "cat", and "rat", but nothing else
import re

of_reddit_count = 0
for row in posts:
    if re.search("of [Rr]eddit", row[0]) is not None:
        of_reddit_count += 1

##8: Escaping Special Characters
#Our data set contains a lot of posts that use the [Serious] tag
#We'd like to search through our data set to see how many posts have this tag, but the regex "[Serious]" doesn't do what we need.
#To deal with this sort of problem, we need to escape special characters. In regular expressions, escaping a character means indicating
#that you don't want the character to do anything special, and that the interpreter should treat it just like any other character. 
#We use the backslash ("\") to escape characters in a regex.

import re

serious_count = 0
for post in posts:
    if re.search("\[Serious\]",post[0]) is not None:
        serious_count += 1
        
#Some people tag serious posts as "[Serious]", and others as "[serious]"
import re

serious_count = 0
for row in posts:
    if re.search("\[[sS]erious\]", row[0]) is not None:
        serious_count += 1
        
        
## 10: Adding More Complexity To Your Regular Expression
