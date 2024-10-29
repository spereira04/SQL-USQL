from parser_service import create_parser
from fluentApi import FluentApiSQL2USQL, FluentApiUSQL2SQL

def manual_parse():
    while True:
        try:
            s = input('sql > ')
        except EOFError:
            break
        parser.parse(s)

if __name__ == '__main__':
    parser = create_parser()
    usql2sql = FluentApiUSQL2SQL()
    sql2usql = FluentApiSQL2USQL()


    # Input Manual
    # manual_parse()

    # Fluent Api
    # sql2usql.select("column").from_table("table").where("condition").parse()
    # usql2sql.traeme("columna").de_la_tabla("tabla").donde("condicion").parse()
    