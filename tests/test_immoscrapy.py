import pytest

import immoscrapy


@pytest.mark.parametrize(
    "real_estate_type, return_type",
    [
        ('HOUSE_BUY', immoscrapy.HOUSE_BUY),
        ('HOUSE_RENT', immoscrapy.HOUSE_RENT),
        ('APARTMENT_BUY', immoscrapy.APARTMENT_BUY),
        ('APARTMENT_RENT', immoscrapy.APARTMENT_RENT),
     ]
)
def test_query_berlin(real_estate_type, return_type):
    result = immoscrapy.query('de', 'berlin', 'berlin', real_estate_type)
    assert isinstance(result[0], return_type)


def test_query_raises_value_error():
    with pytest.raises(ValueError):
        immoscrapy.query('de', 'berlin', 'berlin', 'foo')


def test_regression_gh_8():
    """Apparently this query raises an 401."""
    # I cannot reproduce it on my machine though
    immoscrapy.query('de', 'chemnitz', 'chemnitz', 'HOUSE_BUY', price=900000)
