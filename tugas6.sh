#!/bin/bash

declare -a nilai;

echo 
echo -n " batas nilai yang dimasukkan : "; read ipk

total=0;
ipkMhs=0;

echo
echo " ======================== ";

for ((i=1; i<=ipk; i++))
do
	echo
	echo -n " masukkan nilai IPS ke $i : "; read nilai[$i];
	let total=$total+${nilai[i]};
	let ipkMhs=$total/$ipk;
done

echo 
echo " ++++++++================+++++++++++++========+++++++ "
echo
echo " nilai IPS mahasiswa  selama 3 semester : "
echo
echo " >> ${nilai[@]} << ";
echo 
echo "Nilai IPS: " $total/$ipk;
echo
echo "Nilai IPK:  $ipkMhs ";
