n = int(input())

def binary(n, list):
    a = n // 2
    b = n % 2
    list.append(b)
    if a == 0 :
        return list
    else :
        return binary(a, list)
    
def changenum(li):
    changedanswer = ""
    for i in range(len(li)):
        n = i + 1
        changedanswer = changedanswer + li[-n]
        i += 1
    return changedanswer

answerlist = []
answer = binary(n,answerlist)
# answer.sort()

answer_answer = "".join(([str(i) for i in answer]))
print(changenum(answer_answer))