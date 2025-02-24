# # <=== 1 - masala ===>
# def deco(f):
#     def g(*args, **kwargs):
#         return f(*args, **kwargs).upper()
#     return g

# @deco
# def func(x):
#     return x

# print(func("salom"))


# # <=== 2 - masala ===>
# def deco(f):
#     def g(*args, **kwargs):
#         return f(*args, **kwargs)[::-1]
#     return g

# @deco
# def reverse(x):
#     return x

# print(reverse("salom"))


# # <=== 3 - masala ===>
# import time

# def deco(f):
#     def g(*args, **kwargs):
#         v0 = time.time()
#         x = f(*args, **kwargs)
#         v = time.time()
#         print(f"Ishlash vaqti: {v - v0}")
#         return x
#     return g

# @deco
# def func(x):
#     time.sleep(1) # for test
#     return x

# print(func(0))


# # <=== 4 - masala ===>
# count = 0

# def deco(f):
#     def g(*args, **kwargs):
#         global count
#         count += 1
#         return f(*args, **kwargs) * 2
#     return g

# @deco
# def func(x):
#     return x

# print(func(2))
# print(func(3))
# print(func(4))
# print(func(7))
# print(f"funksiya {count} marta chaqirildi")