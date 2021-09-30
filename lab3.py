#Programmers: Peter & Victoria
#Course: CS151, Dr. Rajeev
#Date: 9/30/21
#Lab Number: 3
#Program Inputs: Weight of package, distance shipped
#Program Outputs: charge for shipping

import math
#ask for inputs of weight and distance and cast them to floats
weight = float(input("Input the weight of your package in kg: "))
distance = float(input("Input the distance it is being shipped in miles: "))

#check if weight is within shipping limits
if (weight>0 and weight<=20):
    #check if distance is within shipping limits
    if (distance>=10 and distance <= 3000):
        #find charge if weight is greater than 0kg and not heavier than 2kg
        if (weight>0 and weight<=2):
            charge = distance/500*1.10
            print(math.ceil(charge))
            #find charge if weight is greater than 2kg and not heavier than 6kg
        if (weight>2 and weight<=6):
            charge = distance/500*2.20
            print(math.ceil(charge))
            #find charge if weight is greater than 6kg and not heavier than 10kg
        if (weight>6 and weight<=10):
            charge = distance/500*3.70
            print(math.ceil(charge))
            #find charge if weight is greater than 10kg
        if (weight>10):
            charge = distance/500*4.80
            print(math.ceil(charge))
    #print statment if the distance is invalid
    else:
        print ("invalid distance, please run again")
#print statement if the weight is invalid
else:
    print("invalid weight, please run again")