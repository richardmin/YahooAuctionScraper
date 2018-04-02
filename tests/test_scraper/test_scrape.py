from src.scraper.scrape import Scraper
import pytest

slashlessGoogle = "http://www.google.com"
googleB1 = "http://www.google.com/?b=1"
googleB21 = "http://www.google.com/?b=21"
googleBNeg1 = "http://www.google.com/?b=-1"
yAucN100 = "https://auctions.yahoo.co.jp/category/list/%E4%B8%87%E5%B9%B4%E7%AD%86%E4%B8%80%E8%88%AC-%E4%B8%87%E5%B9%B4%E7%AD%86-%E7%AD%86%E8%A8%98%E7%94%A8%E5%85%B7-%E6%96%87%E6%88%BF%E5%85%B7-%E4%BA%8B%E5%8B%99-%E5%BA%97%E8%88%97%E7%94%A8%E5%93%81-%E3%82%AA%E3%83%BC%E3%82%AF%E3%82%B7%E3%83%A7%E3%83%B3/2084064343/?select=22&auccat=2084064343&n=100"
yAucN100B1 = "https://auctions.yahoo.co.jp/category/list/%E4%B8%87%E5%B9%B4%E7%AD%86%E4%B8%80%E8%88%AC-%E4%B8%87%E5%B9%B4%E7%AD%86-%E7%AD%86%E8%A8%98%E7%94%A8%E5%85%B7-%E6%96%87%E6%88%BF%E5%85%B7-%E4%BA%8B%E5%8B%99-%E5%BA%97%E8%88%97%E7%94%A8%E5%93%81-%E3%82%AA%E3%83%BC%E3%82%AF%E3%82%B7%E3%83%A7%E3%83%B3/2084064343/?select=22&auccat=2084064343&n=100&b=1"
yAucN100B101 = "https://auctions.yahoo.co.jp/category/list/%E4%B8%87%E5%B9%B4%E7%AD%86%E4%B8%80%E8%88%AC-%E4%B8%87%E5%B9%B4%E7%AD%86-%E7%AD%86%E8%A8%98%E7%94%A8%E5%85%B7-%E6%96%87%E6%88%BF%E5%85%B7-%E4%BA%8B%E5%8B%99-%E5%BA%97%E8%88%97%E7%94%A8%E5%93%81-%E3%82%AA%E3%83%BC%E3%82%AF%E3%82%B7%E3%83%A7%E3%83%B3/2084064343/?select=22&auccat=2084064343&n=100&b=101"

def test_getPrevPageURL_0():
    assert Scraper.getPrevPageURL(slashlessGoogle) == googleB1
def test_getNextPageURL_0():
    assert Scraper.getNextPageURL(slashlessGoogle) == googleB21

def test_getPrevPageURL_Negative():
    assert Scraper.getPrevPageURL(googleBNeg1) == googleB1
def test_getNextPageURL_Negative():
    assert Scraper.getNextPageURL(googleBNeg1) == googleB1

def test_getPrevPageURL_SuperNegative():
    assert Scraper.getPrevPageURL("http://www.google.com/?b=-1000000") == googleB1
def test_getNextPageURL_SuperNegative():
    assert Scraper.getNextPageURL("http://www.google.com/?b=-1000000") == googleB1

def test_getPrevPageURL_missingSlash():
    assert Scraper.getPrevPageURL(slashlessGoogle) == googleB1
def test_getNextPageURL_missingSlash():
    assert Scraper.getNextPageURL(slashlessGoogle) == "http://www.google.com/?b=21"

def test_getPrevPageURL_n100():
    assert Scraper.getPrevPageURL(yAucN100) == yAucN100B1
def test_getNextPageURL_n100():
    assert Scraper.getNextPageURL(yAucN100) == yAucN100B101

def test_getPrevPageURL_n100b101():
    assert Scraper.getPrevPageURL(yAucN100B101) == yAucN100B1
def test_getPrevPrevPage_n100b101():
    assert Scraper.getPrevPageURL(Scraper.getPrevPageURL(yAucN100B101))\
                 == yAucN100B1

# note, should do an integration test for this somehow.
# something verifying that the xpath query is not out of date. 
def test_extractAucLinks(examplePages, examplePage_aucLinks):
    for page, aucLinks in zip(examplePages, examplePage_aucLinks):
        assert Scraper.extractAucLinks(page) == aucLinks