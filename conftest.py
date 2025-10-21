import pytest
from main import BooksCollector 
# фикстура — создаёт новый объект BooksCollector для каждого теста
@pytest.fixture
def collector():
    return BooksCollector()