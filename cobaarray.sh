#!/bin/bash

# deklarasi array
distroLinux=("Mint" "Ubuntu" "Kali" "Arch" "Debian")

# randoo distro
let pilih=$RANDOM%5

# eksekusi
echo "Saya Memilih Distro $pilih, ${distroLinux[$pilih]} !"
