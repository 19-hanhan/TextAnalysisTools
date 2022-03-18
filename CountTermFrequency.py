# -------------------------------------------------------------------------------
# Description: 统计文本词频
# Reference: 
# Author: hanhan 
# Date: 2022/2/27
# -------------------------------------------------------------------------------
import jieba
from textblob import TextBlob

from Configs.config import OriginText, CustomizeWordList, StopWordList, wordCutText, TermFrequencyText


# 通过jieba库进行分词
def WordCut():
    # 读取用于分析的文本
    context = open(OriginText, 'r', encoding='utf8').read()

    # 加载自定义词表
    print('正在加载自定义词表...')
    for word in open(CustomizeWordList, 'r', encoding='utf8').read().split():
        jieba.add_word(word)
    print('自定义词表加载完毕')

    # jieba.lcut分词
    print('正在使用jieba进行中文分词...')
    wordsText = jieba.lcut(context)
    print('jieba分词结束')

    # 保存分词结果
    print('保存分词结果中...')
    wordCutTxt = open(wordCutText, 'w', encoding='utf8')
    wordCutTxt.write(' '.join(wordsText))
    print('分词保存完毕')


# 使用textblob统计词频并删除停用词
def Count():
    wordsText = open(wordCutText, 'r', encoding='utf8').read().split()

    # 使用textblob统计词频
    print('textblob统计词频中...')
    blob = TextBlob(' '.join(wordsText))  # 用于分析的文本块
    # print(blob.word_counts)
    print('词频统计结束')

    # 删除停用词
    print('正在加载停用词表...')
    stopList = open(StopWordList, 'r', encoding='utf8').read().split()
    print('停用词加载成功')

    # 写入词频结果
    print('正在保存词频结果')
    TermFrequencyTxt = open(TermFrequencyText, 'w', encoding='utf8')
    for item in sorted(blob.word_counts.items(), key=lambda x: x[1], reverse=True):
        if item[0] not in stopList:
            TermFrequencyTxt.write(item[0] + ' ' + str(item[1]) + '\n')
    print('词频保存成功')


if __name__ == "__main__":
    # WordCut()
    Count()
