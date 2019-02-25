def get_line(data):
    for i in range(len(data)):
        if "Virtual Address" in data[i]:
            return i + 1

def main():
    with open('vpn_data') as f:
        data = f.readlines()
    
    hosts = open("hosts","w+")

    for i in range(get_line(data), len(data)):
        if "GLOBAL" in data[i]:
            break
        line = data[i].split(",")
        hosts.write(line[0] + " " + line[1] + ".lancs\n")
    
    hosts.close

main()