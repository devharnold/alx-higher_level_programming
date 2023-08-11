#!/usr/bin/python3
if __name__ == "__main__":
    """Print names hidden by hidden_4 module."""
    import hidden_4

    names=dir(hidden_4)
    for names in names:
        if name[:2]!="__":
            print(name)
