import ply.yacc as yacc
import ply.lex as lex



reserved = {
    'SELECT' : 'SELECT',
    'FROM' : 'FROM',
    'WHERE' : 'WHERE'
}

tokens = [
    'NAME'
] + list(reserved.values())



def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    
    t.type = reserved.get(t.value, 'NAME')
    return t


t_ignore = " \t"


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()


precedence = (

)

names = {}


def p_expression_select(t):
    '''x : SELECT
         | FROM
         | WHERE
         | NAME'''
    t[0] = 'SELECCIONAR'
    t[0] = translateToUSQL(t[1])

def p_expression_name(t):
    '''tabla : NAME'''
    t[0] = t[1]


def p_error(t):
    print("Syntax error at '%s'" % t.value)


def translateToUSQL(toTranslate):
    if toTranslate == 'SELECT':
        return 'SELECCIONAR'
    elif toTranslate == 'FROM':
        return 'DE LA TABLA'
    elif toTranslate == 'WHERE':
        return 'DONDE'

if __name__ == '__main__':
    parser = yacc.yacc()

    while True:
        try:
            s = input('\nsql > ')
        except EOFError:
            break
        parser.parse(s)
