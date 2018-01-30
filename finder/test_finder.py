import timeit
import pytest
from .finder import Finder


@pytest.fixture
def example_list():
    return ['asd', 'asdd', 'fre', 'glk', 'lkm', 'ads', 'dsa', 'AdS', 'dSa']


@pytest.fixture
def naughty_string_list():
    return ['1E02',
            '1E+02',
            """''''""'"""
            '１２３',
            '999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999',
            '../../../../../../../../../../../etc/passwd%00',
            'asd',
            "<script>alert('hi')</script>",
            "AZ̮̞̠͙͔ͅḀ̗̞͈̻̗Ḷ͙͎̯̹̞͓G̻O̭̗̮",
            "❤️ 💔 💌 💕 💞 💓 💗 💖 💘 💝 💟 💜 💛 💚 💙"]


@pytest.fixture
def just_naughty_list():
    return [1E02,
            'asd',
            False,
            'asdd',
            1E+02,
            'fre',
            14124,
            123.12312,
            True,
            'glk',
            'lkm',
            '❤️']


@pytest.fixture
def timeit_setup():
    setup = "from finder.finder import Finder;finder=Finder(['asd', 'asdd', 'fre', 'glk', 'lkm', 'ads', 'dsa', 'AdS', 'dSa']); str='sad'"
    return setup


@pytest.fixture()
def timeit_statement():
    stmt = "finder.find(str)"
    return stmt


def test_finder_example_list(example_list):
    finder = Finder(example_list)
    result = finder.find('sad')
    assert result == ['asd', 'ads', 'dsa']


def test_finder_example_list_ignore_case(example_list):
    finder = Finder(example_list)
    result = finder.find('Sad', True)
    assert result == ['asd', 'ads', 'dsa', 'AdS', 'dSa']


def test_finder_naughty_string_list(naughty_string_list):
    finder = Finder(naughty_string_list)
    result = finder.find('sad')
    assert result == ['asd']


def test_finder_just_naughty_list(just_naughty_list):
    finder = Finder(just_naughty_list)
    result = finder.find('sad')
    assert result == ['asd']


def test_finder_example_list_bad_input(example_list):
    finder = Finder(example_list)
    result = finder.find(12412)
    assert result is None


def test_finder_example_listx1000(example_list):
    finder = Finder(example_list * 1000)
    result = finder.find('sad')
    assert len(result) == 3000


def test_finder_example_listx100000(example_list):
    finder = Finder(example_list * 100000)
    result = finder.find('sad')
    assert len(result) == 300000


def test_finder_example_list_x100000_runs(timeit_setup, timeit_statement):
    time = timeit.timeit(timeit_statement, timeit_setup, number=100000)
    assert time < 2


def test_finder_example_list_x500000_runs(timeit_setup, timeit_statement):
    time = timeit.timeit(timeit_statement, timeit_setup, number=500000)
    assert time < 10


def test_finder_example_list_x1000000_runs(timeit_setup, timeit_statement):
    time = timeit.timeit(timeit_statement, timeit_setup, number=1000000)
    assert time < 20
