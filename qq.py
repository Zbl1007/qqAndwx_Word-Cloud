#coding=utf-8
import itchat
import sys
import calendar
import importlib
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator
import matplotlib.pyplot as plt
from scipy.misc import imread
import jieba
from qqbot import _bot as bot

non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

importlib.reload(sys)
#登录
bot.Login()
# #获取好友列表
list1 = bot.List('buddy')



 
f1 = open('out.txt','w')
for i in list1:
	try:
		f1.write(str(i)[3:-1]+"\n")
	except UnicodeEncodeError as e:
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

# text = stop_words(text)

# text = jieba.cut(text,cut_all=True)
# text = " ".join(text)


wc.generate_from_text(text)


img_colors = ImageColorGenerator(backgroud_Image)

plt.imshow(wc.recolor(color_func = img_colors))

plt.axis('off')
plt.show()

wc.to_file('hhhh.jpg')


