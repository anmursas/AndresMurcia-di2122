s = [1,2]
r = s[:]
s[0]=2
print(s)
print(r)
r = s
s[0] = 5
print(r)