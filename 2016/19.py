input = 3014387

class Elf:
    def __init__(self, nb):
        self.nb = nb
        self.next = None
        self.previous = None

    def remove(self):
        self.previous.next = self.next
        self.next.previous = self.previous

def create_list(n):
    global first, victim
    first = None
    previous = None
    for i in range(1, n + 1):
        elf = Elf(i)
        if first is None:
            first = elf
        if previous is not None:
            previous.next = elf
            elf.previous = previous
        previous = elf
        if i == int(n/2) + 1:
            victim = elf
    previous.next = first
    first.previous = previous

# global variables
first = None
victim = None

# part 1
create_list(input)
current = first
while current.next != current:
    current.next.remove()
    current = current.next
print(current.nb)

# part 2
create_list(input)
elves_count = input
current = first
while current.next != current:
    # remove victim
    victim.remove()
    victim = victim.next
    if elves_count % 2 != 0:
        victim = victim.next
    elves_count -= 1
    current = current.next
print(current.nb)
