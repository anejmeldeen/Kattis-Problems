tung = 29260
gold = 29370

w, s = list(map(int, input().split()))

coins = s * (s + 1) // 2
should_be = coins * tung

diff = w - should_be
print(diff)

print(diff // (gold - tung))