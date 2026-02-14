import sys

str_1 = sys.argv[1]
print(str_1)
rot = sys.argv[2]
rot = int(rot)
decoded = []
# decoded = decoded[rot:] + decoded[:rot]
print(decoded)
print(str_1)

for c in str_1:
	if c.isalpha():
		if c.islower():
			decoded.append(chr((ord(c) - ord('a') + rot) % 26 + ord('a')))
		else:
			decoded.append(chr((ord(c) - ord('A') + rot) % 26 + ord('A')))
	else:
		decoded.append(c)
print(''.join(decoded))

print((-3 + 26) % 26)
print(3 % 26)
