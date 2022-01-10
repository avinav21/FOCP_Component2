MPH=[]#lsit to hold values in mile per hour 

print("Swallow Speed Analysis: Version 1.0\n")

while True:
    user_input=input("Enter the speed:")
    if user_input=="":#if the user input is empty it will stop prompting the user  
        break

    if user_input[0].lower()!="u" and user_input[0].lower()!="e":#checking if the user has entered the value starting with u or e 
        print("Invalid input")
        continue

    elif len(user_input)==1:#checking if the the user has only entered unit of the speed
        print("Invalid input")
        continue

    elif user_input[1:].isnumeric()==False:#check if the value entered is neumeric type 
        print("Invalid input")
        continue

    speed=float(user_input[1:])#seperates the value and turn it into a float data 

    if user_input[0].lower()=="u":# checks if the value is in miles 
        MPH.append(speed)

    else:
        speed*=0.621371#cnverting km to miles
        MPH.append(speed)

    print("Reading saved.")

if MPH!=[]:#check if the MPH list is not empty
    maximum=max(MPH)#max value in list holding speed in miles 
    minimum=min(MPH)#min value in list holding speed in miles 
    average=sum(MPH)/len(MPH)#average value in list holding speed in miles 
    print("\nResults Summary\n")
    print("{} Readings Analysed.\n".format(len(MPH)))
    print("Max Speed:{:.2f}MPH,{:.2f}KPH".format(maximum,maximum*1.60934))
    print("Min Speed:{:.2f}MPH,{:.2f}KPH".format(minimum,minimum*1.60934))
    print("Avg Speed:{:.2f}MPH,{:.2f}KPH".format(average,average*1.60934))

else:
    print("No readings entered. Nothing to do.") 
        
    