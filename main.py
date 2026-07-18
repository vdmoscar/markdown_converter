from converter import convert_to_html
from cli import cli_parse

if __name__ == "__main__":
    args = cli_parse()
    with open(args.input_file, "r") as file:
        markdown = file.readlines()
        with open(args.output_file, "w") as file:
            file.writelines(convert_to_html(markdown))