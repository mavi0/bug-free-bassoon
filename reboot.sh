#!/bin/bash

#Check if there are already VPN hosts, if not add the comment
if grep -q  "# VPN Hosts" /etc/hosts
then 
    # Remove any existing maps
    echo "Removing hosts"
    VPN_HOSTS="$(grep -n '# VPN Hosts' /etc/hosts | cut -d : -f 1)"
    sed -i "${VPN_HOSTS}"q /etc/hosts

else
    echo "Inserting [#VPN Hosts] to /etc/hosts"
    echo "# VPN Hosts" >> /etc/hosts
fi


