x = input ("Berapa jumlah mobil didepan , jumlah mobil dibelakang , jumlah detik yang anda inginkan \n'Tuliskan, contoh 11 11 11' :\n")

M,N,T = map(int, x.split())

berhenti = 25
hijau = 60
interval_mobil = 5

if 1<= M and N <=1000 and 1 <= T <= 10000 :
    siklus_lampu = berhenti + hijau
    mobil_per_siklus = hijau // interval_mobil
    siklus_penuh = T // siklus_lampu      # Jumlah siklus penuh dalam waktu T detik
    sisa_waktu = T % siklus_lampu    # Sisa waktu setelah siklus penuh
    mobil_dalam_sisa_waktu = sisa_waktu // interval_mobil     # Jumlah mobil yang dapat melintas dalam sisa waktu
    mobil_dapat_melintas = siklus_penuh * mobil_per_siklus + min(mobil_dalam_sisa_waktu, M + N +1)    # Total mobil yang dapat melintas dalam waktu T detik
    total_mobil = M + N +1     # Jumlah total mobil
    mobil_tidak_dapat_melintas = max(0, total_mobil - mobil_dapat_melintas) # Menghitung jumlah mobil yang tidak dapat melintas
    if mobil_tidak_dapat_melintas == 0 : # Mencetak hasil
        print("Yes !", mobil_tidak_dapat_melintas)
    elif mobil_tidak_dapat_melintas > 0 :
        print("No!", mobil_tidak_dapat_melintas)        
else:
    print ("invalid")