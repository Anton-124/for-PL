square = open('1.txt', 'r')
Points = open('2.txt', 'r')
################################
x = 0
y = 1
counter = 0
################################
A = [float(i) for i in square.readline().split()]
B = [float(i) for i in square.readline().split()]
C = [float(i) for i in square.readline().split()]
D = [float(i) for i in square.readline().split()]
################################
while True:
    line = [float(i) for i in Points.readline().split()]
    if line != []:
        if ((line[x] > A[x]) and (line[y] > A[y])) and ((line[x] < D[x]) and (line[y] > D[y])) and ((line[x] < C[x]) and (line[y] < C[y])) and ((line[x] > B[x]) and (line[y] < B[y])):
            print(counter, '- точка внутри')
            counter += 1
################################
        elif (line[x] > A[x]) and (line[y] > A[y]) and (line[x] > B[x]) and (line[y] >= B[y]) and (line[x] > C[x]) and (line[y] >= C[y]) and (line[x] > D[x]) and (line[y] > D[y]):
            print(counter, '- точка снаружи')
            counter += 1
        elif (line[x] > A[x]) and (line[y] > A[y]) and (line[x] > B[x]) and (line[y] > B[y]) and (line[x] <= C[x]) and (line[y] > C[y]) and (line[x] <= D[x]) and (line[y] > D[y]):
            print(counter, '- точка снаружи')
            counter += 1
        elif (line[x] <= A[x]) and (line[y] > A[y]) and (line[x] <= B[x]) and (line[y] > B[y]) and (line[x] < C[x]) and (line[y] > C[y]) and (line[x] < D[x]) and (line[y] > D[y]):
            print(counter, '- точка снаружи')
            counter += 1
        elif (line[x] > A[x]) and (line[y] >= A[y]) and (line[x] > B[x]) and (line[y] < B[y]) and (line[x] > C[x]) and (line[y] < C[y]) and (line[x] > D[x]) and (line[y] >= D[y]):
            print(counter, '- точка снаружи')
            counter += 1
        elif (line[x] > A[x]) and (line[y] < A[y]) and (line[x] > B[x]) and (line[y] < B[y]) and (line[x] >= C[x]) and (line[y] < C[y]) and (line[x] >= D[x]) and (line[y] < D[y]):
            print(counter, '- точка снаружи')
            counter += 1
        elif (line[x] >= A[x]) and (line[y] < A[y]) and (line[x] >= B[x]) and (line[y] < B[y]) and (line[x] < C[x]) and (line[y] < C[y]) and (line[x] < D[x]) and (line[y] < D[y]):
            print(counter, '- точка снаружи')
            counter += 1
        elif (line[x] < A[x]) and (line[y] <= A[y]) and (line[x] < B[x]) and (line[y] < B[y]) and (line[x] < C[x]) and (line[y] < C[y]) and (line[x] < D[x]) and (line[y] <= D[y]):
            print(counter, '- точка снаружи')
            counter += 1
        elif (line[x] < A[x]) and (line[y] > A[y]) and (line[x] < B[x]) and (line[y] <= B[y]) and (line[x] < C[x]) and (line[y] <= C[y]) and (line[x] < D[x]) and (line[y] > D[y]):
            print(counter, '- точка снаружи')
            counter += 1
################################
        elif ((line[x] == A[x]) and (line[y] == A[y])) or ((line[x] == D[x]) and (line[y] == D[y])) or ((line[x] == C[x]) and (line[y] == C[y])) or ((line[x] == B[x]) and (line[y] == B[y])):
            print(counter, '- точка на одной из вершин')
            counter += 1
################################
        elif ((line[x] == A[x]) and (B[y] > line[y] > A[y])) or ((line[y] == A[y]) and (D[x] > line[x] > A[x])) or \
                ((line[x] == C[x]) and (C[y] > line[y] > D[y])) or ((line[y] == B[y]) and (C[x] > line[x] > B[x])):
            print(counter, '- точка на одной из сторон')
            counter += 1
################################
        else:
            print(counter,'- Ошибка')
            counter += 1