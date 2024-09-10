print ("(1)First free service \n(2)Second free service")

number = int(input("Enter the free service number>> "))
miles = int(input("Enter number of miles>> "))

if number == 1:
    if 1500 < miles <= 3000 :
        print ("Vehicle must be serviced")
    elif 0 <= miles <= 1500  :
        print ("Vehicle not must be serviced")
elif number == 2:
    if 3001 < miles <= 4500 :
        print ("Vehicle must be serviced")
    elif miles < 3000 :
        print ("Vehicle not must be serviced")
else:
    print("Invalid service number.")
    