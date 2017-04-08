##BASH
#shell variables
FOOD="montexte"
echo $FOOD

#we've been creating shell variables We can only access these variables within the Bash shell.
#Another type of variable is an environment variable. We can access these through any program we run from the shell.
#We can create environment variables using the export command

#On the last screen, we typed /usr/bin/python to access the Python interpreter. 
#If the Python interpreter is at that location, though, how come we can also access it by typing python?

echo \$PATH

ls -al --ignore=ipyhton




##2: Use Python

touch script.py
nano script.py
--------
if __name__ == "__main__":
    print("Welcome to a Python script")
--------   
python script.py #by default version 2    
#type for v3 :  python3 script.py



##3: Installing Packages That Extend Python

#pip install requests to install the requests package.
pip install requests

##4: Overview Of Virtual Environments
#On the previous screen, we used the default version of pip to install requests for the python executable, which is Python version 2.
#Type virtualenv python2 in the /home/dq directory to create a new virtual environmented named python2.
virtualenv python2

#we can type virtualenv -p /usr/bin/python3 python3 to use Python 3 instead of Python 2.
#In order to do this, we pass the -p flag to the virtualenv command, which will allow us to change the Python interpreter that virtualenv 
#uses.
virtualenv -p /usr/bin/python3 python3

##6: Activating A Virtualenv
source python3/bin/activate


##7: Verifying The Installed Packages

#Type python -V to verify that Python 3 is the current Python version after activating the virtualenv.
#Renvoie la version de python
#Type pip freeze to check which packages are installed, and their versions.


##8: Importing Saved Functions Into A File
#If there's a file named utils.py, we can import it into another file in the same directory using import utils. 
#All of the functions and classes defined in utils.py will then be available using dot notation.

#Create a file called utils.py that contains the following code:
def print_message():
    print("Hello from another file!")
#Modify the original script.py file to contain this code instead:
import utils

if __name__ == "__main__":
    utils.print_message()
#lacer la commande : 
python script.py    


##9: Accessing Command Line Arguments







    

    
