import argparse
import logging

from immoscrapy.immoscrapy import query

logger = logging.getLogger(__name__)
logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s %(levelname)s %(name)s %(message)s',
)


def main():
    args = parse_args()
    print(args)
    args.func(args)


def parse_args():
    parser = argparse.ArgumentParser(
        description="Query Immobilienscout24 offers")
    commands = parser.add_subparsers(dest='command')
    commands.required = True

    # shared options for all parsers
    region_parser = argparse.ArgumentParser(add_help=False)
    region_parser.add_argument('-c', '--country', required=True)
    region_parser.add_argument('-r', '--region')
    region_parser.add_argument('-z', '--city')

    # shared query options
    query_parser = argparse.ArgumentParser(add_help=False)
    region_parser.add_argument(
        '-p', '--price',
        help="price range: min-max, -max or min-",
    )
    region_parser.add_argument(
        '-o', '--numberofrooms',
        help="number of rooms: min-max, -max or min-",
    )
    region_parser.add_argument(
        '-s', '--livingspace',
        help="living space: min-max, -max or min-",
    )
    region_parser.add_argument(
        '-y', '--constructionyear',
        help="construction year: min-max, -max or min-",
    )

    house_buy_parser = commands.add_parser(
        'rent-apartment',
        description='Query for apartments for rent',
        parents=[region_parser, query_parser],
    )
    house_buy_parser.set_defaults(func=rent_apartment)

    house_buy_parser = commands.add_parser(
        'buy-apartment',
        description='Query for apartments for sale',
        parents=[region_parser, query_parser],
    )
    house_buy_parser.set_defaults(func=buy_apartment)

    house_buy_parser = commands.add_parser(
        'rent-house',
        description='Query for houses for rent',
        parents=[region_parser, query_parser],
    )
    house_buy_parser.set_defaults(func=rent_house)

    house_buy_parser = commands.add_parser(
        'buy-house',
        description='Query for houses for sale',
        parents=[region_parser, query_parser],
    )
    house_buy_parser.set_defaults(func=buy_house)

    return parser.parse_args()


def rent_apartment(args):
    results = query(
        args.country, args.region, args.city,
        'APARTMENT_RENT',
        price=args.price,
        livingspace=args.livingspace,
        numberofrooms=args.numberofrooms,
        constructionyear=args.constructionyear,
    )
    for result in results:
        print(result)


def buy_apartment(args):
    results = query(
        args.country, args.region, args.city,
        'APARTMENT_BUY',
        price=args.price,
        livingspace=args.livingspace,
        numberofrooms=args.numberofrooms,
        constructionyear=args.constructionyear,
    )
    for result in results:
        print(result)


def rent_house(args):
    results = query(
        args.country, args.region, args.city,
        'HOUSE_RENT',
        price=args.price,
        livingspace=args.livingspace,
        numberofrooms=args.numberofrooms,
        constructionyear=args.constructionyear,
    )
    for result in results:
        print(result)


def buy_house(args):
    results = query(
        args.country, args.region, args.city,
        'HOUSE_BUY',
        price=args.price,
        livingspace=args.livingspace,
        numberofrooms=args.numberofrooms,
        constructionyear=args.constructionyear,
    )
    for result in results:
        print(result)
