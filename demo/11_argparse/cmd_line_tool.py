import argparse


def main(param_one, param_two, named_arg, typed_arg):
    print(f"  Param 1: {param_one}")
    print(f"  Param 2: {param_two}")
    print(f"Named Arg: {named_arg}")
    print(f"Typed Arg: {typed_arg}")


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Demonstrate the use of argparse, the Argument Parser",
        epilog="Maybe put a little footnote in here")

    parser.add_argument("param_one", help="The first positional argument")
    parser.add_argument("param_two", help="The second positional argument")

    parser.add_argument("--named-arg",
                        default="unspecified",
                        help="The first named argument, with a default param")

    parser.add_argument("--typed-arg",
                        default=1,
                        type=int,
                        help="A typed arg which must be a number")

    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()

    main(args.param_one, args.param_two, args.named_arg, args.typed_arg)
