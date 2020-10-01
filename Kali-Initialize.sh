#!/usr/bin/bash

atom () {
  echo "[+] Installing Atom"
  wget -qO - https://packagecloud.io/AtomEditor/atom/gpgkey | sudo apt-key add -
  sudo sh -c 'echo "deb [arch=amd64] https://packagecloud.io/AtomEditor/atom/any/ any main" > /etc/apt/sources.list.d/atom.list'
  sudo apt-get update
  sudo apt-get install atom
  echo "[!] Atom Install Complete"
  wait 1
  }

terminator () {
  echo "[+] Installing Terminator"
  sudo apt install terminator
  echo "[!] Terminator Install Complete"
  }

OpSTools () {
  echo "[+] Installing Open-Source Tools"
  mkdir ~/Tools
  cd ~/Tools
  sudo git clone https://github.com/rebootuser/LinEnum
  sudo git clone https://github.com/SecureAuthCorp/impacket.git
  sudo git clone https://github.com/diego-treitos/linux-smart-enumeration.git
  sudo git clone https://github.com/carlospolop/privilege-escalation-awesome-scripts-suite.git
  sudo git clone https://github.com/luke-goddard/enumy.git
  sudo git clone https://github.com/rasta-mouse/Watson.git
  sudo git clone https://github.com/GhostPack/Seatbelt.git
  sudo git clone https://github.com/gentilkiwi/mimikatz.git
  sudo git clone https://github.com/411Hall/JAWS.git
  sudo git clone https://github.com/M4ximuss/Powerless.git
  echo "[!] Open-Source Tools Install Complete"
  }
