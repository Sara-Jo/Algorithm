from collections import deque

n = int(input())
cards = deque([i for i in range(1, n + 1)])

while len(cards) != 1:
    cards.popleft()
    tmp = cards.popleft()
    cards.append(tmp)

print(cards[0])