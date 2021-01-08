import heapq
N = int(input())
card_list = []
for _ in range(N):
    heapq.heappush(card_list, int(input()))

if len(card_list) == 1:
    print(0)
else:
    answer = 0
    while len(card_list) > 1:
        first = heapq.heappop(card_list)
        second = heapq.heappop(card_list)
        answer += first + second
        heapq.heappush(card_list, first + second)
    print(answer)