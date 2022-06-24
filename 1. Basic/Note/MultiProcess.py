# 같은 문제를 나눠서 여러 곳에서 풀기 multiprocess

# Before
# total1 = total2 = total3 = 0

# for i in range(0, 100000000):
#     total1 += i
# print(total1)

# for i in range(100000001, 200000000):
#     total2 += i
# print(total2)

# for i in range(200000001, 300000000):
#     total3 += i
# print(total3)
# print(">>End<<")
# run in python terminal

# After
# 멀티 프로세싱 시작 
from multiprocessing import Process

def start_get(start,end):
    total = 0
    for i in range(start, end):
        total +=i
    print(total)

if __name__ == "__main__":
    #프로세스를 생성합니다.
    p0 = Process(target=start_get, args =(0,100000000))
    p1 = Process(target=start_get, args =(100000001, 200000000))
    p2 = Process(target=start_get, args =(200000001, 300000000))

    # 프로세스의 시작 
    p0.start()
    p1.start()
    p2.start()

    # 순서를 정리 : 다른 프로세스가 종료될 때 대기
    # join 쓴 순서대로 나오지는 않음. 제일 먼저 끝나는 대로 나옴
    p0.join()
    p1.join()
    p2.join()

    print(">>> END <<<")
