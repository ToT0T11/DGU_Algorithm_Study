def count_papers(paper, x, y, size):
    color = paper[x][y]
    for i in range(x, x + size):
        for j in range(y, y + size):
            if paper[i][j] != color:
                size //= 2
                return (count_papers(paper, x, y, size) +
                        count_papers(paper, x, y + size, size) +
                        count_papers(paper, x + size, y, size) +
                        count_papers(paper, x + size, y + size, size))
    if color == 0:
        return (1, 0)
    else:
        return (0, 1)

def solve(paper):
    n = len(paper)
    white, blue = count_papers(paper, 0, 0, n)
    print(white)
    print(blue)

n = int(input().strip())
paper = [list(map(int, input().strip().split())) for _ in range(n)]

solve(paper)
