#!/usr/bin/python3
if __name__ == '__main__':
    import hidden_4
    print([v for v in dir() if not v.startswith('__')])
