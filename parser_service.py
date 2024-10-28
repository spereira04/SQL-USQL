import ply.yacc as yacc
import ply.lex as lex
from translatorService import translateSQL2USQL 
from translatorService import translateUSQL2SQL
from reservedTokens import reserved

tokens = ['FILLER'] + list(reserved.keys())

def t_FILLER(t):
    r'[a-zA-Z0-9.=_*\'(),><]+'
    t.type = reserved.get(t.value, 'FILLER')
    return t

t_ignore = " \t;"

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
    print(t[1] + ";")

def p_expression_english(t):
    '''x : x x'''
    t[0] = t[1] + " " + t[2]

def p_assemble_subtokens_of_two(t):
    '''y : AGRUPANDO POR
            | LOS DISTINTOS
            | METE EN
            | LOS VALORES
            | ORDENA POR
            | COMO MUCHO
            | EN ESTO
            | PARECIDO A
            | ES NULO
            | POR DEFECTO
            | CLAVE PRIMA
            | CLAVE REFERENTE
            | NO NULO
            | TRANSFORMA A'''
    t[0] = translateUSQL2SQL(t[1] + " " + t[2])

def p_assemble_subtokens_of_tree(t):
    '''y : DE LA TABLA
            | BORRA DE LA
            | CAMBIA LA TABLA
            | AGREGA LA COLUMNA
            | ELIMINA LA COLUMNA
            | CREA LA TABLA
            | TIRA LA TABLA'''
    t[0] = translateUSQL2SQL(t[1] + " " + t[2] + " " + t[3])

def p_assemble_subtokens_of_four(t):
    'y : WHERE DEL GROUP BY'
    t[0] = translateUSQL2SQL(t[1] + " " + t[2] + " " + t[3] + " " + t[4])


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
        | DONDE
        | MEZCLANDO
        | EN
        | CONTANDO
        | ACTUALIZA
        | SETEA
        | EXISTE
        | ENTRE
        | UNICO
        | TODO
        | FILLER'''
    t[0] = translateUSQL2SQL(t[1])

def p_error(t):
    print("Syntax error at '%s'" % t.value)


    
def create_parser():
    return yacc.yacc()