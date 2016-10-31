#!/usr/bin/env python3

n = int(input("Enter number: "))

if(n%4 == 0 and n%100 != 0):
	print("YES")
elif(n%400 == 0):
	print("YES")
else:
	print("NO")
