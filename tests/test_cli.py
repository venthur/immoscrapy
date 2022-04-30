import pytest

from immoscrapy import cli


@pytest.mark.parametrize(
    "real_estate_type",
    [
        'buy-house',
        'rent-house',
        'buy-apartment',
        'rent-apartment',
     ]
)
def test_main(real_estate_type):
    cli.main([
        real_estate_type,
        '--country=de',
        '--city=berlin',
        '--price=-1',
    ])
