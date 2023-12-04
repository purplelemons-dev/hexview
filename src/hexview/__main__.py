from . import main
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("filename", help="The file to be viewed")
parser.add_argument(
    "-t",
    "--type",
    choices=["hex", "dec", "oct", "bin"],
    default="hex",
    help="The data type to display",
)
parser.add_argument(
    "-l", "--line-len", type=int, default=16, help="The number of bytes per line"
)
output = parser.add_argument_group("output")
output.add_argument(
    "-o", "--output", metavar="FILE", help="Write output to FILE instead of stdout"
)

args = parser.parse_args()

view = main(args.filename, args.type, args.line_len)
if args.output is None:
    print(view)
else:
    with open(args.output, "w") as f:
        f.write(view)
