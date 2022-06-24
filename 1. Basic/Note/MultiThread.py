# # Before
# total1 = 0

# for i in range(0, 100000000):
#     total1 += i
# print(total1)

# after
# multithread 쓰기
# 한문제를 여러 cpu가 나누어서 
from threading import Thread
def calc(start, end):
    total = 0
    for i in range(start, end):
        total += i 
    print(total)

if __name__ == "__main__":
    start, end = 0 , 100000000
    thr1 = Thread(target=calc, args=(start,end))

    thr1.start()
    thr1.join()

# 문제수에 따라 여러문제를 각자 cpu에 분할한다 => Multiprocess
# 한 문제를 여러 cpu에 분할한다(팀플처럼 ) = MultiThread 