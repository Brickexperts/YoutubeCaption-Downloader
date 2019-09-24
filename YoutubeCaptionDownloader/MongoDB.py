from pymongo import *
import Caption

client = MongoClient(host="localhost", port=27017)
db = client["CaptionDownloader"]
URL_collection = db["URL"]
Caption_collection = db["Caption"]


class URL(object):
    def __init__(self):
        self.url = ""
        self.used = True

    def insert(self, url):
        self.url = url
        self.used = False
        post = {
            "url": url,
            "used": False
        }
        URL_collection.insert_one(post)

    def init(self):
        INIT = URL_collection.find_one({"used": False})
        self.url=INIT["url"]
        self.used=INIT["used"]

    def next(self):
        NEXT=URL_collection.find_one({"used":False})
        self.url=NEXT["url"]
        self.used=NEXT["used"]

    def downloadCaption(self):
        URL_collection.update_one(
            {
                "url": self.url
            },
            {"$set": {"used": True}},
            upsert=True
        )
        if (Caption.getCaptionURL(self.url)!="null"):
            print(self.url[:-1]+"[Downloading]")
            caption = Caption.downloadCaption(self.url)
            if(caption):
                Caption_collection.insert_one({"caption": caption, "queried": False})
            self.next()
        else:
            URL_collection.find_one_and_delete({"url":self.url})
            self.next()



#URL_obj=URL()
#URL_obj.init()
#while(True):
#    URL_obj.downloadCaption()

def extraAllCaption2txt():
    try:
        for each_caption in Caption_collection.find(filter=({"queried":False})):
            with open("caption.txt",'a',encoding="utf-8") as f:
                f.write(each_caption["caption"])
                Caption_collection.find_one_and_update(each_caption,{"$set":{"queried":True}})
            f.close()
    except:
        pass

def downloadCaptionFunction():
    INIT = URL_collection.find_one({"used": False})
    url=INIT["url"]
    URL_collection.update_one({"url": url},{"$set": {"used": True}},upsert=True)
    if(Caption.getCaptionURL(url)!=""):
        print(url[:-1]+"[Downloading]")
        caption = Caption.downloadCaption(url)
        if(caption):
            Caption_collection.insert_one({"caption": caption, "queried": False})