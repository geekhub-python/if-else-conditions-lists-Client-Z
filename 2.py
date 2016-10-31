#!/usr/bin/env python3

n1 = int(input("Enter number: "))
n2 = int(input("Enter number: "))
n3 = int(input("Enter number: "))

if(n1 == n2 == n3):
	print(3)
elif(n1 != n2 and n1 != n3 and n2 != n3):
	print(0)
else:
	print(2)
