import queue
import re

input = list(open("12.txt").read().strip())
#input = list('[1,-3,{"a":{"d":[12,14,"red",15],"e":"f"}"c":"re","b":2},3]')
print(''.join(input))

pcount = 0
count = 0
open = queue.LifoQueue()
for i in range(len(input)):
    if input[i] == '{':
        count += 1
        open.put(i)
    elif input[i] == '}':
        count -= 1
        if count == pcount - 1:
            start = open.get()
            lookup = ''.join(input[start+1:i])
            while True:
                lookup2 = re.sub(r'\[[^\[]*\]', '', lookup)
                if lookup2 == lookup:
                    break
                lookup = lookup2
            if "red" in lookup:
                input[start:i+1] = ['_']*(i+1-start)
    pcount = count

print(''.join(input))
numbers = [int(x) for x in re.findall(r'[-]?\d+', ''.join(input))]
print(numbers)
print(sum(numbers))
