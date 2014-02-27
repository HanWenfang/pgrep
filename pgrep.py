#!/usr/bin/env python
# -*-coding:utf-8 -*-

import os
import sys
import math

PROCESS_NUM = 5

def listToGrep(l, fd):
	for i in l:
		fd.write(i)
		
def parallel(partitions, parameter):
	global PROCESS_NUM

	outputs = []
	fds = []
	cmd = "grep " + parameter

	for i in range(0, PROCESS_NUM):
		fd = os.popen(cmd, 'w') 
		fds.append(fd)
	i=0;
	for lines in partitions:
		listToGrep(lines, fds[i])
		i += 1

def partition(lines):
	global PROCESS_NUM

	partitions = []
	length = len(lines)

	if length < PROCESS_NUM:
		partitions.extend(lines)
		return partitions

	#int(math.floor(length/5))
	# Time to partition
	num = length/PROCESS_NUM
	partition_length = []
	
	for i in range(1,PROCESS_NUM):
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
	parallel(partitions, sys.argv[1])

if __name__ =="__main__":
	main()



