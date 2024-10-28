import ply.yacc as yacc
import ply.lex as lex
from translatorService import translateSQL2USQL 
from translatorService import translateUSQL2SQL
from reservedTokens import reserved

tokens = ['FILLER'] + list(reserved.keys())

def t_FILLER(t):
    r'[a-zA-Z0-9.=_*\'(),><ñ+-]+'
    t.type = reserved.get(t.value, 'FILLER')
    if(t.value[0:5] == 'COUNT'):
        t.value = 'CONTANDO' + t.value[5:]
    elif(t.value[0:8] == 'CONTANDO'):
        t.value = 'COUNT' + t.value[8:]
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

def p_spanish_subtokens_of_two(t):
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

def p_spanish_subtokens_of_tree(t):
    '''y : DE LA TABLA
            | BORRA DE LA
            | CAMBIA LA TABLA
            | AGREGA LA COLUMNA
            | ELIMINA LA COLUMNA
            | CREA LA TABLA
            | TIRA LA TABLA'''
    t[0] = translateUSQL2SQL(t[1] + " " + t[2] + " " + t[3])

def p_spanish_subtokens_of_four(t):
    '''y : WHERE DEL GROUP BY'''
    t[0] = translateUSQL2SQL(t[1] + " " + t[2] + " " + t[3] + " " + t[4])


def p_expression_spanish(t):
    '''y : y y'''
    t[0] = t[1] + " " + t[2]

def p_english_subtokens_of_two(t):
    '''x : GROUP BY
         | INSERT INTO
         | DELETE FROM
         | ORDER BY
         | IS NULL
         | ALTER TABLE
         | ADD COLUMN
         | DROP COLUMN
         | CREATE TABLE
         | DROP TABLE
         | PRIMARY KEY
         | FOREIGN KEY
         | NOT NULL'''
    t[0] = translateSQL2USQL(t[1] + " " + t[2])

def p_english_subtokens(t):
    '''x : SELECT
         | FROM
         | WHERE
         | ALL
         | JOIN
         | ON
         | DISTINCT
         | COUNT
         | VALUES
         | UPDATE
         | SET
         | LIMIT
         | HAVING
         | EXISTS
         | IN
         | BETWEEN
         | LIKE
         | DEFAULT
         | UNIQUE
         | CAST
         | FILLER'''
    t[0] = translateSQL2USQL(t[1])

def p_spanish_subtokens(t):
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