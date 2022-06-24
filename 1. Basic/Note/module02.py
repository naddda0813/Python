# 문자열과 숫자
def sum(a, b):
    if type(a) != type(b):
        print("더하기를 할 수 없습니다")
        return
    else:
        return a + b
# system 변수 
# main method
# _ 2개 
if __name__ == "__main__":
    print(sum(10,20))

# 오른쪽 마우스 > run python in terminal