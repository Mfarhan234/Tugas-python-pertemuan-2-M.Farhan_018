huruf = input("Masukkan Sebuah huruf: ")

if huruf.upper() == "O" :
    cylinder_color = "Orange"
    countents = "Ammonia"
    print ("you have a",cylinder_color, "gas cylinder and it countents ", countents)
elif huruf.upper() == "B" :
    cylinder_color = "Brown"
    countents = "Carbon Monocide"
    print ("you have a",cylinder_color, "gas cylinder and it countents", countents)
elif huruf.upper() == "Y" :
    cylinder_color = "Yellow"
    countents = "Hydrogen"
    print ("you have a",cylinder_color, "gas cylinder and it countents", countents)
elif huruf.upper() == "G" :
    cylinder_color = "Green"
    countents = "Oxygen"
    print ("you have a",cylinder_color, "gas cylinder and it countents", countents)
else :
    print("Contents unknow")
    
    