# python 3.7.1
# abcde
# ab

# abcde
# bc

# abcde
# bd

# abcdebd
# bd

# 123abcd
# ab

# This does not work with repeat character either in input or search keywords
# Ex
# aabbcd
# abbc
# This fails in below program, refer to StringChecker.py

t = int(input())
while t != 0:
    str_N = input()
    str_F = input()
    len_F = len(str_F)
    len_N = len(str_N)
    current_index_N = 0
    count = 0
    for i in range(len_F):
        if i == 0:
            for j in range(current_index_N, len_N):
                if str_F[i] == str_N[j]:
                    count += 1
                    current_index_N = j
                    break
                else:
                    count = 0
        else:
            if str_F[i] == str_N[current_index_N + i]:
                count += 1
            elif (len_N - i) > len_F:
                i = 0
            else:
                count = 0
                break

    if (count == len_F):
        print("Yes")
    else:
        print("No")

    t -= 1