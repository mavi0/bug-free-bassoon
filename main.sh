sudo docker exec -it $1 sh -c "cat tmp/openvpn-status.log" > vpn_data
python3 parse.py 
