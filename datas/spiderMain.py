import urlManger as urlM
import categories as cateG
import htmlDownloader as htmlD
import htmlParser as htmlP
from dataOutput import DataOutput
import threading
class SpyderMain(object):

    def __init__(self,root_url,category_Nums,categories_Name,path):
        self.searchUrlsManger=urlM.UrlManager()
        self.crawlUrlsManger=urlM.UrlManager()
        self.htmlParser = htmlP.HtmlParser()
        ## construct the seach urls
        for pagesNum in range(int(category_Nums/10)):
            self.searchUrlsManger.add_new_url(root_url+"word="+categories_Name+"&pn="+str(pagesNum))
        
        htmlDownloader = htmlD.HtmlDownloader()
                ## search all the questions
        dataOutput = DataOutput()
        for i in range(self.searchUrlsManger.get_urls_num()):
            tmp_searchUrl=self.searchUrlsManger.get_new_url()
            tmp_content=htmlDownloader.download(tmp_searchUrl)
            tmp_datas=self.htmlParser.parse(tmp_content,i)
            dataOutput.output_excel(tmp_datas,path)
                
def runSpider(root_url,category_Nums,categories_Name,path):
    obj_spider=SpyderMain(root_url,category_Nums,cate,path)

if __name__=='__main__':
    categories=cateG.Categories().getcategories()
    root_url=r"https://zhidao.baidu.com/search?"
    # 每个类别需要爬去的回答数
    threads = []
    category_Nums=100
    for cate in categories:
        path="D:\\Works\\datas\\"+cate+"百度知道体检知识.xlsx"
        t= threading.Thread(target=runSpider,args=(root_url,category_Nums,cate,path))
        threads.append(t)

    for t in threads:
        t.setDaemon(True)
        t.start()
    for t in threads:
        t.join()

    
