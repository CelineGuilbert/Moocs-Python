##an application program interface (API)
#An API is a set of methods and tools that allows different applications to interact with each other. 
#Programmers use APIs to query and retrieve data dynamically (which they can then integrate with their own apps). 
#A client can retrieve information quickly and effectively through an API.


#In this mission, we'll query a basic API to retrieve data about the International Space Station (ISS).
#Using an API will save us time and effort, instead of doing all the computation ourselves.


##TO RETRIEVE DATA USE OPEN NOTIFY; GET request to retrieve information from the OpenNotify API.
#http://open-notify.org/Open-Notify-API/


#The most common is a GET request, which we use to retrieve data

#The first endpoint we'll look at on OpenNotify is the iss-now.json endpoint. 
#This endpoint gets the current latitude and longitude position of the ISS.
# A data set wouldn't be a great fit for this task because the information changes often, and involves some calculation on the server.

# Make a get request to get the latest position of the ISS from the OpenNotify API.

#We can use a simple GET request to retrieve information from the OpenNotify API.
response = requests.get("http://api.open-notify.org/iss-now.json")
status_code = response.status_code


##The request we just made returned a status code of 200. Web servers return status codes every time they receive an API request.
# A status code provides information about what happened with a request. Here are some codes that are relevant to GET requests:

#200 - Everything went okay, and the server returned a result (if any).
#301 - The server is redirecting you to a different endpoint. This can happen when a company switches domain names, or an endpoint's name has changed.
#401 - The server thinks you're not authenticated. This happens when you don't send the right credentials to access an API (we'll talk about this in a later mission).
#400 - The server thinks you made a bad request. This can happen when you don't send the information the API requires to process your request, among other things.
#403 - The resource you're trying to access is forbidden; you don't have the right permissions to see it.
#404 - The server didn't find the resource you tried to access.


# Enter your answer below.
response = requests.get("http://api.open-notify.org/iss-pass.json")
status_code = response.status_code
#You'll see that in the last example, we got a 400 status code, which indicates a bad request. 
#If you look at the documentation for the OpenNotify API, we see that the ISS Pass endpoint requires two parameters.

#To accomplish this, we can add an optional keyword argument, params, to our request. In this case, we need to pass in two parameters:
  #lat - The latitude of the location
  #lon - The longitude of the location

#We can make a dictionary that contains these parameters, and then pass them into the function.
#We can also do the same thing directly by adding the query parameters to the url, like this:
   #http://api.open-notify.org/iss-pass.json?lat=40.71&lon=-74
#It's almost always preferable to set up the parameters as a dictionary, because the requests library we mentioned earlier takes care 
#of certain issues, like properly formatting the query parameters.


response = requests.get("http://api.open-notify.org/iss-pass.json?lat=37.78&lon=-122.41")
print(response.content)

#You may have noticed that the content of the API response we received earlier was a string. 
#Strings are the way we pass information back and forth through APIs, but it's hard to get the information we want out of them. 

#there's a format we call JSON.This format encodes data structures like lists and dictionaries as strings to ensure that machines can
#read them easily. JSON is the primary format for sending and receiving data through APIs.

#Python offers great support for JSON through its json library. We can convert lists and dictionaries to JSON, and vice versa. 
#Our ISS Pass data, for example, is a dictionary encoded as a string in JSON format.

#The JSON library has two main methods:

  #dumps -- Takes in a Python object, and converts it to a string
  #loads -- Takes a JSON string, and converts it to a Python object

# Import the JSON library.
import json

# Make a list of fast food chains.
best_food_chains = ["Taco Bell", "Shake Shack", "Chipotle"]
print(type(best_food_chains))
# Use json.dumps to convert best_food_chains to a string.
best_food_chains_string = json.dumps(best_food_chains)
print(type(best_food_chains_string))

# Convert best_food_chains_string back to a list.
print(type(json.loads(best_food_chains_string)))

# Make the same request we did two screens ago.
parameters = {"lat": 37.78, "lon": -122.41}
response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)

# Get the response data as a Python object.  Verify that it's a dictionary.
json_data = response.json()
print(type(json_data))
print(json_data)
first_pass_duration = json_data["response"][0]["duration"]




