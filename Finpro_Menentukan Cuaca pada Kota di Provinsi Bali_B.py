import requests
from bs4 import BeautifulSoup as bs

daftar_kota = ['Amlapura','Bangli','Denpasar','Gianyar','Mengwi','Negara',
               'Semarapura','Singaraja','Tabanan']

print("⠂⠁⠈⠂⠄⠄⠂⠁⠁⠂⠄⠄⠂⠁⠁⠂⠂⠁⠈⠂⠄⠄⠂⠁⠁⠂⠄⠄⠂⠁⠁⠂⠂⠁⠈⠂⠄⠄⠈⠂⠄⠄⠂⠈⠂⠄⠄⠂⠈⠂⠄⠄⠂⠂")
print("|              WELCOME TO MY PROGRAM                 |")
print("|         MENENTUKAN CUACA DI PROVINSI BALI          |")
print("|                                                    |")
print("|----------------------------------------------------|")
print("|              By : Aulia Nur Fitriani               |")
print("⠂⠁⠈⠂⠄⠄⠂⠁⠁⠂⠄⠄⠂⠁⠁⠂⠂⠁⠈⠂⠄⠄⠂⠁⠁⠂⠄⠄⠂⠁⠁⠂⠂⠁⠈⠂⠄⠄⠈⠂⠄⠄⠂⠈⠂⠄⠄⠂⠈⠂⠄⠄⠂⠂")

loc = 'Provinsi Bali'
url = 'https://data.bmkg.go.id/DataMKG/MEWS/DigitalForecast/DigitalForecast-Bali.xml'

response = requests.get(url,verify=False)
r = response.text

prakiraan = {'Pagi': '' , 'Siang': '', 'Malam': ''}

kode = {
'0': 'Cerah',
'1': 'Cerah Berawan',
'2': 'Cerah Berawan',
'3': 'Berawan',
'4': 'Berawan Tebal',
'5': 'Udara Kabur',
'10': 'Asap',
'45': 'Kabut',
'60': 'Hujan Ringan',
'61': 'Hujan Sedang',
'63': 'Hujan Lebat',
'80': 'Hujan Lokal',
'95': 'Hujan Petir',
'97': 'Hujan Petir'
}

def question():
    print("\nMenu yang ingin dijalankan:\n")
    print("[1] Lihat daftar kota yang tersedia")
    print("[2] Perkiraan Cuaca")
    print("[3] Keluar program")
    
def PerkiraanCuaca():
    query = str(input("Masukkan kota di Bali \n"))
    while True:
        if query in daftar_kota:
            url = url = 'https://data.bmkg.go.id/DataMKG/MEWS/DigitalForecast/DigitalForecast-Bali.xml'
            print("\n•´¨`•.¸¸.•´¨`•.¸¸.•´¨`•.¸¸.••´¨`*•.")
            print(("☁ Hasil cuaca"))
            response = requests.get(url,verify=False) 
            r = response.text
            print("Selesai")
            break
        else:
            print("Kota tidak ditemukan,Inputkan ulang\n")
            PerkiraanCuaca()
            break
    
Amlapura = bs(r,"xml")
cuacaBali = Amlapura.find(id="501162").find(id="weather")

h0 = cuacaBali.find(h='0').value.string
h6 = cuacaBali.find(h='6').value.string
h12 = cuacaBali.find(h='12').value.string

Bangli = bs(r,"xml")
cuacaBali = Bangli.find(id="501163").find(id="weather")

h0 = cuacaBali.find(h='0').value.string
h6 = cuacaBali.find(h='6').value.string
h12 = cuacaBali.find(h='12').value.string
 
Denpasar = bs(r,"xml")
cuacaBali = Denpasar.find(id="501164").find(id="weather")

h0 = cuacaBali.find(h='0').value.string
h6 = cuacaBali.find(h='6').value.string
h12 = cuacaBali.find(h='12').value.string

Gianyar = bs(r,"xml")
cuacaBali = Gianyar.find(id="501165").find(id="weather")

h0 = cuacaBali.find(h='0').value.string
h6 = cuacaBali.find(h='6').value.string
h12 = cuacaBali.find(h='12').value.string
 
Mengwi = bs(r,"xml")
cuacaBali = Mengwi.find(id="501166").find(id="weather")

h0 = cuacaBali.find(h='0').value.string
h6 = cuacaBali.find(h='6').value.string
h12 = cuacaBali.find(h='12').value.string
    
Negara  = bs(r,"xml")
cuacaBali = Negara.find(id="501167").find(id="weather")

h0 = cuacaBali.find(h='0').value.string
h6 = cuacaBali.find(h='6').value.string
h12 = cuacaBali.find(h='12').value.string

Semarapura = bs(r,"xml")
cuacaBali = Semarapura.find(id="501168").find(id="weather")

h0 = cuacaBali.find(h='0').value.string
h6 = cuacaBali.find(h='6').value.string
h12 = cuacaBali.find(h='12').value.string

Singaraja = bs(r,"xml")
cuacaBali = Singaraja.find(id="501169").find(id="weather")

h0 = cuacaBali.find(h='0').value.string
h6 = cuacaBali.find(h='6').value.string
h12 = cuacaBali.find(h='12').value.string
    
Tabanan = bs(r,"xml")
cuacaBali = Tabanan.find(id="501170").find(id="weather")

h0 = cuacaBali.find(h='0').value.string
h6 = cuacaBali.find(h='6').value.string
h12 = cuacaBali.find(h='12').value.string

prakiraan['Pagi'] = kode[h0]
prakiraan['Siang'] = kode[h6]
prakiraan['Malam'] = kode[h12]

def alur3():
    while True:
        Exit = str(input("\nE untuk Exit\n"))
        if Exit == "E":
            alur2()
            break
        else:
            print("\nInputan tidak sesuai,gagal dijalankan")
            print("Inputkan ulang")
            alur3()
            break

def alur2():
    question()
    menu = str(input("\nMasukkan menu pilihan\n"))
    while True:
        if menu == "3":
            print("Program Berhasil")
            break
        elif menu == "1":
            print("\nKota yang tersedia")
            print(daftar_kota)
            print("\n-----------------------------")
            print("[E] Untuk Exit")
            print("-----------------------------")
            alur3()
            break
        elif menu == "2":
            PerkiraanCuaca()
            print("\n-----------------------------")
            print("[E] Untuk Exit")
            print("-----------------------------")
            alur3()
            break
        else:
            print("Inputan tidak sesuai,sistem berulang")
            alur2()
            break

alur2()

print(
    "Perkiraan Cuaca di provinsi Bali",
    "\nPagi  : ",
    prakiraan['Pagi'],
    "\nSiang : ",
    prakiraan['Siang'],
    "\nMalam : ",
    prakiraan['Malam'],
    )
