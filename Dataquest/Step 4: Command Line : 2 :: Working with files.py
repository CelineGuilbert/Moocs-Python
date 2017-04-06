##: Making A File
https://en.wikipedia.org/wiki/Touch_(Unix)

#First, we need to create a file. While there are several ways to do this, we'll start with the touch command. 
#This command will create an empty file with the name we give it. For example, typing touch file.txt will create a new file 
#called file.txt in the current directory
touch file.txt

##2: Understanding Standard Streams
#stdout, stderr, and stdin exist because these standard streams allow the interfaces to be abstract
echo "All bears should juggle"


##3: Redirecting Standard Streams
#To redirect, we use the greater than sign (>). 
#For example, echo "Dataquest is awesome" > dataquest.txt will write Dataquest is awesome to stdout, then redirect stdout to the file 
#dataquest.txt. 
echo "Dataquest is awesome" > dataquest.txt


##4: Editing A File
#To run nano, type nano, followed by the name of the file you want to edit. 
#For example, nano test.txt will open the test.txt file for editing.
nano test.txt

#Once a file is open, we can make whatever changes we want, then hit ctrl+x to quit. 
#When we quit, the terminal will prompt us to save our work. Typing Y (for yes), then pressing Enter will save all changes.


##5: Overview Of File Permissions

## Permissions have 3 Scopes:
##owner - The user who created the file or folder
##group - Users in the owner's group (on Unix systems, an owner can place users in groups)
##everyone - All other users on the system who aren't the user or in the user's group

#Each scope can have any of three permissions (a scope can have multiple permissions at once):

##read - The ability to see what's in a file (if defined on a folder, the ability to see what files are in a folder)
##write - The ability to modify a file (if a folder, the ability to delete, modify, and rename files in the folder)
##execute - The ability to run a file (some files are executable, and need this permission to run)


#In the example above, the permissions for the file test.txt are -rw-r--r--. There are 10 characters in that string.
#Type ls -l to see the file permissions in the /home/dq directory.


##6: Octal Notation For File Permissions

--- : No permissions; corresponds to 0
--x : Execute only permission; corresponds to 1
-w- : Write only permissions; corresponds to 2
-wx : Write and execute permissions; corresponds to 3
r-- : Read only permissions; corresponds to 4
r-x : Read and execute permissions; corresponds to 5
rw- : Read and write permissions; corresponds to 6
rwx : Read, write, and execute permissions; corresponds to 7


#We can use this system to convert the permissions string -rw-r--r-- to 0644
#We can pull up a file's octal permissions with the stat command.
#Typing stat test.txt will show us some information about the file test.txt, including the octal permissions.


##7: Modifying File Permissions
#Now that we understand file permissions, we can modify them using the chmod command. 
#f we pass in an octal permissions string and a file name, the command will modify the file to assign it the permissions we specifie
#in the string.
Typing chmod 0664 test.txt


##8: Moving Files (Déplacer)
#We can move files with the mv command. Typing mv test.txt /dq will move the test.txt file to the /dq folder

/home/dq$ mkdir test    
/home/dq/test$ mv test.txt test

##9: Copying Files
#cp test.txt test2.txt will copy the test.txt file, and create a new file called test2.txt containing the contents of test.txt


##10: Overview Of File Extensions
#For example, mv test.txt test2.txt will move the file test.txt to test2.txt. This will basically rename test.txt.
mv test.txt test_no_extension  

##11: Deleting A File
#We can delete a file with the rm command. Typing rm test.txt will remove the test.txt file, for example,
#provided that it's in the current directory.
rm test2.txt

##12: Bypassing Permissions As The Root User
#For example, typing sudo rm test.txt will switch to the root user, then delete the test.txt file as the root user. 





