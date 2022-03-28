"""
@Description : 分词统计
@File        : WordCount.py
@Project     : TextAnalysisTools
@Time        : 2022/3/28 11:12
@Author      : hanhan
@Software    : PyCharm
"""
from textblob import TextBlob


def Count(inputUrl, outputUrl, stopListUrl=None):
    """
    使用textblob统计词频并删除停用词
    :param inputUrl: 输入的分词文件
    :param outputUrl: 输出的词频文件
    :param stopListUrl: 停用词表地址（可以不填）
    :return:
    """
    wordsText = open(inputUrl, 'r', encoding='utf8').read().split()

    # 使用textblob统计词频
    print('textblob统计词频中...')
    blob = TextBlob(' '.join(wordsText))  # 用于分析的文本块
    # print(blob.word_counts)
    print('词频统计结束')

    # 删除停用词
    print('正在加载停用词表...')
    stopList = []
    try:
        stopList = open(stopListUrl, 'r', encoding='utf8').read().split()
        print('停用词加载成功')
    except:
        print('没有提供停用词表')

    # 写入词频结果
    print('正在保存词频结果')
    TermFrequencyFile = open(outputUrl, 'w', encoding='utf8')
    for item in sorted(blob.word_counts.items(), key=lambda x: x[1], reverse=True):
        if item[0] not in stopList:
            TermFrequencyFile.write(item[0] + ' ' + str(item[1]) + '\n')
    print('词频保存成功')


if __name__ == "__main__":
    pass
