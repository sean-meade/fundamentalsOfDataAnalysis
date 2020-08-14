import re

print(re.match("c", "abcdef"))
print(re.match("abcdef", "abcdef"))
print(re.match("^a", "abcdef"))

f = open("iris.csv.data", "r")

data = f.read()

# takes a string and splits it into a arry of strings using \n as the delimiter
# + means one or more. 
lines = re.split(r"\n+", data)

print(lines)
print(lines[0])

vals = re.split(r",", lines[0])

print(vals)
print(vals[2])

f.close()
