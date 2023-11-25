a = int(input())

def solution(b):
    answer = ""
    while b != 0:
        answer = str(b%2) + answer
        b = b//2
    return answer
    
print(solution(a))