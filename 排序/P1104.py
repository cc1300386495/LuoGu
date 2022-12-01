# P1104 生日

n = int(input())

persons = []

for i in range(n):
    input_list = list(input().split())
    persons.append([input_list[0], int(input_list[1]), int(
        input_list[2]), int(input_list[3]), - i])  # i 表示输入顺序,越靠后，-i越小

persons.sort(key=lambda x: [x[1], x[2], x[3], x[4]])

for item in persons:
    print(item[0])
