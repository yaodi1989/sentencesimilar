#-*-coding:utf-8-*-
import numpy as np

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

file_path = "F:\\AIProject\\CIKM\\cikm_test_a_20180516.txt"
result = []
with open(file_path, "r", encoding="utf-8") as f:
    for line in f:
        temp_list = line.split("\t")
        result.append(temp_list)

for i in result:
    if(len(i)>2 or len(i)<2):
        print("aaaaaaaa")
print(result)