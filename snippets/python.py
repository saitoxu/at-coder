# ------------------------
# 再帰回数の上限を変更
# ------------------------
import sys
import resource

sys.setrecursionlimit(10 ** 9)
# 合わせてスタックの最大サイズを変更する必要があることもある
# ただしAtCoderではresourceモジュールが使えないらしく, 提出時は除くこと
resource.setrlimit(resource.RLIMIT_STACK, (-1, -1))


# ------------------------
# enumerate
# ------------------------
l = [1, 2, 3]
for idx, i in enumerate(l):
    print(idx, i)


# ------------------------
# zfill
# ------------------------
print('123'.zfill(5)) # => '00123'


# ------------------------
# 和集合・積集合
# ------------------------
s1 = set([1, 2, 3])
s2 = set([2, 4, 6])
print(s1 | s2) # => {1, 2, 3, 4, 6}
print(s1 & s2) # => {2}


# ------------------------
# 2進数・8進数・16進数
# ------------------------
print(bin(15)) # => '0b1111'
print(oct(15)) # => '0o17'
print(hex(15)) # => '0xf'


# ------------------------
# 論理和・論理積・排他的論理和・反転
# ------------------------
print(bin(0b110 | 0b001)) # =>  '0b111'
print(bin(0b100 & 0b111)) # =>  '0b100'
print(bin(0b100 ^ 0b011)) # =>  '0b111'
print(bin(~0b100))        # => '-0b101' note. 1011(-5)のマイナス表記


# ------------------------
# LRU Cache
# ------------------------
from functools import lru_cache

# 引数はハッシュ化できる必要がある(リストとかはNG)
@lru_cache(maxsize=None)
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(10))


# ------------------------
# numpy
# ------------------------
import numpy as np
ary = np.asarray([[1, 2, 3], [4, 5, 6]])
print(ary.shape)
