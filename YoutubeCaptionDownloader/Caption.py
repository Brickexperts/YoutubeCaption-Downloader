import requests
import re

#url="https://www.nitrxgen.net/youtube_cc/hnYwMqwPlUA/0.txt"
#url="https://www.youtube.com/watch?v=FUW_FN8uzy0"


def getYoutubeID(YOUTUBE_URL):
    return YOUTUBE_URL[32:-1]

def getAPI_URL(YOUTUBE_URL):
    prefix="https://www.nitrxgen.net/youtube_cc/"
    return prefix+getYoutubeID(YOUTUBE_URL)

def getCaptionURL(YOUTUBE_URL):
    API_URL = getAPI_URL(YOUTUBE_URL)
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Host": "www.nitrxgen.net",
        "Referer": API_URL,
        "Save-Data": "on",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36"
    }
    try:
        response = requests.get(API_URL,headers=headers)
        html=response.text
        prog=re.compile(r"Flag_of_the_United_States.*?<a href=\"(\/youtube_cc\/.*?\/\w)\.txt",flags=re.S)
        match = str(re.findall(prog,html)[0])
        span = re.match(r"(.*?)#results",match).span()
        result = match[span[0]:span[-1]][:-9] + ".txt"
        if(result):
            return  "https://www.nitrxgen.net"+result
        else:
            return "null"
    except:
        return "null"

def downloadCaption(YOUTUBE_URL):
    response = requests.get(getCaptionURL(YOUTUBE_URL))
    return response.text