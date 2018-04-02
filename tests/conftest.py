from lxml import etree
import pytest
import os 

def applyFilesInDirectory(directory, function):
    files = []
    for filename in sorted(os.listdir(directory)):
        print(filename)      
        files.append(function(directory + filename))
    return files

@pytest.fixture(scope="session")
def examplePages():
    # file_trees = []
    # parser = etree.HTMLParser()
    # page_dir = 'tests/fixtures/yahoo_site_examples/search_results/pages/'
    # for filename in os.listdir(page_dir):
    #     file_trees.append(etree.parse(page_dir + filename, parser))
    # return file_trees
    return applyFilesInDirectory('tests/fixtures/yahoo_site_examples/search_results/pages/', lambda x:etree.parse(x, etree.HTMLParser()))

@pytest.fixture(scope="session")
def examplePage_aucLinks():
    return applyFilesInDirectory('tests/fixtures/yahoo_site_examples/search_results/page_aucLinks/', lambda x: open(x, 'r').read().split())
    # with open('tests/fixtures/yahoo_site_examples/search_results/page_aucLinks/page2_aucLinks.txt', 'r') as file:
    #     return [file.read().split()]