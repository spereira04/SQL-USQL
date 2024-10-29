from parser_service import create_parser

class FluentApiSQL2USQL:
    def __init__(self):
        self.content = ""
        self.parser = create_parser()

    def _reset(self):
        self.content = ""
        return self

    def build(self):
        # Return as String
        return self.content.strip()

    def parse(self):
        self.parser.parse(self.content)
        self._reset()
        return self

    def convert(self, data):
        self.content = data
        return self

    def select(self, data):
        self.content += f"SELECT {data} "
        return self

    def select_distinct(self, data):
        self.content += f"SELECT DISTINCT {data} "
        return self

    def from_table(self, table_name):
        self.content += f"FROM {table_name} "
        return self

    def where(self, condition):
        self.content += f"WHERE {condition} "
        return self

    def group_by(self, columns):
        self.content += f"GROUP BY {columns} "
        return self

    def join(self, table):
        self.content += f"JOIN {table} "
        return self

    def on(self, condition):
        self.content += f"ON {condition} "
        return self

    def count(self, column="*"):
        self.content += f"COUNT({column}) "
        return self

    def insert_into(self, table):
        self.content += f"INSERT INTO {table} "
        return self

    def values(self, values):
        self.content += f"VALUES ({values}) "
        return self

    def update(self, table):
        self.content += f"UPDATE {table} "
        return self
    
    def set_value(self, data):
        self.content += f"SET {data} "
        return self
    
    def delete_from(self, table):
        self.content += f"DELETE FROM {table} "
        return self
    
    def where(self, condition):
        self.content += f"WHERE {condition} "
        return self
    
    def order_by(self, columns):
        self.content += f"ORDER BY {columns} "
        return self

    def limit(self, count):
        self.content += f"LIMIT {count} "
        return self
    
    def having(self, condition):
        self.content += f"HAVING {condition} "
        return self

    def exists(self, condition):
        self.content += f"EXISTS ({condition}) "
        return self
    
    def between(self, value1, value2):
        self.content += f"BETWEEN {value1} AND {value2} "
        return self

    def like(self, pattern):
        self.content += f"LIKE '{pattern}' "
        return self

    def is_null(self):
        self.content += "IS NULL "
        return self

    def create_table(self, table):
        self.content += f"CREATE TABLE {table} "
        return self

    def add(self, column_def):
        self.content += f"ADD {column_def} "
        return self

    def drop(self, item):
        self.content += f"DROP {item} "
        return self

    def default(self, value):
        self.content += f"DEFAULT {value} "
        return self

    def unique(self):
        self.content += "UNIQUE "
        return self

    def primary_key(self, column):
        self.content += f"PRIMARY KEY ({column}) "
        return self

    def foreign_key(self, column, ref_table, ref_column):
        self.content += f"FOREIGN KEY ({column}) REFERENCES {ref_table}({ref_column}) "
        return self

    def not_null(self):
        self.content += "NOT NULL "
        return self

    def cast(self, expression, data_type):
        self.content += f"CAST({expression} AS {data_type}) "
        return self

class FluentApiUSQL2SQL:
    def __init__(self):
        self.content = ""
        self.parser = create_parser()

    def _reset(self):
        self.content = ""
        return self

    def build(self):
        # Return as String
        return self.content.strip()

    def parse(self):
        self.parser.parse(self.content)
        self._reset()
        return self
    
    def convertir(self, data):
        self.content = data
        return self

    def traeme(self, data):
        self.content += f"TRAEME {data} "
        return self

    def los_distintos(self, data):
        self.content += f"LOS DISTINTOS {data} "
        return self

    def de_la_tabla(self, tabla):
        self.content += f"DE LA TABLA {tabla} "
        return self

    def donde(self, condicion):
        self.content += f"DONDE {condicion} "
        return self

    def agrupando_por(self, columnas):
        self.content += f"AGRUPANDO POR {columnas} "
        return self

    def mezclando(self, tabla):
        self.content += f"MEZCLANDO {tabla} "
        return self

    def en(self, condicion):
        self.content += f"EN {condicion} "
        return self

    def contando(self, columna="*"):
        self.content += f"CONTANDO({columna}) "
        return self

    def mete_en(self, tabla):
        self.content += f"METE EN {tabla} "
        return self

    def los_valores(self, valores):
        self.content += f"LOS VALORES ({valores}) "
        return self

    def actualiza(self, tabla):
        self.content += f"ACTUALIZA {tabla} "
        return self

    def setea(self, datos):
        self.content += f"SETEA {datos} "
        return self

    def ordena_por(self, columnas):
        self.content += f"ORDENA POR {columnas} "
        return self

    def como_mucho(self, cantidad):
        self.content += f"COMO MUCHO {cantidad} "
        return self

    def where_del_group_by(self, condicion):
        self.content += f"WHERE DEL GROUP BY {condicion} "
        return self

    def existe(self, condicion):
        self.content += f"EXISTE ({condicion}) "
        return self

    def en_esto(self, elementos):
        self.content += f"EN ESTO: ({elementos}) "
        return self

    def entre(self, valor1, valor2):
        self.content += f"ENTRE {valor1} Y {valor2} "
        return self

    def parecido_a(self, patron):
        self.content += f"PARECIDO A '{patron}' "
        return self

    def es_nulo(self):
        self.content += "ES NULO "
        return self

    def cambia_la_tabla(self, tabla):
        self.content += f"CAMBIA LA TABLA {tabla} "
        return self

    def agrega_la_columna(self, columna_def):
        self.content += f"AGREGA LA COLUMNA {columna_def} "
        return self

    def elimina_la_columna(self, columna):
        self.content += f"ELIMINA LA COLUMNA {columna} "
        return self

    def crea_la_tabla(self, tabla):
        self.content += f"CREA LA TABLA {tabla} "
        return self

    def tira_la_tabla(self, tabla):
        self.content += f"TIRA LA TABLA {tabla} "
        return self

    def por_defecto(self, valor):
        self.content += f"POR DEFECTO {valor} "
        return self

    def unico(self):
        self.content += "UNICO "
        return self

    def clave_prima(self, columna):
        self.content += f"CLAVE PRIMA ({columna}) "
        return self

    def clave_referente(self, columna, tabla_ref, columna_ref):
        self.content += f"CLAVE REFERENTE ({columna}) REFERENCIAS {tabla_ref}({columna_ref}) "
        return self

    def no_nulo(self):
        self.content += "NO NULO "
        return self

    def transforma_a(self, expresion, tipo_dato):
        self.content += f"TRANSFORMA A({expresion} COMO {tipo_dato}) "
        return self
    