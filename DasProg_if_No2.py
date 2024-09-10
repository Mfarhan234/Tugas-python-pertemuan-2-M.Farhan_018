berat_badan = float(input("Berapa berat badan anda dalam pound : "))
tinggi = float(input("berapa Tinggi badan anda dalam satuan inchi : "))

BMI = (703*berat_badan) / (tinggi**2)

if BMI < 18.5 :
    print ("Underweight")
elif 18.5 <= BMI <= 24.9 :
    print ("Normal")
elif 25.0 <= BMI <= 29.9 :
    print ("Overweight")
elif BMI >= 30.0 :
    print ("Obese")
