x = input ("berapa jarak lompatan maksimal B, jarak A ke Bee, Bee-C, C-D, D-E : ")

n, A_Bee, Bee_C, C_D, D_E = map(int, x .split())

if A_Bee <= n and Bee_C <= n and C_D <= n and D_E <= n :
    print ("YA..Dia bisa")
else:
    print ("TIDAK..Dia tidak bisa")