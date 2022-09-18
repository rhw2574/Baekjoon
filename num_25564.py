a = list(map(int, input().split()))
max_len = a[0]
min_len = a[1]

ls_result = []
ls_part = []
part = ""

str = input().strip()

for i in range(0,max_len):
    for j in range(i,max_len):
        part += str[j]
        if(ls_part.count(part) == 0 and len(part) >= min_len):
            ls_part.append(part)
    part = ""
print(ls_part)

for item in ls_part:
    for j in range(0,len(item) - min_len +1):
        if item[j] == item[j+2] and ls_result.count(item) == 0:
            ls_result.append(item)
print(len(ls_result))
