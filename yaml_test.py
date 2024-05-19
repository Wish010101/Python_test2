import yaml
import networkscan

data = {'192.168.2.1': 'Router', '192.168.2.2': 'Cam'}

with open("IP.yaml", "w") as f:
    yaml.dump(data, f)

my_network = "192.168.2.0/24"
my_scan = networkscan.Networkscan(my_network)
my_scan.run()

for i in my_scan.list_of_hosts_found:  # сканироване
    print(i)
