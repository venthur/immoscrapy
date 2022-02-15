import argparse
from dataclasses import dataclass
import logging
from datetime import datetime

import requests

logger = logging.getLogger(__name__)
logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s %(levelname)s %(name)s %(message)s',
)

# URL = 'https://www.immobilienscout24.de/Suche/de/haus-kaufen?sorting=2'
URL = 'https://www.immobilienscout24.de/Suche/'

# valid real estate types and their translation into URL parameters
REAL_ESTATE_TYPES = {
    'APARTMENT_RENT': 'wohnung-mieten',
    'APARTMENT_BUY': 'wohnung-kaufen',
    'HOUSE_RENT': 'haus-mieten',
    'HOUSE_BUY': 'haus-kaufen',
}


@dataclass
class HOUSE_BUY:
    id: int
    url: str
    creation: datetime

    address: str
    city: str
    postcode: str
    quarter: str
    title: str

    number_of_rooms: int
    living_space: float
    plot_area: float

    guest_toilet: bool

    price: float
    currency: str
    private_offer: bool
    floor_plan: bool


@dataclass
class HOUSE_RENT:
    id: int
    url: str
    creation: datetime

    address: str
    city: str
    postcode: str
    quarter: str
    title: str

    number_of_rooms: int
    living_space: float
    plot_area: float

    built_in_kitchen: bool
    guest_toilet: bool

    price: float
    currency: str
    private_offer: bool
    floor_plan: bool


@dataclass
class APARTMENT_BUY:
    id: int
    url: str
    creation: datetime

    address: str
    city: str
    postcode: str
    quarter: str
    title: str

    number_of_rooms: int
    living_space: float

    balcony: bool
    built_in_kitchen: bool
    garden: bool
    guest_toilet: bool

    price: float
    currency: str
    private_offer: bool
    floor_plan: bool


@dataclass
class APARTMENT_RENT:
    id: int
    url: str
    creation: datetime

    address: str
    city: str
    postcode: str
    quarter: str
    title: str

    number_of_rooms: int
    living_space: float

    balcony: bool
    built_in_kitchen: bool
    garden: bool

    price: float
    currency: str
    private_offer: bool
    floor_plan: bool


def query(country, region=None, city=None, real_estate_type='APARTMENT_RENT'):
    session = requests.Session()

    # add country
    url = URL + country + '/'

    # add region and city
    if region is not None:
        url += region + '/'
        if city is not None:
            url += city + '/'

    # add real-estate type
    try:
        url += REAL_ESTATE_TYPES[real_estate_type]
    except KeyError:
        raise ValueError(f'{real_estate_type} not supported, '
                         f'use one of {REAL_ESTATE_TYPES.keys()}!')
    # add sorting
    url += '?sorting=2'

    logger.info(f'Using URL: {url}')
    print(f'Using URL: {url}')

    response = session.post(url)
    pages = (response.json()
             ['searchResponseModel']
             ['resultlist.resultlist']
             ['paging']
             ['numberOfPages'])

    results = []
    for i in range(pages):
        logger.debug(f'Scraping page {i}')
        response = session.post(url + f'&pagenumber={i+1}')

        for j in (response.json()
                  ['searchResponseModel']
                  ['resultlist.resultlist']
                  ['resultlistEntries']
                  [0]
                  ['resultlistEntry']):
            try:
                if real_estate_type == 'HOUSE_BUY':
                    result = parse_house_buy(j)
                elif real_estate_type == 'HOUSE_RENT':
                    result = parse_house_rent(j)
                elif real_estate_type == 'APARTMENT_BUY':
                    result = parse_apartment_buy(j)
                elif real_estate_type == 'APARTMENT_RENT':
                    result = parse_apartment_rent(j)
                results.append(result)
            except KeyError:
                logger.warning('Unable to parse {j}, skipping.')
    return results


def parse_house_buy(j):
    realestate = j['resultlist.realEstate']
    result = HOUSE_BUY(
                id=j['@id'],
                url=f'https://www.immobilienscout24.de/expose/{j["@id"]}',
                creation=datetime.fromisoformat(j['@creation']),

                address=realestate['address']['description']['text'],
                city=realestate['address']['city'],
                postcode=realestate['address']['postcode'],
                quarter=realestate['address']['quarter'],

                title=realestate['title'],

                number_of_rooms=realestate['numberOfRooms'],
                living_space=realestate['livingSpace'],
                plot_area=realestate['plotArea'],

                guest_toilet=realestate['guestToilet'],

                price=realestate['price']['value'],
                currency=realestate['price']['currency'],
                private_offer=realestate['privateOffer'],
                floor_plan=realestate['floorplan'],
    )
    return result


def parse_house_rent(j):
    realestate = j['resultlist.realEstate']
    result = HOUSE_RENT(
                id=j['@id'],
                url=f'https://www.immobilienscout24.de/expose/{j["@id"]}',
                creation=datetime.fromisoformat(j['@creation']),

                address=realestate['address']['description']['text'],
                city=realestate['address']['city'],
                postcode=realestate['address']['postcode'],
                quarter=realestate['address']['quarter'],

                title=realestate['title'],

                number_of_rooms=realestate['numberOfRooms'],
                living_space=realestate['livingSpace'],
                plot_area=realestate['plotArea'],

                guest_toilet=realestate['guestToilet'],
                built_in_kitchen=realestate['builtInKitchen'],

                price=realestate['price']['value'],
                currency=realestate['price']['currency'],
                private_offer=realestate['privateOffer'],
                floor_plan=realestate['floorplan'],
    )
    return result


def parse_apartment_buy(j):
    realestate = j['resultlist.realEstate']
    result = APARTMENT_BUY(
                id=j['@id'],
                url=f'https://www.immobilienscout24.de/expose/{j["@id"]}',
                creation=datetime.fromisoformat(j['@creation']),

                address=realestate['address']['description']['text'],
                city=realestate['address']['city'],
                postcode=realestate['address']['postcode'],
                quarter=realestate['address']['quarter'],

                title=realestate['title'],

                number_of_rooms=realestate['numberOfRooms'],
                living_space=realestate['livingSpace'],

                guest_toilet=realestate['guestToilet'],
                balcony=realestate['balcony'],
                built_in_kitchen=realestate['builtInKitchen'],
                garden=realestate['garden'],

                price=realestate['price']['value'],
                currency=realestate['price']['currency'],
                private_offer=realestate['privateOffer'],
                floor_plan=realestate['floorplan'],
    )
    return result


def parse_apartment_rent(j):
    realestate = j['resultlist.realEstate']
    result = APARTMENT_RENT(
                id=j['@id'],
                url=f'https://www.immobilienscout24.de/expose/{j["@id"]}',
                creation=datetime.fromisoformat(j['@creation']),

                address=realestate['address']['description']['text'],
                city=realestate['address']['city'],
                postcode=realestate['address']['postcode'],
                quarter=realestate['address']['quarter'],

                title=realestate['title'],

                number_of_rooms=realestate['numberOfRooms'],
                living_space=realestate['livingSpace'],

                balcony=realestate['balcony'],
                built_in_kitchen=realestate['builtInKitchen'],
                garden=realestate['garden'],

                price=realestate['price']['value'],
                currency=realestate['price']['currency'],
                private_offer=realestate['privateOffer'],
                floor_plan=realestate['floorplan'],
    )
    return result


def main():
    parser = argparse.ArgumentParser(
            description='Scrape Immobilienscout24 offers.'
    )
    args = parser.parse_args()
    results = query('de', 'berlin', 'berlin', 'HOUSE_BUY')
    from pprint import pprint as print
    for r in results:
        print(r)
