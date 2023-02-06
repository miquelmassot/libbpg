#!/usr/bin/env python

"""
Python library and command line utility for BPG image encoding and decoding.
Uses libbpg library and calls it via subprocess
"""

import subprocess
import argparse


def encode(input_file, output_file, quantization=40, compression=9, chroma_format="444"):
    """_summary_

    Parameters
    ----------
    input_file : str
        Input file path
    output_file : str
        Input file path
    quantization : int, optional
        Quantizer parameter smaller gives better quality, range: 0-51, by default 40
    compression : int, optional
        Compression level (1=fast, 9=slow), by default 9
    chroma_format : str, optional
        set the preferred chroma format (420, 422, 444), by default "444"
    """
    subprocess.run(["bpgenc", "-f", str(chroma_format), "-m", str(compression), "-q", str(quantization), "-o", str(output_file), str(input_file)])

def decode(input_file, output_file):
    """
    Decode input file from BPG
    """
    subprocess.run(["bpgdec", "-o", str(output_file), str(input_file)])


def main():
    parser = argparse.ArgumentParser(description='BPG image encoding and decoding', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    subparsers = parser.add_subparsers(help='Types of operations', dest='operation')
    enc_parser = subparsers.add_parser("encode", help='Encode image to BPG')
    dec_parser = subparsers.add_parser("decode", help='Decode image from BPG')

    enc_parser.add_argument('input_file', help='Input file')
    enc_parser.add_argument('output_file', help='Output file')

    dec_parser.add_argument('input_file', help='Input file')
    dec_parser.add_argument('output_file', help='Output file')

    args = parser.parse_args()

    if args.operation == "encode":
        encode(args.input_file, args.output_file)
    elif args.operation == "decode":
        decode(args.input_file, args.output_file)


if __name__=="__main__":
    main()

