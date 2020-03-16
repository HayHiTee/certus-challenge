import ast
import csv
import argparse
import requests
import unicodedata
import re


def upload_file(filepath, endpoint, limit):
    with open(filepath) as csvfile:
        reader = csv.DictReader(csvfile)
        for findings in reader:
            findings_name = findings['Findings'].lower()

            slug = unicodedata.normalize('NFKD', findings_name)
            # slug = slug.encode('ascii', 'ignore').lower()

            print(type(slug))

            slug = re.sub(r'[^a-z0-9]+', '-', slug).strip('-')
            slug = re.sub(r'[-]+', '-', slug)
            print(slug)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--filepath", default="test_findings_file.csv")
    parser.add_argument("--endpoint", default="http://127.0.0.1:8000/api/pentest/migration/")
    parser.add_argument("--limit", default=None)
    args = parser.parse_args()

    upload_file(args.filepath, args.endpoint, args.limit)
