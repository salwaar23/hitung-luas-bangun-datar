print ("Nama  : Salwaa Roudlootul Jannah Rabbani \nNIM   : 41037006211189 \nKelas : A3")
print ("-------------------------------------")
print ("Program Menghitung Luas Bangun Datar")
print ("-------------------------------------")
print ("1. Luas Persegi panjang \n2. Luas Segitiga \n3. Luas Lingkaran")
pilih = int (input("Pilih luas yang akan dihitung : "))
print ("-------------------------------------")

if pilih == 1 :
  print ("Menghitung Luas Persegi Panjang")
  panjang = int (input("\nInput Panjang (dalam cm): "))
  lebar = int (input("Input Lebar (dalam cm) : "))
  luas = panjang * lebar
  print ("Luas Persegi Panjang adalah : ",luas, 'cm')
elif pilih == 2:
  print ("Menghitung Luas Segitiga")
  alas = int (input("\nInput alas (dalam cm): "))
  tinggi = int (input("Input tinggi (dalam cm) : "))
  luas = (alas * tinggi)/2
  print ("Luas Segitiga adalah : ",luas, 'cm')
elif pilih == 3:
  print ("Menghitung Luas Lingkaran")
  phi = 3.14
  jari = int (input("\nInput jari-jari (dalam cm): "))
  luas = (phi * jari * jari)
  print ("Luas Segitiga adalah : ",luas, 'cm')
else :
  print ("Nomor tidak valid")