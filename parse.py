
# find the starting line from an array and an identifier 
def get_line(data, ident):
    for i in range(len(data)):
        if ident in data[i]:
            return i + 1

#parse a line from the vpn data to extract the ip, domain and add tld
def parse_line(line):
    return line[0] + " " + line[1] + ".lancs\n"

def main():
    # open vpn data from container
    with open('vpn_data') as f:
        data = f.readlines()
    
    #open existing data 
    with open('/etc/hosts') as f:
        old_hosts = f.readlines()
    
    # open a hosts file as output
    hosts = open("hosts","w+")

    # instantiate new hosts array
    new_hosts = []

    # extract the old hosts list from /etc/hosts
    for i in range(get_line(old_hosts, "# VPN Hosts"), len(old_hosts)):
        if old_hosts[i] != "\n":
            new_hosts.append(old_hosts[i])
    
    print("Existing Hosts: ")
    print(new_hosts)

    # get list of new hosts, cross check with existing hosts, add any new hosts
    for i in range(get_line(data, "Virtual Address"), len(data)):
        if "GLOBAL" in data[i]:
            break
        line = data[i].split(",")
        parsed_line = parse_line(line)
        if not parsed_line in new_hosts:
            new_hosts.append(parsed_line)
    
    # print(new_hosts)

    # save hosts to file
    for i in range(0, len(new_hosts)):
        # print(new_hosts[i])
        hosts.write(new_hosts[i])

    hosts.close

main()
