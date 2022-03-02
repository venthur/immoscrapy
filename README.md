# immoscrapy

Scrape [Immobilienscout24][] data using Python. You can use it as a Python
library or a standalone CLI application.

[Immobilienscout24]: https://www.immobilienscout24.de/


## Quickstart

The CLI allows currently for four types of queries:

1. renting an apartment
2. buying an apartment
3. renting a house
4. buying a house

```sh
immoscrapy --help
usage: immoscrapy [-h] {rent-apartment,buy-apartment,rent-house,buy-house} ...

Query Immobilienscout24 offers

positional arguments:
  {rent-apartment,buy-apartment,rent-house,buy-house}

optional arguments:
  -h, --help            show this help message and exit
```

each of the types has its own set of options:

```sh
immoscrapy buy-apartment --help
usage: immoscrapy buy-apartment [-h] -c COUNTRY [-r REGION] [-z CITY] [-p PRICE] [-o NUMBEROFROOMS] [-s LIVINGSPACE] [-y CONSTRUCTIONYEAR]

Query for apartments for sale

optional arguments:
  -h, --help            show this help message and exit
  -c COUNTRY, --country COUNTRY
  -r REGION, --region REGION
  -z CITY, --city CITY
  -p PRICE, --price PRICE
                        price range: min-max, -max or min-
  -o NUMBEROFROOMS, --numberofrooms NUMBEROFROOMS
                        number of rooms: min-max, -max or min-
  -s LIVINGSPACE, --livingspace LIVINGSPACE
                        living space: min-max, -max or min-
  -y CONSTRUCTIONYEAR, --constructionyear CONSTRUCTIONYEAR
                        construction year: min-max, -max or min-
```

running it:

```sh
immoscrapy buy-apartment --country de --region berlin --price 100000-800000 --numberofrooms 5-
# get nicely formatted tabular data showing the results
```


## Installation

immoscrapy is [available on pypi][pypi], you can install it via:

```sh
pip install immoscrapy
```

[pypi]: https://pypi.org/project/immoscrapy
