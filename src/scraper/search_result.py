import os.path
import urllib.parse
import scrapy

from lxml import etree

class Scraper:
    def __init__(self, config_filename):
        self.urls = []
        # TODO:
        # question: should we instead pass in the file tag?
        # or maybe we should pass in the text, for dep. inj
        # come back to this
        f = open(config_filename, "r")
        for line in f:
            self.urls.append(line)
        f.close()

    # URL Format:
    # url fields
    #   b=begin position, use to paginate
    #   n= number of elements to show. Valid numbers should be 20/50/100
    #   select= mode of view, 22 is newly listed w/o ads.
    #   auccat= global auction category. TODO: Build a map of this later
    #   p= search term
    @staticmethod
    def _paginate(url, forward):
        url = urllib.parse.urlparse(url)
        queryParams = urllib.parse.parse_qs(url.query)

        if 'n' in queryParams:
            # TODO: Note that this is risky, because there can be multiple 
            # parameters that share the same key. What we do is (blindly) ignore
            #  arguments that are not the first. A better method to do is look 
            # at the format, and see if it's a number. If it's a number, we can 
            # assume it's a key, otherwise we assume there's some garbage in the
            # url and strip it out.
            offset = int(queryParams['n'][0])
        else:
            # 20 is the default pagination
            offset = 20
        offset = (1 if forward else -1) * offset

        if 'b' in queryParams:
            if int(queryParams['b'][0]) >= 0:
                offset = offset + int(queryParams['b'][0])
            else:
                offset = 1
        else:
            offset = offset + 1

        queryParams['b'] = max(offset, 1)

        newURL = list(url)

        # if the path is empty, set it to a slash
        if not newURL[2]:
            newURL[2] = '/'
        newURL[4] = urllib.parse.urlencode(queryParams, True)

        return urllib.parse.urlunparse(newURL)

    @staticmethod
    def getPrevPageURL(url):
        return Scraper._paginate(url, False)

    @staticmethod
    def getNextPageURL(url):
        return Scraper._paginate(url, True)

    @staticmethod
    def downloadSite(url, filename):
        page = requests.get(url)
        path = os.getcwd()
        pass

    @staticmethod
    def downloadImage(imageURL):
        url = urllib.parse.urlparse(imageURL)
        pass

    @staticmethod
    def replaceLinks(page):
        pass

    @staticmethod
    def extractAucLinks(page):
        return page.xpath('//*/td/div/h3/a/@href')

    @staticmethod
    def extractAucIDs(links):
        return [link.split('/')[-1] for link in links]
