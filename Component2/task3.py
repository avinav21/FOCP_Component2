from random import choice

def rand_str(lst):
    """
        A function to choose a random sring from a list of string.
        Params:
            lst: list of sting       
        Return:
            String 
    """
    return(choice(lst))

def isemail(email,domain):
    """
        A function to check if an email is valid or not.
        Params:
            email: email to be checked
            domain: valid domain for the email 
        
        Return:
            Boolean 
    """
    if email.count("@")!=1: # is this the correct way for checking for emails? this would consider a@b@c.com to be an email
        print("Invalid email")
        return False
    
    if len(email.split("@")[0])<2:
        print("Invalid email")
        return False

    if email.split("@")[1]!=domain:
        print("Invalid email")
        return False
    
    return True

def getname(email):
    """
        A function to get a name from an email.
        Parameter:
            email: email from which name should be extracted 
        Return:
            String
    """
    name= email.split("@")[0]
    return name


def inword(sent,word):
    """
        A function to check if a string is substring of another or not.
        Params:
            sent: string to be checked
            word: substring to be searched for within the string sent
        Return:
            boolean
    """
    if word.lower() in sent.lower():
        return True

    else:
        return False

names=["Alice","Bob","George"] # possible names of the chat bot
network=[True,False,False,False,False,False,False,False,False,False] # why not rand int between 0 and 1?
words=["bye","exit"] 
options={        
    "library":"The library is closed today.",
    "WiFi":"WiFi is excellent across the campus.",
    "deadline":"Your deadline has been extended by two working days.",
    "teacher":"The teacher will be there soon.",
    "classes":"There will be no further classes today.",
    "lab":"The lab is closed today."
    }#A dictionary of all the possible keywords and its reply
no_understand=["sorry","I didn't understand"]
 
print("Welcome to Pop Chat \nOne of our operators will be pleased to help you today.\n")

email=input("Please enter your Poppleton email address:")

if isemail(email,"pop.ac.uk"):
    print(f"Hi, {getname(email)}! Thank you, and Welcome to PopChat!")
    print(f"My name is {rand_str(names)}, and it will be my pleasure to help you.")

    while True:
        flag=True # what is this flag for?
        sent=input("Enter string:")

        if rand_str(network):
            print("Network error")
            break

        if any(word in sent.lower() for word in words):#if any word in list of words is in sentence then the code is terminated                                        
            break # terminate the program if the user enters bye or exit

        for items,values in options.items():#unpacking dictionary                                                   
            if inword(sent,items):
                print(values)
                flag=False

        if flag:
            print(rand_str(no_understand)) # default response if the bot does not have predefined response

