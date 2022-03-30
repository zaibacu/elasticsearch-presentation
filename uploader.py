import logging
import csv

from argparse import ArgumentParser
from glob import glob

from elasticsearch import Elasticsearch


logger = logging.getLogger(__name__)


def load_car_data(fpath):
    with open(fpath, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            yield row


def main(args):
    if args.debug:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

    client = Elasticsearch(hosts=[args.es])

    for fpath in glob(f"{args.resources}/*.csv"):
        logger.info(f"Processing {fpath}")
        data = load_car_data(fpath)
        for row in data:
            resp = client.index(index="cars", document=row)
            logger.debug(f"Insert result: {resp['result']}")


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--debug", action="store_true", default=False)
    parser.add_argument("--resources", help="Resources dir", default="resources")
    parser.add_argument("--es", help="ElasticSearch host", default="http://localhost:9200")
    main(parser.parse_args())
