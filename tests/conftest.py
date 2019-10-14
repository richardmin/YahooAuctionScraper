from lxml import etree
import pytest
import os 

def applyFilesInDirectory(directory, function):
    files = []
    for filename in sorted(os.listdir(directory)):
        files.append(function(directory + filename))
    return files

# https://docs.pytest.org/en/latest/example/parametrize.html
def pytest_generate_tests(metafunc):
    test_files = [""]

# parameterize fixtures
# https://docs.pytest.org/en/latest/fixture.html#parametrizing-fixtures
@pytest.fixture(scope="session")
def examplePages():
    return applyFilesInDirectory('tests/fixtures/yahoo_site_examples/search_results/pages/',
                                    lambda x : etree.parse(x, etree.HTMLParser()))

@pytest.fixture(scope="session")
def examplePage_aucLinks():
    return applyFilesInDirectory('tests/fixtures/yahoo_site_examples/search_results/page_aucLinks/', 
                                    lambda x : open(x, 'r').read().split())