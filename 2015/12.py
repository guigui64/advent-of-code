import re
input = open("12.txt").read().strip()
list = [int(x) for x in re.findall(r'[-]?\d+', input)]
print(sum(list))
