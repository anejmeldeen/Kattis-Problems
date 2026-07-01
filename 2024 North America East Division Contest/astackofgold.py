TUNG = 29260
GOLD = 29370

w, s = list(map(int, input().split()))
expected = s*(s+1) // 2 * TUNG

diff = w - expected

print(diff // (GOLD - TUNG))