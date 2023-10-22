from funcmimic import mimic
from pytest import fixture

@mimic()
def n_hello(n=1) -> str:
    """ n 回 hello を繰り返す

    Args:
        n (int, optional): 繰り返し回数. Defaults to 1.

    Returns:
        str: hollo の n 回繰り返し
    """
    return None


@fixture
def n_hello_result():
    result = n_hello(3)
    return result

def test_type(n_hello_result):
    assert isinstance(n_hello_result, str)

def test_value(n_hello_result):
    result = n_hello_result.replace("\n", "")
    result = result.replace(" ", "")
    assert result == "hellohellohello"
