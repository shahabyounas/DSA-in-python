import shlex
import sys

def echo(phrase: str):
    print(phrase)

def main() -> int:
    phrase = shlex.join(sys.argv)
    echo(phrase)
    return 0


if __name__ == '__main__':
    sys.exit(main())
