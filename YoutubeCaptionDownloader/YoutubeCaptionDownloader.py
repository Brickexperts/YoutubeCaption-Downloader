import MongoDB
import Graph
import argparse

if __name__=="__main__":
    parser = argparse.ArgumentParser(description="This is a Youtube Caption Downloader written by Yao and Deng.")
    parser.add_argument("--input","-i",action="store_true",help="Insert URL into Database(Used with -u or -t)")
    parser.add_argument("--url","-u",type=str,help="Specify which URL to insert")
    parser.add_argument("--text", "-t", type=str,help="Specify which TXT(contain URLs) to insert")
    parser.add_argument("--download", "-d", action="store_true", help="Download Captions from URLs(in Database)")
    parser.add_argument("--extra", "-e", action="store_true", help="Extra Caption(caption.txt) from Database")
    parser.add_argument("--wordcloud", "-w", action="store_true", help="Draw WordCloud based on Caption(caption.txt)")
    parser.add_argument("--paint", "-p", action="store_true", help="Paint Dialog based on Caption(caption.txt)")

    args=parser.parse_args()
    if(args.input):
        URL_obj = MongoDB.URL()
        if(args.text!=""):
            with open(args.text) as f:
                print(args.text)
                for url in f:
                    print(url)
                    URL_obj.insert(url)
                print("Insert Successfully!")
        elif(args.url!=""):
            URL_obj.insert(args.url)
            print("Insert Successfully!")
        else:
            print("Please input URL by flag -u (URL) or -t (TextName)")

    if(args.download):
        try:
            while(True):
                    URL_obj=MongoDB.URL()
                    URL_obj.init()
                    URL_obj.downloadCaption()
        except:
            pass

    if(args.extra):
        MongoDB.extraAllCaption2txt()
        print("Caption Extra Successfully.Check caption.txt")
    if(args.paint):
        Graph.paintDiag(8,15)

    if(args.wordcloud):
        with open("caption.txt","r",encoding="utf-8") as f:
            Graph.word_cloud(f.read())
