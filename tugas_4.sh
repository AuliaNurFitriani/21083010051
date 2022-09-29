#!bin/bash

echo "input bil:"
read inp

echo "maka, kelipatan  bil.ganjil positifnya yaitu"
for ((bil=inp; bil>0; bil=bil-2))
do
   echo $bil
done
