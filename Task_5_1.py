def odd_nums(max_num):
    for n in range(1, max_num + 1, 2):
        yield n


num = 17
for i in odd_nums(num):
    print(i)
