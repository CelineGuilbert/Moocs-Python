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
#In our data set, some users have tagged their posts with "(Serious)" or "(serious)", including the parentheses. 
#Therefore, we should account for both square brackets and parentheses. 
#We can do this by using square bracket notation, and escaping the "[", "]", "(", and ")" characters with the backslash.
import re

serious_count = 0
for row in posts:
    if re.search("[\[\(][Ss]erious[\]\)]", row[0]) is not None:
        serious_count += 1
 

 ## 11: Combining Multiple Regular Expressions       
#To combine regular expressions, we use the "|" character. For example, "cat|dog" would match "catfish" and "hotdog",
#because both of these strings match either "cat" or "dog". Similarly, we can combine our regular expressions for the serious
#tags with the "|" operator to match all titles that either begin or end with the tag.

import re

serious_start_count = 0
serious_end_count = 0
serious_count_final = 0

for row in posts:
    if re.search("^[\[\(][Ss]erious[\]\)]", row[0]) is not None: #commence par
        serious_start_count += 1
    if re.search("[\[\(][Ss]erious[\]\)]$", row[0]) is not None: #fini par
        serious_end_count += 1
    if re.search("^[\[\(][Ss]erious[\]\)]|[\[\(][Ss]erious[\]\)]$", row[0]) is not None: #combine les deux REGEX
        serious_count_final += 1
        
##12: Using Regular Expressions To Substitute Strings     
#If we were to call re.sub("yo", "hello", "yo world"), the function will replace the "yo" in "yo world" with "hello", 
#producing the result "hello world". If it doesn't find a pattern, the re.sub() function simply returns the original string.

#Replace "[serious]", "(Serious)", and "(serious)" with "[Serious]" for all of the titles in posts.
    #You should only need to use one call to sub(), and one regex.
    #Recall that the repl argument is an ordinary string. It's not a regex, so you don't need to escape characters like "[".
    #Append each formatted row to posts_new.       

import re
posts_new = []

for row in posts:
  row[0]= re.sub("[\[\(][Ss]erious[\]\)]",'[Serious]', row[0])
  posts_new.append(row)
  
# posts= ['If The Lord of the Rings had a Scooby Doo ending, who would Sauron really be?',
#'3576',
#'1422318567.0',
#'0',
#'2690']

##13: Matching Years With Regular Expressions
#We've loaded a number of strings into the strings variable for you.
#Loop through strings and use re.search() to determine whether each string contains a year between 1000 and 2999.
#Store every string that contains a year in year_strings. The .append() function will help here.
import re

year_strings = []
for string in strings:
    if re.search("[1-2][0-9][0-9][0-9]", string) is not None:
        year_strings.append(string)
        
## ou plus court : 
import re

year_strings = []
for string in strings:
    if re.search("[1-2][0-9]{3}", string) is not None:
        year_strings.append(string)
#retourne : ['War of 1812', 'Happy New Year 2016!']        
#strings = ['War of 1812', 'There are 5280 feet to a mile', 'Happy New Year 2016!']
        
###15: Challenge: Extracting All Years   
#Finally let's extract years from a string. The re module contains a findall() function that returns a list of substrings matching 
#he regex. re.findall("[a-z]", "abc123") would return ["a", "b", "c"], because those are the substrings that match the regex.        
import re

years = re.findall("[1-2][0-9]{3}" , years_string)
# retourne : years = ['2015', '2016']
#years_string = '2015 was a good year, but 2016 will be better!'
