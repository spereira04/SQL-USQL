from main import create_parser
from fluentApi import FluentApiSQL2USQL, FluentApiUSQL2SQL


def run_manual_tests():
    parser = create_parser()
    
    parser.parse( 'TRAEME TODO DE LA TABLA usuarios DONDE edad > 18;')
    parser.parse( 'TRAEME LOS DISTINTOS nombre DE LA TABLA clientes DONDE ciudad = \'Madrid\';')
    parser.parse( 'METE EN usuarios (nombre, edad) LOS VALORES (\'Juan\', 25);')
    parser.parse( 'ACTUALIZA empleados SETEA salario = 3000 DONDE puesto = \'ingeniero\';')
    parser.parse( 'TRAEME TODO DE LA TABLA pedidos MEZCLANDO clientes EN pedidos.cliente_id = clientes.id DONDE clientes.ciudad = \'Barcelona\';')
    parser.parse( 'TRAEME CONTANDO(TODO) DE LA TABLA ventas AGRUPANDO POR producto WHERE DEL GROUP BY COUNT(*) > 5;')
    parser.parse( 'BORRA DE LA tabla clientes DONDE edad ENTRE 18 Y 25;')
    parser.parse( 'CAMBIA LA TABLA empleados AGREGA LA COLUMNA direccion VARCHAR(255) NO NULO;')
    parser.parse( 'CAMBIA LA TABLA empleados ELIMINA LA COLUMNA direccion;')

    print("-------------------------------------------\n\n")

    parser.parse('SELECT * FROM usuarios WHERE edad > 18;')
    parser.parse('SELECT DISTINCT nombre FROM clientes WHERE ciudad = \'Madrid\';')
    parser.parse('INSERT INTO usuarios (nombre, edad) VALUES (\'Juan\', 25);')
    parser.parse('UPDATE empleados SET salario = 3000 WHERE puesto = \'ingeniero\';')
    parser.parse('SELECT * FROM pedidos JOIN clientes ON pedidos.cliente_id = clientes.id WHERE clientes.ciudad = \'Barcelona\';')
    parser.parse('SELECT COUNT(*) FROM ventas GROUP BY producto HAVING COUNT(*) > 5;')
    parser.parse('DELETE FROM tabla clientes WHERE edad BETWEEN 18 Y 25;')
    parser.parse('ALTER TABLE empleados ADD COLUMN direccion VARCHAR(255) NOT NULL;')
    parser.parse('ALTER TABLE empleados DROP COLUMN direccion;')

    print("-------------------------------------------\n\n")

    parser.parse('SELECT nombre, edad FROM usuarios WHERE ciudad = \'Valencia\';')
    parser.parse('INSERT INTO clientes (nombre, ciudad) VALUES (\'Ana\', \'Sevilla\');')
    parser.parse('UPDATE productos SET precio = 150 WHERE id = 1;')
    parser.parse('DELETE FROM pedidos WHERE fecha < \'2023-01-01\';')
    parser.parse('SELECT * FROM ventas ORDER BY fecha DESC;')
    parser.parse('SELECT COUNT(*) FROM usuarios WHERE edad BETWEEN 30 AND 40 HAVING COUNT(*) > 10;')
    parser.parse('ALTER TABLE clientes DROP COLUMN telefono;')
    parser.parse('CREATE TABLE empleados (id INT, nombre VARCHAR(100), salario DECIMAL(10, 2));')
    parser.parse('DROP TABLE IF EXISTS productos;')
    parser.parse('SELECT DISTINCT ciudad FROM clientes WHERE pais = \'España\';')
    parser.parse('SELECT nombre FROM empleados WHERE salario > (SELECT AVG(salario) FROM empleados);')
    parser.parse('UPDATE ventas SET cantidad = cantidad + 1 WHERE producto_id = 5;')
    parser.parse('INSERT INTO pedidos (cliente_id, fecha) VALUES (1, \'2024-10-28\');')
    parser.parse('SELECT nombre, COUNT(*) FROM usuarios GROUP BY nombre HAVING COUNT(*) > 1;')

def run_fluent_api_tests():
    usql2sql = FluentApiUSQL2SQL()
    sql2usql = FluentApiSQL2USQL()

    usql2sql.traeme("nombre").de_la_tabla("usuarios").donde("edad > 21").parse()
    usql2sql.traeme("nombre, edad").de_la_tabla("clientes").parse()
    usql2sql.mete_en("productos").los_valores("('Laptop', 1200)").parse()
    usql2sql.actualiza("empleados").setea("sueldo = 3500").donde("id = 5").parse()
    usql2sql.traeme("departamento, COUNT(*)").de_la_tabla("empleados").agrupando_por("departamento").parse()
    usql2sql.traeme("nombre").de_la_tabla("proveedores").ordena_por("nombre ASC").parse()
    usql2sql.traeme("edad").de_la_tabla("usuarios").entre(18, 25).parse()
    usql2sql.crea_la_tabla("nuevos_usuarios").parse()
    usql2sql.elimina_la_columna("antigua_direccion").parse()
    usql2sql.transforma_a("salario", "DECIMAL(10,2)").parse()

    sql2usql.select("nombre").from_table("usuarios").where("edad > 21").parse()
    sql2usql.select_distinct("nombre, edad").from_table("clientes").parse()
    sql2usql.insert_into("productos").values("'Laptop', 1200").parse()
    sql2usql.update("empleados").set_value("sueldo = 3500").where("id = 5").parse()
    sql2usql.select("departamento, COUNT(*)").from_table("empleados").group_by("departamento").parse()
    sql2usql.select("nombre").from_table("proveedores").order_by("nombre ASC").parse()
    sql2usql.delete_from("pedidos").where("status = 'cancelado'").parse()
    sql2usql.create_table("nuevos_usuarios").add("id INT").add("nombre VARCHAR(100)").parse()
    sql2usql.create_table("usuarios").add("direccion VARCHAR(255)").parse()
    sql2usql.cast("salario", "DECIMAL(10,2)").parse()

if __name__ == '__main__':
    # Manual Tests
    # run_manual_tests()

    # Fluent Api Tests
    run_fluent_api_tests()
    