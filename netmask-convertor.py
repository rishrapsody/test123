#!/usr/local/bin/python

from ipaddress import IPv4Network
import csv
import os

def main():
	if os.path.exists('data_converted.csv'):
		os.remove('data_converted.csv')
	with open('data.txt') as f:
		lines = f.readlines()
#		print(lines)
		for line in lines:
			line = line.strip()
			print(line)
			converted_data = [IPv4Network(line).network_address,IPv4Network(line).netmask]
			final_data.append(converted_data)
#			print(IPv4Network(line).network_address)
#			print(IPv4Network(line).netmask)
			with open('data_converted.csv','a+') as cfile:
				writer = csv.writer(cfile)
				writer.writerow(converted_data)

if __name__ == "__main__":
	global final_data
	final_data = []
	main()
