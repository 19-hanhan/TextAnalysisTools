# -------------------------------------------------------------------------------
# Description: 
# Reference: 
# Author: hanhan 
# Date: 2022/2/28
# -------------------------------------------------------------------------------
from Configs.config import *
from Tools.DrawWordCloud import ImgDraw
from Tools.WordCount import Count
from Tools.WordCut import WordCut


def main():
    WordCut(OriginText, wordCutText, CustomizeWordList)
    Count(wordCutText, TermFrequencyText, StopWordList)
    ImgDraw(TermFrequencyText, OutputWordCloudPath, WordCloudBackgroundPath)


if __name__ == "__main__":
    main()
