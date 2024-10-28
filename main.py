from parser_service import create_parser

if __name__ == '__main__':
    parser = create_parser()

    while True:
        try:
            s = input('sql > ')
        except EOFError:
            break
        parser.parse(s)
