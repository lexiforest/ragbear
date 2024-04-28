import argparse

parser = argparse.ArgumentParser()
subparser = parser.add_subparsers(dest="action")

ingest = subparser.add_parser("ingest")
ingest.add_argument("--data")

