#!/bin/bash

#deklarasikan array compound assignment
distroLinuxDesktop=('BlankON' 'Ubuntu' 'Debian' 'ArchLinux' 'LinuxMint')
distroLinuxServer=('UbuntuServer' 'CentOS' 'FedoraServer')

#cara mengambil nilai array
echo ${distroLinuxDesktop[*]}
echo ${distroLinuxServer[*]}
