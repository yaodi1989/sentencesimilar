#-*-coding:utf-8-*-
import datetime
import numpy as np
import pandas as pd
import fasttext as ft
import nltk
from CIKM.fast_text import FastVector
from nltk.tokenize import sent_tokenize, word_tokenize
import nltk.tokenize.punkt

file_path_es = "F:\\AIProject\\CIKM\\wiki.es.vec"
file_path_en = "F:\\AIProject\\CIKM\\wiki.en.vec"
fr_dictionary = FastVector(vector_file=file_path_es)
print(fr_dictionary)

# 计算两个向量欧式距离方法
def distance (vec1, vec2):
    d = 0
    for a, b in zip(vec1, vec2):
        d += (a - b) ** 2
    return d ** 0.5

# 计算两个向量的cos值方法
def cos (vec1, vec2):
    dot_product = 0.0
    normA = 0.0
    normB = 0.0
    for a, b in zip(vec1, vec2):
        dot_product += a * b
        normA += a ** 2
        normB += b ** 2
    if normA == 0.0 or normB == 0.0:
        return None
    else:
        return dot_product / ((normA * normB) ** 0.5)

# 分句
sent_list = []
filepath = "F:\\AIProject\\CIKM\\cikm_test_a_20180516.txt"
with open(filepath, "r", encoding="utf-8") as f:
    for line in f:
        temp_list = line.split("\t")
        sent_list.append(temp_list)

#print(len(sent_list))

# 将句子分词成单词
word_list = []
for sent_line in sent_list:
    words = []
    for sent in sent_line:
        s = word_tokenize(sent)
        words.append(s)
        # print(s)
    word_list.append(words)

#print(len(word_list))

# 获得每个单词的词向量，并合并为句子向量
result = []

for w_list in word_list:
    temp_list = []
    for ws in w_list:
        temp = np.zeros(300)
        for w in ws:
            # 有大写的转化为小写
            w = w.lower()
            # 获取单词对应ID
            l = fr_dictionary.word2id
            try:
                w_id = l[w]
            except KeyError:
                print("错误的单词" + w)
                continue
            # print(w_id)
            w_vec = fr_dictionary.embed[w_id]
            # print(w_vec)
            temp = temp + w_vec
        temp_list.append(temp)
    vec1 = temp_list[0]
    vec2 = temp_list[1]
    cos_result = cos(vec1, vec2)
    result.append(cos_result)

# 输出cos数据到文件
nowTime = datetime.datetime.now().strftime('%m%d%H%M')
result_file_path = "F:\\AIProject\\CIKM\\result\\result_" + nowTime + ".txt"
with open(result_file_path, "w", encoding="utf-8") as f:
    for r in result:
        f.write(str(r) + "\n")