from main import create_parser

if __name__ == '__main__':
    parser = create_parser()

    #Tests
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
