import base64,linecache,pymysql




# 读文件并得到明文列表
def getLisOfPW(path):
    pws=[]
    line = 1
    # line = 44470
    # 只要能读到内容（包括换行）就一直读
    # while (linecache.getline(path, line)):
    for line in range (1,44470):
        # 读取文件特定行，去除掉换行符
        pw = linecache.getline(path, line)
        pw = pw.replace("\n", "")
        line +=1
        # 如果不存在列表里就插入列表
        if pw not in pws:
            pws.append(pw)
    return pws


def baseDB(s):
    print(s)
    bs = bytes(s.encode())
    print(bs)
    base = base64.b64encode(bs)
    base = str(base, 'utf-8')
    print(base)
# 更新数据库，base64是后来才想到的，所以前面有些数据没有填这个字段，因此需要更新
    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "431879", "hash")
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # SQL 语句
    sql = "UPDATE `hash` SET base64 = '%s' WHERE pw = '%s'" %(base,s)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 执行sql语句
        db.commit()
        # 打印提示
        print('更新成功')
    except:
        # 发生错误时回滚
        db.rollback()
        # 打印提示
        print('更新失败')
    # 关闭数据库连接
    db.close()

if __name__ == '__main__':
    path = 'F:\字典破解\密码字典\\10w1.txt'
    print('读取文件中...')
    pws = getLisOfPW(path)
    print('加密中...')
    for pw in pws:
        baseDB(pw)