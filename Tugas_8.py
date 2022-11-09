from time import time, sleep
from os import getpid
from multiprocessing import cpu_count, Pool, Process

print("input nilai :")
nilai = int(input())

def cetak(i):
	for i in range(nilai):
		if i % 2 == 0:
		   print(f"{i+1} Angka Ganjil","- ID proses", getpid())
		else:
		   print(f"{i+1} Angka Genap","- ID proses", getpid())
	sleep(1)
print(" ")

# multiprocessing sekuensial
print("Multi_Sekuen")
sekuensial_awal = time()

for i in range(1):
	cetak(i)
sekuensial_akhir = time()
print(" ")

# multiprocessing process
print("Multi_Process")
kumpulan_proses = []
process_awal = time()

for i in range(1):
	p = Process(target = cetak, args = (i,))
	kumpulan_proses.append(p)
	p.start()

for i in kumpulan_proses:
	p.join()
process_akhir = time()
print(" ")

# multiprocessing pool
print("Multi_Pool")
pool_awal = time()
pool = Pool()
pool.map(cetak, range(0,1))
pool.close()
pool_akhir = time()
print(" ")

# membandingkan waktu eksekusi
print("waktu eksekusi Sekuensial  :", sekuensial_akhir - sekuensial_awal, "detik")
print("waktu eksekusi Multiprocessing.Process :", process_akhir - process_awal, "detik")
print("waktu eksekusi Multiprocessing.Pool :", pool_akhir - pool_awal, "detik")



