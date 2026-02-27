import sys

token =open("token", "rb").read().strip()

for (i, c) in enumerate(token):
	print(chr(c-i), end="")
