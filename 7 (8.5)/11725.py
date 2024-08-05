import sys
input = sys.stdin.readline

n = int(input())
tree = {i:[] for i in range(1,n+1)}
for _ in range(n-1):
    first, second = map(int, input().split())
    tree[first].append(second)
    tree[second].append(first)

parents = {i:-1 for i in range(1,n+1)}
visited = {i:False for i in range(1,n+1)}

def write_parent(start):
    parents[start]=0
    stack = [start]
    visited = [False]*(n+1)

    while stack:
        current = stack.pop()
        
        for node in tree[current]:
            if not visited[node]:
                stack.append(node)
                parents[node]=current
                visited[current] = True

write_parent(1)

for i in range(2,n+1):
    print(parents[i])
