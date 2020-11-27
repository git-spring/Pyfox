# 递归
# 函数自己调用自己
# 一定要设置好结束条件

# 1~n 的和
def get_sum(n):
    if n == 0:
        return 0
    return n + get_sum(n - 1)


print(get_sum(5))


# n 的乘积
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


print(factorial(5))


# 5 * factorial(4)               n = 5
# 5 * 4 * factorial(3)           n = 4
# 5 * 4 * 3 * factorial(2)       n = 3
# 5 * 4 * 3 * 2 * factorial(1)   n = 2
# 5 * 4 * 3 * 2 * 1              n = 1   程序退出, 返回结果


# 斐波那契数列的第n个数
def Fibonacci(n):
    if n <= 2:
        return 1
    return Fibonacci(n - 1) + Fibonacci(n - 2)


print(Fibonacci(8))
