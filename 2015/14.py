class Reindeer:
    def __init__(self, name, speed, flying_time, resting_time):
        self.name = name
        self.speed = speed
        self.flying_time = flying_time
        self.remainig_ft = flying_time
        self.resting_time = resting_time
        self.remainig_rt = resting_time
        self.distance = 0
        self.points = 0
        self.state = "Flying"

    def reset(self):
        self.remainig_ft = self.flying_time
        self.remainig_rt = self.resting_time
        self.distance = 0
        self.points = 0
        self.state = "Flying"

    def race(self, racing_time):
        self.distance = 0
        remaining_time = racing_time
        while(remaining_time > 0):
            if self.state == "Flying":
                remaining_time -= self.flying_time
                self.distance += self.speed * self.flying_time
                if remaining_time < 0:
                    self.distance += self.speed * remaining_time
                self.state = "Resting"
            else:
                remaining_time -= self.resting_time
                self.state = "Flying"

    def race1s(self):
        if self.state == "Flying":
            self.distance += self.speed
            self.remainig_ft -= 1
            if self.remainig_ft == 0:
                self.state = "Resting"
                self.remainig_ft = self.flying_time
        else: # Resting
            self.remainig_rt -= 1
            if self.remainig_rt == 0:
                self.state = "Flying"
                self.remainig_rt = self.resting_time

    def __str__(self):
        return "{} : speed = {}km/s, flying for {}s and resting for {}\n".format(self.name, self.speed, self.flying_time, self.resting_time)

reindeers = set()
with open("14.txt", "r") as f:
    for line in f:
        name = line.split()[0]
        speed = int(line.split()[3])
        flying_time = int(line.split()[6])
        resting_time = int(line.split()[-2])
        reindeers.add(Reindeer(name, speed, flying_time, resting_time))

# Part 1
longest = 0
for reindeer in reindeers:
    reindeer.race(2503)
    if reindeer.distance > longest:
        longest = reindeer.distance
print(longest)

# Part 2
for r in reindeers:
    r.reset()
for t in range(2503):
    for r in reindeers:
        r.race1s()
    distances = [[r.distance, r] for r in reindeers]
    distances = sorted(distances, key=lambda r: r[0], reverse=True)
    distances[0][1].points += 1
    for i in range(1, len(distances)):
        if distances[i][0] == distances[0][0]:
            distances[i][1].points += 1
        else:
            break

print(sorted([r.points for r in reindeers], reverse=True)[0])
