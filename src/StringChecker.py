# abcd
# ab
t = int(input())
while t > 0:
    str_Original = input()
    str_Find = input()
    i = 0
    j = 0
    count = 0
    while i < len(str_Original):
        for j in range(len(str_Find)):
            if (len(str_Original) - i - 1) >= j:
                if str_Original[i+j] == str_Find[j]:
                    if j == len(str_Find) - 1:
                        print("Found String at index : " + str(i))
                        count += 1
                else:
                    break
        i += 1
    if count > 0:
        print("Count : " + str(count))
    else:
        print("Did not find any match")
    t -= 1

