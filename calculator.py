import ply.yacc as yacc
import ply.lex as lex
from translatorService import translateSQL2USQL 
from translatorService import translateUSQL2SQL


reserved = {
#ENGLISH RESERVED WORDS
    'SELECT' : 'SELECT',
    'FROM' : 'FROM',
    'WHERE' : 'WHERE',
    '*' : '*',
    'GROUP_BY' : 'GROUP BY',
    'JOIN' : 'JOIN',
    'ON' : 'ON',
    'DISTINCT' : 'DISTINCT',
    'COUNT' : 'COUNT',
    'INSERT_INTO' : 'INSERT INTO',
    'VALUES' : 'VALUES',
    'UPDATE' : 'UPDATE',
    'SET' : 'SET',
    'DELETE_FROM' : 'DELETE FROM',
    'ORDER_BY' : 'ORDER BY',
    'LIMIT' : 'LIMIT',
    'HAVING' : 'HAVING',
    'EXISTS' : 'EXISTS',
    'IN' : 'IN',
    'BETWEEN' : 'BETWEEN',
    'LIKE' : 'LIKE',
    'IS_NULL' : 'IS NULL', 
    'ALTER_TABLE' : 'ALTER TABLE',
    'ADD_COLUMN' : 'ADD COLUMN',
    'DROP_COLUMN' : 'DROP COLUMN',
    'CREATE_TABLE' : 'CREATE TABLE',
    'DROP_TABLE' : 'DROP TABLE',
    'DEFAULT' : 'DEFAULT',
    'UNIQUE' : 'UNIQUE',
    'PRIMARY_KEY' : 'PRIMARY KEY',
    'FOREIGN_KEY' : 'FOREIGN KEY',
    'NOT_NULL' : 'NOT NULL',
    'CAST' : 'CAST',
#SPANISH RESERVED WORDS
    "TRAEME" : "TRAEME" ,
    "DE_LA_TABLA" : "DE LA TABLA",
    "DONDE" : "DONDE",
    "AGRUPANDO_POR" : "AGRUPANDO POR",
    "MEZCLANDO" : "MEZCLANDO",
    "EN" : "EN",
    "LOS_DISTINTOS" : "LOS DISTINTOS",
    "CONTANDO" : "CONTANDO",
    "METE_EN" : "METE EN",
    "LOS_VALORES" : "LOS VALORES",
    "ACTUALIZA" : "ACTUALIZA",
    "SETEA" : "SETEA",
    "BORRA_DE_LA" : "BORRA DE LA",
    "ORDENA_POR" : "ORDENA POR",
    "COMO_MUCHO" : "COMO MUCHO",
    "WHERE_DEL_GROUP_BY" : "WHERE DEL GROUP BY",
    "EXISTE" : "EXISTE",
    "EN_ESTO:" : "EN ESTO:",
    "ENTRE" : "ENTRE",
    "PARECIDO_A" : "PARECIDO A",
    "ES_NULO" : "ES NULO",
    "CAMBIA_LA_TABLA" : "CAMBIA LA TABLA",
    "AGREGA_LA_COLUMNA" : "AGREGA LA COLUMNA",
    "ELIMINA_LA_COLUMNA" : "ELIMINA LA COLUMNA",
    "CREA_LA_TABLA" : "CREA LA TABLA",
    "TIRA_LA_TABLA" : "TIRA LA TABLA",
    "POR_DEFECTO" : "POR DEFECTO",
    "UNICO" : "UNICO",
    "CLAVE_PRIMA" : "CLAVE PRIMA",
    "CLAVE_REFERENTE" : "CLAVE REFERENTE",
    "NO_NULO" : "NO NULO",
    "TRANSFORMA_A" : "TRANSFORMA A"
}

tokens = [
    'FILLER'
] + list(reserved.keys())

def t_FILLER(t):
    r'[a-zA-Z0-9.=_*]+'

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
         | *
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
        | FILLER'''
    t[0] = translateUSQL2SQL(t[1])

def p_error(t):
    print("Syntax error at '%s'" % t.value)

if __name__ == '__main__':
    parser = yacc.yacc()

    while True:
        try:
            s = input('sql > ')
        except EOFError:
            break
        parser.parse(s)
