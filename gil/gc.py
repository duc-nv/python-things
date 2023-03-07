import sys
import gc


def foo():
    a = []
    b = a
    print(sys.getrefcount(a))

    del b
    print(sys.getrefcount(a))

foo()
print('GC collected: ', gc.collect())