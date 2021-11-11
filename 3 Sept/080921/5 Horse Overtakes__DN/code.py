# P = [5, 7, 4, 10, 3, 7]   =>velocities
#      0  1  2  3   4   5   =>positions

# 0 <= v => 10

# dis = [0,0,0,0,0,0,0,0,0,0,0]  # size 11 ( 0 to 10)
# move with increasing positions and keep updating the lower
# each iterations -> is there any element, with [lower positions ] and [higher vel]
n = int(input())
pos = [0]*n

for i in range(n):
    x, y = map(int, input().split())
    pos[x] = y

dis = [0]*11
overtake = 0
for position in range(n):
    vel = pos[position]
    for j in range(vel+1, 11):
        overtake += dis[j]
    dis[vel] += 1

print(overtake)


# https://6793fdf6.widgets.sphere-engine.com/lp?hash=hGambFsYTS