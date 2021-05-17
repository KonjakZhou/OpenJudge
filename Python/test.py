import time
from multiprocessing import Pool

class testClass(object):
    def fun(self, k):
        time.sleep(1)
        print("{:f} is doing...".format(k))
        ans = [[k,k], [k,k]]
        return ans

p = Pool(2)

obj = testClass()
start = time.time()
ans = list()
for i in range(20):
    p.apply_async(obj.fun, args=(float(i),))
p.close()
p.join()
# for i in ans:
#     print(i.get())
# print(time.time() - start)

# for i in range(20):
#     print(obj.fun(i))
# print(time.time() - start)
