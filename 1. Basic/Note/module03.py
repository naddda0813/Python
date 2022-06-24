# 변수 
PI = 3.141592

# class
class Math: 
    a = 1 
    # 클래스에 함수 만들 때 self를 넣어야 math에 있는 종속함수를 정의하는 것 
    def solve(self, r):
        # 원의 면적 구하기 
        # r = 반지름 
        return PI * (r**2)
    def sum(self, a, b):
        return a + b 
# jupyter는 싱글cpu 이고 terminal은 multi cpu라서 여러번 실행 가능 
if __name__ == "__main__":
    print(PI)
    a = Math()
    print(a.solve(2))
    print(a.sum(PI, 4.4))