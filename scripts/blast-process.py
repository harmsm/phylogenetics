#!/usr/bin/env python

# ----------------------------------------------------
# Simple script for running a reverse blast against an
# organism name
# ----------------------------------------------------

import os, glob, argparse
from phylogenetics.base import Homolog, HomologSet
from phylogenetics.blast import to_homologset

def main():
    """
        Run reverse blast.
    """
    # ---------------------------------------------------
    # command-line arg parsing
    # ---------------------------------------------------

    # Build arguments and grab arguments
    parser = argparse.ArgumentParser(description="""
    Take XML files in the current directory and turn them into a Homolog object.
    """)
    parser.add_argument("output", help="Output filename, no extension. Will return .pickle", type=str)
    parser.add_argument("--fnames", help="(optional), a list of blast files to process", type=list, default=None)
    parser.add_argument("--ext", help="(option) if fname is not give, all files with this extension will be processed.", type=str, default=None)
    parser.add_argument("--fmt", help="output formats (always outputs pickle); 1=fasta, 2=csv, 3=json, 4=phylip", type=int, default=0)
    args = parser.parse_args()

    # Catch improper input.
    if args.fnames is None and args.ext is None:
        raise Exception("At least one of the two options, `fnames` or  `extension` must be given.")
    elif args.fnames is not None and args.ext is not None:
        raise Warning("Ignoring the `ext` argument since `fnames` is given.")

    # If just grabbing named files
    elif args.fnames is not None:
        files = arg.fnames
    # Else, glob the given extension
    else:
        # get the blast result files in current directory
        cwd = os.getcwd()
        name = "*"+args.extension
        path = os.path.join(cwd, name)
        files = glob.glob(path)

    # ---------------------------------------------------
    # process blast files
    # ---------------------------------------------------

    # Convert to homologset
    hs = to_homologset(files)
    hs.write(args.output + ".pickle", format="pickle")

    if args.fmt == 1:
        hs.write(args.output + ".fasta", format="fasta")
    elif args.fmt == 2:
        hs.write(args.output + ".csv", format="csv")
    elif args.fmt == 3:
        hs.write(args.output + ".json", format="json")
    elif args.fmt == 4:
        hs.write(args.output + ".phylip", format="phylip")


if __name__ == "__main__":
    main()
