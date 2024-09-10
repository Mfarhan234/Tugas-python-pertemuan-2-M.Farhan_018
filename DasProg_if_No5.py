n = float(input("Berapa penggunaan data anda dalam GBs: "))

if 0 < n <= 1.0:
    charge = 250
    print (f"biaya yang harus anda bayar adalah {charge:,.2f}")
elif 1.0 < n <= 2.0 :
    charge = 500
    print (f"biaya yang harus anda bayar adalah {charge:,.2f}")
elif 2.0 < n <= 5.0:
    charge = 1000
    print (f"biaya yang harus anda bayar adalah {charge:,.2f}")
elif 5.0 < n <= 10.0:
    charge = 1500
    print (f"biaya yang harus anda bayar adalah {charge:,.2f}")
elif n >10.0:
    charge = 2000
    print (f"biaya yang harus anda bayar adalah {charge:,.2f}")
else :
    print ("Data Anda Invalid")