# # demo 1
# def count(num):
#     counter =  1
#     while counter<=num:
#         yield counter
#         counter += 1

# gen = count(10)
# for n in gen:
#     print(n)

# # demo 2
# gen = (x ** 2 for x in range(5))

# for num in gen:
#     print(num)

# demo 3

numbers = [1,2,3,4,5,6,7,8,9,10]

even = (num for num in numbers if num%2 == 0)
for e in even:
    print(e)

odd = (num for num in numbers if num%2 != 0)
for o in odd:
    print(o)