import hashlib
import linecache
import pymysql
import base64

# 改变文件编码utf-8 防止gbk编码文件无法打开
def encodeFile(path):
    # 改变文件编码utf-8 防止gbk编码文件无法打开
    fp = open(path, 'rb')
    fps = fp.read()
    fp.close()
    try:
        fps = fps.decode('utf-8')
        print('当前文件编码为 utf-8,无需修改编码')
    except:
        fps = fps.decode('gbk')
        print('当前文件编码为 gbk,正在修改编码...')
    fps = fps.encode('utf-8')
    fp = open(path, 'wb')
    fp.write(fps)
    fp.close()
    print('当前文件编码为 utf-8')

# 读文件并得到明文列表
def getLisOfPW(path):
    pws=[]
    line = 1
    # 只要能读到内容（包括换行）就一直读
    while (linecache.getline(path, line)):
        # 读取文件特定行，去除掉换行符
        pw = linecache.getline(path, line)
        pw = pw.replace("\n", "")
        line +=1
        # 如果不存在列表里就插入列表
        if pw not in pws:
            pws.append(pw)
    return pws

# 加密并插入数据库
def hashDB(s,f):
    bs = bytes(s.encode())
    print(bs)
    #直接new不同hash对象
    md5 = hashlib.new('md5', bs).hexdigest()
    print(md5)
    f.write('md5: '+md5+'\n')
    sha1 = hashlib.new('sha1', bs).hexdigest()
    print(sha1)
    f.write('sha1: ' + sha1+'\n')
    sha224 = hashlib.new('sha224', bs).hexdigest()
    print(sha224)
    f.write('sha224: ' + sha224+'\n')
    sha256 = hashlib.new('sha256', bs).hexdigest()
    print(sha256)
    f.write('sha256: ' + sha256+'\n')
    sha384 = hashlib.new('sha384', bs).hexdigest()
    print(sha384)
    f.write('sha384: ' + sha384+'\n')
    sha512 = hashlib.new('sha512', bs).hexdigest()
    print(sha512)
    f.write('sha512: ' + sha512+'\n')
    blake2b = hashlib.new('blake2b', bs).hexdigest()
    print(blake2b)
    f.write('blake2b: ' + blake2b+'\n')
    blake2s = hashlib.new('blake2s',bs).hexdigest()
    print(blake2s)
    f.write('blake2s: ' + blake2s+'\n')
    sha3_224 = hashlib.new('sha3_224',bs).hexdigest()
    print(sha3_224)
    f.write('sha3_224: ' + sha3_224+'\n')
    sha3_256 = hashlib.new('sha3_256', bs).hexdigest()
    print(sha3_256)
    f.write('sha3_256: ' + sha3_256+'\n')
    sha3_384 = hashlib.new('sha3_384', bs).hexdigest()
    print(sha3_384)
    f.write('sha3_384: ' + sha3_384+'\n')
    sha3_512 = hashlib.new('sha3_512', bs).hexdigest()
    print(sha3_512)
    f.write('sha3_512: ' + sha3_512+'\n')
    # shake_128 = hashlib.new('shake_128',bs).hexdigest()
    # print(shake_128)
    # shake_256 = hashlib.new('shake_256', bs).hexdigest()
    # print(shake_256)
    base = base64.b64encode(bs)
    base = str(base, 'utf-8')
    print(base)
    f.write('base: ' + base+'\n')
    f.write('\n\n')

    # 插入数据库
    # # 打开数据库连接
    # db = pymysql.connect("localhost", "root", "431879", "hash")
    # # 使用cursor()方法获取操作游标
    # cursor = db.cursor()
    # # SQL 语句
    # sql = "insert into hash(pw,md5,sha1,sha224,sha256,sha384,sha512,blake2b,blake2s,sha3_224,sha3_256,sha3_384,sha3_512,base64) \
    #       VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" \
    #       %(s,md5,sha1,sha224,sha256,sha384,sha512,blake2b,blake2s,sha3_224,sha3_256,sha3_384,sha3_512,base)
    #
    # try:
    #     # 执行SQL语句
    #     cursor.execute(sql)
    #     # 执行sql语句
    #     db.commit()
    #     # 打印提示
    #     print('插入成功')
    # except:
    #     # 发生错误时回滚
    #     db.rollback()
    #     # 打印提示
    #     print('插入失败')
    # # 关闭数据库连接
    # db.close()


if __name__ == '__main__':
    # s = 'root1234'
    # hashDB(s)
    path = 'D:\\1.txt'
    pws = getLisOfPW(path)
    for pw in pws:
        hashDB(pw)


