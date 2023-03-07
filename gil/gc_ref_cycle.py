import sys
import gc


def foo():
    x = []
    x.append(x)
    print(sys.getrefcount(x))
    del x

foo()
print('GC collected: ', gc.collect())