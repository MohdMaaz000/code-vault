k = int(input())
room_list = list(map(int, input().split()))

room_set = set(room_list)
sum_set = sum(room_set) * k
sum_list = sum(room_list)

captain_room = (sum_set - sum_list) // (k - 1)
print(captain_room)
