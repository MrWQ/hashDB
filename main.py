import hashDB
import datetime
import os
import json


# 获取当前文件夹路径
path = os.path.dirname(os.path.realpath(__file__))
filepath = input("要加密的文件路径：")
# 获取当前时间
nowTime=datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')#现在
print(nowTime)
# # 创建log文件
logFile = path + '/' + nowTime+'.log'
with open(logFile,'a') as f:
    if os.path.isfile(filepath):
        # 改变文件编码utf-8 防止gbk编码文件无法打开
        hashDB.encodeFile(filepath)
        print('读取文件中...')
        pws = hashDB.getLisOfPW(filepath)
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




