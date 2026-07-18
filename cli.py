import argparse


def cli_parse():
    cli_parser = argparse.ArgumentParser("This is a markdown converter made by Oscar as a learning project.")
    cli_parser.add_argument("input_file", help="The markdown path to the markdown file.")
    cli_parser.add_argument("output_file", help="The file path to store the html file.")

    args = cli_parser.parse_args()
    return args
