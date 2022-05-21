'''
[98] 설탕과자 뽑기
격자판의 세로(h), 가로(w), 막대의 개수(n), 각 막대의 길이(l),
막대를 놓는 방향(d:가로는 0, 세로는 1)과
막대를 놓는 막대의 가장 왼쪽 또는 위쪽의 위치(x, y)가 주어질 때,
격자판을 채운 막대의 모양을 출력하는 프로그램을 만들어보자.

입력
첫 줄에 격자판의 세로(h), 가로(w) 가 공백을 두고 입력되고,
두 번째 줄에 놓을 수 있는 막대의 개수(n)
세 번째 줄부터 각 막대의 길이(l), 방향(d), 좌표(x, y)가 입력된다.
5 5
3
2 0 1 1
3 1 2 3
4 1 2 5

[입력값의 정의역]
1 <= w, h <= 100
1 <= n <= 10
d = 0 or 1
1 <= x <= 100-h
1 <= y <= 100-w

출력
모든 막대를 놓은 격자판의 상태를 출력한다.
막대에 의해 가려진 경우 1, 아닌 경우 0으로 출력한다.
단, 각 숫자는 공백으로 구분하여 출력한다.
1 1 0 0 0
0 0 1 0 1
0 0 1 0 1
0 0 1 0 1
0 0 0 0 1
'''
h, w = map(int, input().split())
n = int(input())
brd = [[0 for _ in range(w)]for _ in range(h)]

for j in range(n):
    i, d, x, y = map(int, input().split())
    brd[x-1][y-1] = 1
    if d == 0:  # 가로
        for a in range(1, i):
            brd[x-1][y-1+a] = 1  # +1열
    if d == 1:  # 세로
        for a in range(1, i):
            brd[x-1+a][y-1] = 1  # +1행
for k in brd:
    print(*k)
