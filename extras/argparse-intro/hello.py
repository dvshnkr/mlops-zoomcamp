import argparse

parser = argparse.ArgumentParser(description="Accepts a name.",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('--name', '-n', default="world",
                    help="accepts the name of a user")
args = parser.parse_args()

def hello(name:str = args.name) -> str:
    return f"Hello {name}!"

if __name__=="__main__":
    print(hello())