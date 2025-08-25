# 4:03
# 17608 막대기
'''
일렬로 높이가 다른 직육면체 세워 -> 오른쪽에서 봤을때 보이는 기둥의 개수 != 세워진 기둥의 개수
N 개의 막대기에 대한 높이가 주어질때, 오른쪽에서 최종 몇개가 보이게 되는지 계산하는 프로그램을 만들ㅇ러ㅏ

인풋 
N   (2<=N <=100000)
h1  (1 <= h <= 100000)
h2
h3
..
hn

아웃풋
오른쪽에서 봤을때 보이는 막대기의 개수
'''
import sys
user_input = sys.stdin.read().split()

N = int(input(user_input[0]))
# constraint 1
if not (2 <= N <= 100000):
    sys.exit()

h_list = list(map(int,input(user_input[1:])))

# 유저가 입력한 막대기의 길이 조건을 만족하는지 확인
if not all (1 <= h <= 100000 for h in h_list):
    sys.exit()

# 인풋 길이랑 N 일치하지 않으면 종료
if len(h_list) != N:
    sys.exit()

# for _ in range(N):
    ''' !Exceed time limit : python input() is too slow for getting all inputs when they called many times
    sys.stdin.readline() : ✅good
    sys.stdin.read() : ✅✅ very fast'''
#     h_i = int(input())
#     if not 1 <= h_i <= 100000:
#         exit()
#     else:
#         h_list.append(h_i)
# # print(h_list)

max_height = 0
count = 0
for h in reversed(h_list):
    if h > max_height:
        max_height = h
        count += 1
print(count)
# 4:22