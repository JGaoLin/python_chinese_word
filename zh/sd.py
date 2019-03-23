import pandas as pd
from wordcloud import WordCloud
import jieba
import matplotlib.pyplot as plt
import PIL.Image as image
import numpy as np

txt = open(r'G:\aa\三体.txt', 'r', encoding='utf8').read()  # 打开三体小说文件
jieba.load_userdict(r'G:\aa\three.txt')  # 读取三体小说词库

Filess= open(r'G:\aa\stops_chinese.txt', 'r', encoding='utf8')  # 打开中文停用词表
stops = Filess.read().split('\n')  # 以回车键作为标识符把停用词表放到stops列表中


wordsls = jieba.lcut(txt)  # 使用jieba中文分词组件
wcdict = {}


tokens=[token for token in wordsls if token not in stops]
print("过滤后中文内容对比:",len(tokens), len(wordsls))

# 统计词频次数
for word in tokens:
    if len(word) == 1:
        continue
    else:
        wcdict[word] = wcdict.get(word, 0) + 1

# 词频排序
wcls = list(wcdict.items())
wcls.sort(key=lambda x: x[1], reverse=True)


# 打印前20词频最高的中文
for i in range(20):
    print(wcls[i])

# 存储结果
pd.DataFrame(wcls).to_csv('three.csv', encoding='utf-8')

# 读取生成词云
txt = open('three.csv', 'r', encoding='utf-8').read()


cut_text = "".join(jieba.lcut(txt))
mywc = WordCloud().generate(cut_text)

plt.imshow(mywc)
plt.axis("off")
plt.show()