"""
@Description : 文本分词
@File        : WordCut.py
@Project     : TextAnalysisTools
@Time        : 2022/3/28 11:06
@Author      : hanhan
@Software    : PyCharm
"""
import jieba


def WordCut(inputUrl, outputUrl, myWordUrl=None):
    """
    通过jieba库分词
    :param inputUrl: 输入的文本内容文件
    :param outputUrl: 输出的分词文件
    :param myWordUrl: 自定义词表文件地址（可以不填）
    :return:
    """
    # 读取用于分析的文本
    context = open(inputUrl, 'r', encoding='utf8').read()

    # 加载自定义词表
    print('正在加载自定义词表...')
    try:
        for word in open(myWordUrl, 'r', encoding='utf8').read().split():
            jieba.add_word(word)
        print('自定义词表加载完毕')
    except:
        print('没有提供自定义词表')

    # jieba.lcut分词
    print('正在使用jieba进行中文分词...')
    wordsText = jieba.lcut(context)
    print('jieba分词结束')

    # 保存分词结果
    print('保存分词结果中...')
    f = open(outputUrl, 'w', encoding='utf8')
    f.write(' '.join(wordsText))
    print('分词保存完毕')


if __name__ == "__main__":
    pass
