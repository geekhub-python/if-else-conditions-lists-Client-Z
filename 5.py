#!/usr/bin/env python3

my_list = [1,-2,-3,-1, 3,4]

for i in range(len(my_list)-1):
	if( (my_list[i] > 0 and my_list[i+1] > 0) or (my_list[i] < 0 and my_list[i+1] < 0) ):
		print(my_list[i], my_list[i+1])
		break
