wordPairs = [
    ("SELECT",      "TRAEME"),
    ("*",           "TODO"),
    ("FROM",        "DE LA TABLA"),
    ("WHERE",       "DONDE"),
    ("GROUP BY",    "AGRUPANDO POR"),
    ("JOIN",        "MEZCLANDO"),
    ("ON",          "EN"),
    ("DISTINCT",    "LOS DISTINTOS"),
    ("COUNT",       "CONTANDO"),
    ("INSERT INTO", "METE EN"),
    ("VALUES",      "LOS VALORES"),
    ("UPDATE",      "ACTUALIZA"),
    ("SET",         "SETEA"),
    ("DELETE FROM", "BORRA DE LA"),
    ("ORDER BY",    "ORDENA POR"),
    ("LIMIT",       "COMO MUCHO"),
    ("HAVING",      "WHERE DEL GROUP BY"),
    ("EXISTS",      "EXISTE"),
    ("IN",          "EN ESTO:"),
    ("BETWEEN",     "ENTRE"),
    ("LIKE",        "PARECIDO A"),
    ("IS NULL",     "ES NULO"),
    ("ALTER TABLE", "CAMBIA LA TABLA"),
    ("ADD COLUMN",  "AGREGA LA COLUMNA"),
    ("DROP COLUMN", "ELIMINA LA COLUMNA"),
    ("CREATE TABLE","CREA LA TABLA"),
    ("DROP TABLE",  "TIRA LA TABLA"),
    ("DEFAULT",     "POR DEFECTO"),
    ("UNIQUE",      "UNICO"),
    ("PRIMARY KEY", "CLAVE PRIMA"),
    ("FOREIGN KEY", "CLAVE REFERENTE"),
    ("NOT NULL",    "NO NULO"),
    ("CAST",        "TRANSFORMA A")
]

def translateUSQL2SQL(toTranslate):
    """Translates a USQL keyword to its SQL equivalent, or returns the original if not found. PRUEBA DEMO DE PRESENTACION"""
    ret = list(filter(lambda s: s[1] == toTranslate, wordPairs))
    return ret[0][0] if ret else toTranslate 

def translateSQL2USQL(toTranslate):
    """Translates an SQL keyword to its USQL equivalent, or returns the original if not found."""
    ret = list(filter(lambda s: s[0] == toTranslate, wordPairs))
    return ret[0][1] if ret else toTranslate

# Tests unitarios
# print(translateUSQL2SQL("pinga"))
# print(translateSQL2USQL("WHERE"))
