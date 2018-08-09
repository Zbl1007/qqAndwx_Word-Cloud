#coding=utf-8
import itchat
import sys
import calendar
import importlib
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator
import matplotlib.pyplot as plt
from scipy.misc import imread
import jieba
# from qqbot import _bot as bot

non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

importlib.reload(sys)
#登录
itchat.auto_login(hotReload=True)
# bot.Login()
# list1 = bot.List('buddy')

# #发送消息
# #itchat.send('你好啊！','filehelper')

# #获取好友列表
friends = itchat.get_friends(update=True)[0:]

# # 初始化计数器，有男有女，当然，有些人是不填的
# male = female = other = 0

# # 遍历这个列表，列表里第一位是自己，所以从"自己"之后开始计算

 
f1 = open('out.txt','w')
# for i in list1:
# 	try:
# 		f1.write(str(i)[3:-1]+"\n")
# 	except UnicodeEncodeError as e:
# 		continue

# f1.close()  
for i in friends:
    try:
        #print(i)
        if i['Signature'] !="":
            if i['RemarkName'] !="":
                print(i['RemarkName']+"："+i['Signature'])
            else:
                print(i['NickName']+"："+i['Signature'])
            f1.write(i['Signature']+'\n')
    except ValueError as e:
        #print(e)
        continue

f1.close()    
backgroud_Image = plt.imread('hhh.jpg')
wc = WordCloud(
    background_color = 'white',
    mask = backgroud_Image,
    font_path = 'C:\\Windows\\Fonts\\STZHONGS.TTF',
    max_words = 2000,
    max_font_size = 100,
    random_state = 30,
    
    )


text = open('out.txt','r').read()

#分词jieba
# text = stop_words(text)

text = jieba.cut(text,cut_all=True)
text = " ".join(text)


wc.generate_from_text(text)


img_colors = ImageColorGenerator(backgroud_Image)

plt.imshow(wc.recolor(color_func = img_colors))

plt.axis('off')
plt.show()

wc.to_file('hhhh.jpg')


