import os
def getTxt():
        txt = open("library.txt","r").read()
        return txt
kusTxt=getTxt()
words=kusTxt.split(',')
for word in words:
    os.system("pip install "+word)
    print("{}成功安装".format(word))
print('已完成所有安裝!!!')
input()
