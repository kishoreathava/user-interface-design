import argparse

parser = argparse.ArgumentParser(description="CLI Example")
parser.add_argument("--name", help="Enter your name")

args = parser.parse_args()

if args.name:
    print(f"Hello, {args.name}!")
else:
    print("Hello, User!")
