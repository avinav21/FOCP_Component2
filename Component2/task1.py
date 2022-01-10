
print("Stop! Who would cross the Bridge of Death \nMust answer me these questions three, 'ere the other side he see.")

name = input("What is your name?\n")

if name=="":#check if the name is empty 
    print("Name not entered.")
    print("You may not pass")

elif "arthur" not in name.lower():#check if the users name is arthur 
    quest = input("What is your quest?\n")
    
    if "grail" in quest.lower():#check if the user seeks grail 
        colour=input("What is your favourite colour?\n")

        if colour=="":#check if the name is empty 
            print("favourite colour not entered")

        elif name[0].lower()==colour[0].lower():#check if the first letter of name is same as first letter of colour  
            print("you may pass")
        else:
            print("Incorrect! You must now face the Gorge of Eternal Peril.")

    else:      
        print("Only those who seek the Grail may pass.")  

else:
    print("My liege! You may pass!")

