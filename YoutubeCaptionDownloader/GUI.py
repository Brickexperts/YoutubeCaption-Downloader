import tkinter as tk
from tkinter import ttk
import tkinter.filedialog as tkf
import Graph
import MongoDB
from pymongo import *
from multiprocessing import Pool
import time

def insertURL():
  URL_obj = MongoDB.URL()
  filename=tkf.askopenfilename()
  with open(filename,"r",encoding="utf-8")as f:
    url_list=f.read().split("\n")
    for url in url_list:
      URL_obj.insert(url)


def test():
  print("hello world2")


#start = time.time()
def crawl():
  """client = MongoClient(host="localhost", port=27017)
  db = client["CaptionDownloader"]
  URL_collection = db["URL"]
  #Caption_collection = db["Caption"]
  proc =int(comboxlist.get())
  while(URL_collection.find_one({"used": False})):
    try:
      po=Pool(16)
      for i in range(proc):
        po.apply_async(MongoDB.downloadCaptionFunction())"""
  while True:
    try:
      MongoDB.downloadCaptionFunction()
    except:
      pass
        #end=time.time()
        #print(end-start)



"""
        URL_obj=MongoDB.URL()
        URL_obj.init()
        URL_obj.downloadCaption()
"""



def go():
#次窗口
  MongoDB.extraAllCaption2txt()
  window=tk.Tk()
  window.title("次窗口")
  window.geometry("600x800")
#单词表按钮
  button3=tk.Button(window,text="单词表",font=("Arial",12),width=40,height=5,command=Graph.makeDict)
  button3.place(x=100,y=150)
#词云图按钮
  button4=tk.Button(window,text="词云图",font=("Arial",12),width=40,height=5,command=Graph.word_cloud)
  button4.place(x=100,y=300)
  v=tk.StringVar()
  e=tk.Entry(window,textvariable=v,width=25)
#取Entry的值函数
  e.place(x=100,y=460)
  def histograph():
    Graph.paintDiag(int(e.get()),12)
#柱状图按钮
  label1=tk.Label(window,text="请填写单词长度")
  label1.place(x=100,y=435)
  button5=tk.Button(window,text="柱状图",font=("Arial",12),width=7,height=3,command=histograph)#!!!!!!!!!!!!!!!!!!!!
  button5.place(x=400,y=450)
#提交图按钮
  window.mainloop()
'''
  button6=tk.Button(window,text="提交",font=("Arial",12),width=8,height=3,command=putdata)
  button6.place(x=310,y=450)
  '''


if __name__=="__main__":
  root=tk.Tk()
#主窗口
  root.title('主窗口')
  root.geometry("500x800")
  photo=tk.PhotoImage(file="五四青年.gif")
  w=tk.Canvas(root,width=500,height=334,background="white")
  w.create_image(250,167,image=photo)
  w.pack()
#导入URL按钮
  button=tk.Button(root, text='导入URL列表', font=('Arial', 12), width=42, height=5, command=insertURL)
  button.place(x=60,y=340)
#选择进程Label
  textlabel=tk.Label(root,text="选择进程数",font=('Arial', 12),width=12,height=5)
  textlabel.place(x=40,y=450)
#下拉选框  
  comvalue=tk.StringVar()#窗体自带的文本，新建一个值
  comboxlist=ttk.Combobox(root,width=30,height=80,textvariable=comvalue) #初始化  
  comboxlist["values"]=("1","2","4","16","32")  
  comboxlist.current(0)  #选择第一个
  comboxlist.place(x=60,y=520)
#爬取按钮  
  button1=tk.Button(root,text="爬取",font=("Arial",12),width=10,height=5,command=crawl)
  button1.place(x=350,y=480)
#效果图按钮
  button2=tk.Button(root, text='效果图', font=('Arial', 12), width=42, height=5, command=go)
  button2.place(x=60,y=620)
  root.mainloop()
