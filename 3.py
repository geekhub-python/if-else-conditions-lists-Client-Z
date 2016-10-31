#!/usr/bin/env python3

n = int(input("Enter number: "))
m = int(input("Enter number: "))
k = int(input("Enter number: "))

if( (k%n == 0 or k%m == 0) and k < n*m):
	print("YES")
else:
	print("NO")
