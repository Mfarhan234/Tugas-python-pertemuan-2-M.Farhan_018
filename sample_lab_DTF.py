x = input ("Masukkan Waktu Siaran anda ' HH:MM:SS' GMT+2 : ")
y = input ("Masukkan Waktu anda sekarang ' CH:CM:CS ' GMT+7 :  ")

HH, MM, SS = map(int, x.split(":"))
CH, CM, CS = map(int, y.split(":"))

HH += 5
if HH >= 24 :
    HH -= 24 #menyesuaikan agara jika lebih dari 24 dapat kembali ke 
    
waktu_siaran = HH * 3600 + MM * 60 + SS # hitungan waktu siaran
waktu_saat_ini = CH * 3600 + CM * 60 + CS #hitungan waktu saat ini
selisih_waktu = waktu_siaran - waktu_saat_ini #selisih waktu

if selisih_waktu >= 0 :
        jam = selisih_waktu // 3600
        menit = (selisih_waktu % 3600) // 60 
        detik = selisih_waktu % 60
        print(f"streaming yang akan datang kurang dari {jam}:{menit}:{detik}")
elif -10800 < selisih_waktu < 0 :
        print ("Sampai jumpa di siaran acara berikutnya") 
else: 
        jam = selisih_waktu // 3600
        menit = (selisih_waktu % 3600) // 60 
        detik = selisih_waktu % 60
        print(f"streaming yang akan datang kurang dari {jam}:{menit}:{detik}")
        
