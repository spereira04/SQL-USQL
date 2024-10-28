from main import create_parser

if __name__ == '__main__':
    #Tests
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
