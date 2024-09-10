n = int(input("Monster mengatakan angka apa : ")) # masukkan angka

if 2 <= n <=1000 : #rentang batas
    for i in range (2, n) : # memeriksa setiap angka i dari 2 hingga n-1. apakah ada angka selain 1 dan n yang dapat membagi n tanpa sisa.
        if n % i == 0:   #memeriksa apakah n dapat dibagi habis oleh i
            print ("INI BUKAN BILANGAN PRIMA") 
        break    #break menghentikan eksekusi loop, sehingga tidak perlu memeriksa angka-angka berikutnya.
    else :
        print ("INI BILANGAN PRIMA")
else:
    print ("INI BUKAN BILANGAN PRIMA")
        