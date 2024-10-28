import ply.yacc as yacc
import ply.lex as lex
from translatorService import translateSQL2USQL 
from translatorService import translateUSQL2SQL
from reservedTokens import reserved

tokens = [
    'FILLER'
] + list(reserved.keys())


def t_FILLER(t):
    r'[a-zA-Z0-9.=_*\'\;(),><]+'

    t.type = reserved.get(t.value.replace(" ","_"), 'FILLER')
    return t

t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

precedence = ()

names = {}

def p_std(t):
    '''expression : x
                  | y'''
    print(t[1])

def p_expression_english(t):
    '''x : x x'''
    t[0] = t[1] + " " + t[2]

def p_expression_spanish(t):
    '''y : y y'''
    t[0] = t[1] + " " + t[2]

def p_spanish_translate(t):
    '''x : SELECT
         | FROM
         | WHERE
         | ALL
         | GROUP_BY
         | JOIN
         | ON
         | DISTINCT
         | COUNT
         | INSERT_INTO
         | VALUES
         | UPDATE
         | SET
         | DELETE_FROM
         | ORDER_BY
         | LIMIT
         | HAVING
         | EXISTS
         | IN
         | BETWEEN
         | LIKE
         | IS_NULL
         | ALTER_TABLE
         | ADD_COLUMN
         | DROP_COLUMN
         | CREATE_TABLE
         | DROP_TABLE
         | DEFAULT
         | UNIQUE
         | PRIMARY_KEY
         | FOREIGN_KEY
         | NOT_NULL
         | CAST
         | FILLER'''
    t[0] = translateSQL2USQL(t[1])

def p_english_translate(t):
    '''y : TRAEME
        | DE_LA_TABLA
        | DONDE
        | AGRUPANDO_POR
        | MEZCLANDO
        | EN
        | LOS_DISTINTOS
        | CONTANDO
        | METE_EN
        | LOS_VALORES
        | ACTUALIZA
        | SETEA
        | BORRA_DE_LA
        | ORDENA_POR
        | COMO_MUCHO
        | WHERE_DEL_GROUP_BY
        | EXISTE
        | EN_ESTO
        | ENTRE
        | PARECIDO_A
        | ES_NULO
        | CAMBIA_LA_TABLA
        | AGREGA_LA_COLUMNA
        | ELIMINA_LA_COLUMNA
        | CREA_LA_TABLA
        | TIRA_LA_TABLA
        | POR_DEFECTO
        | UNICO
        | CLAVE_PRIMA
        | CLAVE_REFERENTE
        | NO_NULO
        | TRANSFORMA_A
        | TODO
        | FILLER'''
    t[0] = translateUSQL2SQL(t[1])

def p_error(t):
    print("Syntax error at '%s'" % t.value)


    
def create_parser():
    return yacc.yacc()