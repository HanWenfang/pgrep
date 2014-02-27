#!/usr/bin/env python
# -*-coding:utf-8 -*-

import os
import sys
import math

def listToGrep(l):
	outputs = []
	for i in l:
		fd = os.popen("grep test", 'w') 
		fd.write(i)
	return outputs
	
def parallel(partitions):
	outputs = []
	for lines in partitions:
		output = listToGrep(lines)
		if(len(output) != 0):
			outputs.extend(output)

def partition(lines):
	partitions = []
	length = len(lines)

	if length < 5:
		partitions.extend(lines)
		return partitions

	#int(math.floor(length/5))
	# Time to partition
	num = length/5
	partition_length = []
	
	for i in xrange(1,5):
		partition_length.append(num)
	partition_length.append(length-4*num)

	
	i = 0
	counter = partition_length[i]
	partition = []

	for j in lines:
		partition.append(j)
		counter -= 1

		if counter == 0:
			i += 1
			if (i < len(partition_length)):
				counter = partition_length[i]

			if len(partition) != 0:
				partitions.append(partition)
				partition = []

	return  partitions

def main():
	lines = sys.stdin.readlines()
	partitions = partition(lines)
	parallel(partitions)

if __name__ =="__main__":
	main()



