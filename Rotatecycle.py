#For rotating to the right in a list +1 

def solution(A, K):
    for _ in range(K):
        A = [A.pop(len(A)-1)] +A[:len(A)]
    return A

def solution(A, K):
    if len(A) == 0: #in the instance of an empty list 
        return A
    else:
        K = K % len(A)
        return A[-K:] + A[:-K]

solution([3, 8, 9, 7, 6], 3)
solution2([3, 8, 9, 7, 6], 3)
