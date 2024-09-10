Pembeli = input("Apakah anda seorang mahasiswa \nJika anda mahasiswa tulis 'IYA' : ")
jumlah_uang = float(input ("Masukkan pembelian anda : "))

percentage_discount = 20/100
sales_tax_percentage = 5/100
 
if Pembeli.upper() == "IYA" : 
    discount = jumlah_uang * percentage_discount
    Discounted_total = jumlah_uang - discount
    tax = Discounted_total * sales_tax_percentage
    total = Discounted_total + tax
    
    
    print (f"Total purchases: ${jumlah_uang:,.2f}")
    print (f"Student discount(20%) :$ {Discounted_total:,.2f}")
    print (f"Discounted total :$ {Discounted_total:,.2f}")
    print (f"Sales tax (5%):$ {tax:,.2f}")
    print (f"Total : $ {total:,.2f}")
else:
    tax = jumlah_uang * sales_tax_percentage
    total = jumlah_uang + tax
    
    print (f"Total purchases: $ {jumlah_uang:,.2f}")
    print (f"sales tax (5%) :$ {tax:,.2f}")
    print (f"Total :$ {total:,.2f}")