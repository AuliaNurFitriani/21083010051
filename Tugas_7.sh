#!/bin/bash

echo "===Luas Persegi Panjang==="


persegi_panjang() {

	panjang=$p
	lebar=$l
	echo "$panjang"
	echo "$lebar"
}

echo "Masukkan Panjang : "
read panjang
echo "Masukkan Lebar : "
read lebar
let pp=$panjang*$lebar
echo "Jadi, Luas Persegi Panjang adalah  $pp"

printf "\n"
persegi_panjang $panjang $lebar 	

