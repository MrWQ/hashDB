import hashDB
import datetime
import os

# main
path = input("要加密的文件路径：")
# path = 'D:\\1.txt'
# path = 'D:\\10w.txt'
# 获取当前时间
nowTime=datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')#现在
print(nowTime)
# # 打开文件
logFile = nowTime+'.log'
# logFile = path+'.log'
f = open(logFile,'w')

if os.path.isfile(path):
    # 改变文件编码utf-8 防止gbk编码文件无法打开
    hashDB.encodeFile(path)
    print('读取文件中...')
    pws = hashDB.getLisOfPW(path)
    print('加密中...')
    #计数
    count = 0
    for pw in pws:
        count +=1
        # 写入文件
        f.write(nowTime+'\t')
        f.write(pw+'\t\n')
        hashDB.hashDB(pw,f)
        # 每1000条数据刷新缓存
        if count % 1000 == 0:
            f.flush()
else:
    print('该路径不存在文件！')
# 关闭文件
f.close()


