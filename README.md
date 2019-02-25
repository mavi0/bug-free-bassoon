# OVPN Hosts to /etc/hosts
For use with an OVPN instance from [here](https://github.com/kylemanna/docker-openvpn)

Gets a list of the IP to HOST mappings from OVP and inserts them into the /etc/hosts file the local machine.

Run main.sh as sudo, passing in the OVPN docker instance name as a param. 

For example:

```
$ docker ps -a
CONTAINER ID    IMAGE           STATUS         PORTS                    NAMES
cca3aefb50de    51cb67c43598    Up 7 hours     0.0.0.0:1194->1194/udp   youthful_zhukovsky

$ sudo ./main.sh youthful_zhukovsky
```
