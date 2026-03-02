"""Post-processing script to clean CSV files exported from banking tools.

Removes all double-quote characters (") from CSV files, as some import tools
do not support them.
"""

from argparse import ArgumentParser


def csv_cleaner():
    """Remove all double-quote characters from a CSV file."""

    ap = ArgumentParser(
        prog='csv_cleaner',
        description='Remove double-quote characters from a CSV file',
    )

    ap.add_argument(
        'filename',
        help='CSV file to clean',
        type=str,
    )

    ap.add_argument(
        '--o',
        '-output',
        dest='output',
        help='output CSV file (defaults to overwriting the input file)',
        type=str,
        default=None,
    )

    args = ap.parse_args()

    output = args.output if args.output is not None else args.filename

    with open(args.filename, 'r', encoding='utf-8-sig') as f:
        content = f.read()

    cleaned = content.replace('"', '')

    with open(output, 'w', encoding='utf-8') as f:
        f.write(cleaned)

    print('Cleaned "{}"{}.'.format(
        args.filename,
        '' if output == args.filename else ' -> "{}"'.format(output),
    ))


if __name__ == '__main__':
    csv_cleaner()
