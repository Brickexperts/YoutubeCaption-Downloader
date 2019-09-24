import matplotlib.pyplot as plt
import wordcloud
from scipy.misc import imread
from collections import Counter

def count(string):
    # 按照空格分割字符串
    list1 = string.split(" ")
    word_dict = Counter(list1)
    return sorted(zip(word_dict.keys(), word_dict.values()), key=lambda x: x[1], reverse=True)
def paint(args):
    dict1 = dict(args)
    x = list(dict1.keys())
    y = list(dict1.values())
    plt.figure(figsize=(100, 25))
    plt.bar(x, y, color="blue")
    plt.show()

def paintDiag(wordlength,rank=12):
    with open("caption.txt", "r", encoding="utf-8") as f:
        char = f.read()
        string = char.lower()
        string1 = string.replace("\n", " ")
        string2=string1.replace(",", " ")
        string3=string2.replace(".", " ")
        string4=string3.replace("?", " ")
        string5=string4.split(" ")
        string5=[x for x in string5 if len(x)==wordlength]
        new_tuple = tuple(count(str(string5)))
        paint(new_tuple[0:rank])

def makeDict():
    with open("caption.txt", "r", encoding="utf-8") as f:
        char = f.read()
        string = char.lower()
        string1 = string.replace("\n", " ")
        string2=string1.replace(",", " ")
        string3=string2.replace(".", " ")
        string4=string3.replace("?", " ")
        string5=string4.split(" ")
        string5=[x for x in string5]
        new_tuple = tuple(count(str(string5)))
        with open("dict.txt","w",encoding="utf-8") as o:
            for word,freq in new_tuple:
                o.write(word[1:-2]+" "+str(freq)+"\n")

def word_cloud(args=open("caption.txt","r",encoding="utf-8").read()):
    Wordcloud=wordcloud.WordCloud(width=2560,height=1440,font_path="COOPBL.TTF",background_color="white",mask=imread("mask.png")).generate(args)
    plt.imshow(Wordcloud)
    plt.axis("off")
    plt.show()