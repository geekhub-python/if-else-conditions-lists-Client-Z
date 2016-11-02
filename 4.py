#!/usr/bin/env python3

my_list = [3, 2, 1, 2, 2, 4, 3, 2, 5, 3, 2]
temp_count, i = 0, 0
 
while i < len(my_list):
	temp_count += my_list.count(my_list[i]) - 1
	my_list.pop(i)
	
print(temp_count)
