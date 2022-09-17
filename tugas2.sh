echo "===Operasi Aritmatika==="

echo "1. penjumlahan"
echo "2. pengurangan"
echo "3. perkalian"
echo "4. pembagian"
read -p "pilih operasi: " pilih
echo "masukkan x: "
read X
echo "masukkan y: "
read Y
case $pilih  in
1)
	menu="penjumlahan"
	hasil=$((X+Y))
;;
2) 
	menu="pengurangan"
	hasil=$((X-Y))
;;
3)
	menu="perkalian"
	hasil=$((X*Y))
;;
4)
	menu="pembagian"
	hasil=$((X/Y))
;;
esac
echo "hasil dari operasi $menu : $hasil"
echo "Selesai Be happy"

sleep 1
#bertanya
echo "it is really fu,right? (yes/no)"
read tanya
if [ $tanya == "yes" ]
then
   echo "see you again ^^"
elif [ $tanya == "no" ]
then
   echo "don't give up :)"
else
   echo "aku bingung :("
fi


