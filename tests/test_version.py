import immoscrapy


def test_version():
    assert isinstance(immoscrapy.__VERSION__, str)
