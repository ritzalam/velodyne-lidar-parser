#!/usr/bin/env python

import dpkt

print("opening file")
f = open('./unit_46_Monterey_subset.pcap', 'rb')
res = open("lidar.txt", "w")

pcap = dpkt.pcap.Reader(f)

for ts, buf in pcap:
    eth = dpkt.ethernet.Ethernet(buf)
    ip = eth.data
    udp = ip.data
		
    if udp.dport == 2368 and len(udp.data) > 0:
		for i in range(1206):
			ba = bytearray(udp.data)
			for byte in ba:
				hdata = hex(byte).strip("L").strip("0x") + " "
				res.write(hdata)
	
res.close()	
f.close()
