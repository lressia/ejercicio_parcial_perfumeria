# ejercicio_parcial_perfumeria

Una perfumería desea un programa que procese los datos de las ventas que realiza. En cada Venta se registran los siguientes datos: el número de factura, importe de la factura, el tipo de factura (A, B, C o E), el apellido de la persona que realiza la compra, y el tipo del perfume vendido (un número entero para indicar su marca, entre 1 y 17, por ejemplo: 1: Chanel, 2: Paco Rabanne, etc.). Se desea almacenar la información referida a las ventas que realiza la perfumería en un arreglo de registros de tipo Venta (definir el tipo Venta y cargar n por teclado).

Se pide desarrollar un programa en Python controlado por un menú de opciones y que posea como mínimo dos módulos, que permita gestionar las siguientes tareas:

1- Cargar el arreglo pedido con los datos de n ventas realizadas. Valide que el importe de la factura sea mayor a 0 y menor a 200000. Valide que el tipo de factura sea alguno de los tipos válidos: A, B, C o E, y valide también que el tipo de perfume sea un número entero entre 1 y 17 ambos incluidos. Puede hacer la carga en forma manual, o puede generar los datos en forma automática (con valores aleatorios) o puede disponer de ambas técnicas si lo desea. Pero al menos una debe programar.

2- Mostrar todos los datos de las ventas cuyo importe de factura sea mayor a x y el tipo de la factura sea distinto de t (x y t son valores que se cargan por teclado). El listado debe salir ordenado de mayor a menor según los apellidos de las personas que realizaron la compra.

3- Determinar y mostrar el importe total facturado para cada uno de los 17 tipos posibles pero informe por pantalla solamente el total facturado correspondiente al tipo de perfume z (cargar el número z por teclado).

4- Mostrar por pantalla el número de factura, el comprador y el importe, de todas las ventas cuyo tipo de perfume se encuentre entre 5 y 12 y que no sean con factura de tipo C. Si no existe ninguna venta que cumpla con ese criterio informarlo por pantalla.

5- Determinar si existe una venta cuyo número de factura sea igual a n (cargar n por teclado) y cuyo importe de factura sea menor a a un valor p que se carga por teclado. Si existe, mostrar 
