#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    names = [n for n in dir(hidden_4) if n[0:2] != '__']
    print(*names, sep="\n", end="")
