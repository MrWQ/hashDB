import hashlib


def hashDB(s):
    bs = bytes(s.encode())
    print(bs)
    # new
    # m = hashlib.new('md5',bs)
    # print(m.hexdigest())

    #直接new不同hash对象
    md5 = hashlib.new('md5', bs).hexdigest()
    print(md5)
    print('md5 位数'+str(len(md5)))
    sha1 = hashlib.new('sha1', bs).hexdigest()
    print(sha1)
    print('sha1 位数' + str(len(sha1)))
    sha224 = hashlib.new('sha224', bs).hexdigest()
    print(sha224)
    print('sha224 位数' + str(len(sha224)))
    sha256 = hashlib.new('sha256', bs).hexdigest()
    print(sha256)
    print('sha256 位数' + str(len(sha256)))
    sha384 = hashlib.new('sha384', bs).hexdigest()
    print(sha384)
    print('sha384 位数' + str(len(sha384)))
    sha512 = hashlib.new('sha512', bs).hexdigest()
    print(sha512)
    print('sha512 位数' + str(len(sha512)))
    blake2b = hashlib.new('blake2b', bs).hexdigest()
    print(blake2b)
    print('blake2b 位数' + str(len(blake2b)))
    blake2s = hashlib.new('blake2s',bs).hexdigest()
    print(blake2s)
    print('blake2s 位数' + str(len(blake2s)))
    sha3_224 = hashlib.new('sha3_224',bs).hexdigest()
    print(sha3_224)
    print('sha3_224 位数' + str(len(sha3_224)))
    sha3_256 = hashlib.new('sha3_256', bs).hexdigest()
    print(sha3_256)
    print('sha3_256 位数' + str(len(sha3_256)))
    sha3_384 = hashlib.new('sha3_384', bs).hexdigest()
    print(sha3_384)
    print('sha3_384 位数' + str(len(sha3_384)))
    sha3_512 = hashlib.new('sha3_512', bs).hexdigest()
    print(sha3_512)
    print('sha3_512 位数' + str(len(sha3_512)))
    # shake_128 = hashlib.new('shake_128',bs).hexdigest()
    # print(shake_128)
    # shake_256 = hashlib.new('shake_256', bs).hexdigest()
    # print(shake_256)



if __name__ == '__main__':
    s = 'root1234'
    hashDB(s)