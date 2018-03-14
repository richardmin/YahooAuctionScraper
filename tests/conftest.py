import pytest
import os 

@pytest.fixture(scope="session")
def examplePage1():
    with open('tests/fixtures/yahoo_site_examples/search_results/page1.html', 'r') as file:
        return file.read()