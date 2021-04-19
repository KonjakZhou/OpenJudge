import sympy   # 引入解方程的专业模块sympy

import time

start = time.time()
x = sympy.symbols("x")   # 申明未知数"x"
y = sympy.symbols("y")   # 申明未知数"x"

a = sympy.solve(
    [
        x ** 2 + y ** 2 -1,
        x - y
    ],[x,y])   # 写入需要解的方程体
b = [[x.evalf() for x in y ] for y in a]
print(b)
print(time.time() - start)
