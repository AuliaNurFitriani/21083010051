#!/bin/bash

# deklarasikan array [Explicit DEclaration] :
declare -a angka

#clear
i=0;
while [ $i -le 4 ];
do
	let isi=$i*2;
	angka[$i]=$isi;
	let i=$i+1;
done

#tambpilkan semua elemen array
#dengan indexnya berisi "*" ATAU "@"
echo ${angka[@]}

