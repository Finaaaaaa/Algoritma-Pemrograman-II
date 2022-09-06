def penjumlahan(angka1, angka2): #mendefinisikan fungsi penjumlahan dengan parameter angka1 dan angka2
    jumlah = angka1 + angka2 #menjumlahkan angka1 dan angka2
    return jumlah #mengembalikan nilai jumlah

def pengurangan(angka1, angka2): #mendefinisikan fungsi pengurangan dengan parameter angka1 dan angka2
    selisih = angka1 - angka2 #mengurangkan angka1 dan angka2
    return selisih #mengembalikan nilai selisih

def perkalian(angka1, angka2): #mendefinisikan fungsi perkalian dengan parameter angka1 dan angka2
    kali = angka1 * angka2 #mengalikan angka1 dan angka2
    return kali #mengembalikan nilai kali

def pembagian(angka1, angka2): #mendefinisikan fungsi pembagian dengan parameter angka1 dan angka2
    bagi = angka1 / angka2 #membagi angka1 dan angka2
    return bagi #mengembalikan nilai bagi

def kalkulator(): #mendefinisikan fungsi
    operasi = input("1. Penjumlahan(+) \n2. Pengurangan(-) \n3. Perkalian(*) \n4. Pembagian(/) \nPilih operasi matematika yang diinginkan: ")
    #menginput operasi matematika yang diinginkan
    while True: #perulangan while selama nilai yang diinputkan benar
        if operasi == "1" or operasi == "+" or operasi == "2" or operasi == "-" or operasi == "3" or operasi == "*" or operasi == "4" or operasi == "/":
            angka1 = float(input("Masukkan angka pertama: ")) #menginput angka1
            angka2 = float(input("Masukkan angka kedua: ")) #menginput angka2
            if operasi == "1" or operasi == "+": #jika user memilih penjumlahan
                print(angka1, "+", angka2, "=" , penjumlahan(angka1, angka2)) #menampilkan hasil penjumlahan
            elif operasi == "2" or operasi == "-": #jika user memilih penguranga
                print(angka1, "-", angka2, "=" , pengurangan(angka1, angka2)) #menampilkan hasil pengurangan
            elif operasi == "3" or operasi == "*": #jika user memilih perkalian
                print(angka1, "*", angka2, "=" , perkalian(angka1, angka2)) #menampilkan hasil perkalian
            elif operasi == "4" or operasi == "/": #jika user memilih pembagian
                print(angka1, "/", angka2, "=" , pembagian(angka1, angka2)) #menampilkan hasil pembagian
        else: #jika memilih selain operasi yang tersedia
            print("Error") 
            print("operasi matematika yang dimasukkan kurang tepat")
            operasi = input("Pilih operasi matematika yang diinginkan: ")
            #menginput kembali operator hingga sesuai dengan operator yang tersedia

            continue #mengulang perulangan
        break #menghentikan perulangan
kalkulator() #memanggil fungsi