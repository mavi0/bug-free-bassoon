#!/bin/bash

#Check if there are already VPN hosts, if not add the comment
if grep -q  "# VPN Hosts" /etc/hosts
then 
    echo "OK"
else
    echo "Inserting [#VPN Hosts] to /etc/hosts"
    echo "# VPN Hosts" >> /etc/hosts
fi

# Get source IP/Host maps
echo -e "\e[33mGetting Data.... \e[39m"
sudo docker exec -it $1 sh -c "cat tmp/openvpn-status.log" > vpn_data
cat vpn_data
# Parse the maps
echo -e "\e[33mParsing maps \e[39m"
python3 parse.py 
cat hosts

# Remove any existing maps
VPN_HOSTS="$(grep -n '# VPN Hosts' /etc/hosts | cut -d : -f 1)"
sed -i "${VPN_HOSTS}"q /etc/hosts

# Insert maps
echo -e "\e[33mInserting maps\e[39m"
cat hosts >> /etc/hosts
cat /etc/hosts
