
class Found(Exception): pass
try:
    for i in range(100):
        for j in range(1000):
            for k in range(10000):
               if i + j + k == 777:
                  raise Found
except Found:
    print i, j, k