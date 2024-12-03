f = open("13.txt").read().split("\n\n")

for goal in [0,1]:
  score = 0
  for pattern in f:
    P = pattern.splitlines()
    X, Y, s, d = len(P[0]), len(P), 0, 0
    Pt = ["".join([P[y][x] for y in range(Y)]) for x in range(X)]

    for x in range(X):
      dx = min(X-x, x)
      diffs = sum(1 for a,b in zip("".join(Pt[x-dx:x]), "".join(Pt[x:x+dx][::-1])) if a!=b)
      if diffs==goal and dx>d: s = x
    for y in range(Y):
      dy = min(Y-y, y)
      diffs = sum(1 for a,b in zip("".join(P[y-dy:y]), "".join(P[y:y+dy][::-1])) if a!=b)
      if diffs==goal and dy>d: s = 100*y

    score+=s

  print(score)
