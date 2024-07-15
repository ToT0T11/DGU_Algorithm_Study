def can_place_routers(houses, distance, routers):
    count = 1
    last_position = houses[0]
    
    for i in range(1, len(houses)):
        if houses[i] - last_position >= distance:
            count += 1
            last_position = houses[i]
        if count >= routers:
            return True
            
    return False

def find_max_distance(houses, routers):
    houses.sort()
    left = 1
    right = houses[-1] - houses[0]
    result = 0
    
    while left <= right:
        mid = (left + right) // 2
        if can_place_routers(houses, mid, routers):
            result = mid
            left = mid + 1
        else:
            right = mid - 1
            
    return result

n, c = map(int, input().split())
houses = [int(input()) for _ in range(n)]

max_distance = find_max_distance(houses, c)
print(max_distance)
