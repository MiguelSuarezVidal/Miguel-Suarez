
from Data import data
from Producto import Producto
from Persona import Persona
from Persona import Cliente_Jur
from Persona import Cliente_Nat
from Pagos import Factura
from Pagos import Pago
from Pagos import Envio
import json
import os

class App:
    def __init__(self):
        
        self.inventario = []
        self.contactos = []
        self.motos = []
        self.facturas = []
        self.productos = []
        self.ventas = []
        self.clientes= []
        self.clientes_dict = []
        self.pagos = []
        self.envios = []
        self.cargar_datos()

    def cargar_datos(self):
        if os.path.exists("data_base.json"):
            try:
                with open("data_base.json", "r") as data_base:
                    datos = json.load(data_base)
                    self.productos = datos.get("productos", [])
                    self.ventas = datos.get("ventas", [])
                    self.clientes_dict = datos.get("clientes", [])
                    self.pagos = datos.get("pagos", [])
                    self.envios = datos.get("envios", [])
                    
                    # Imprimir los datos cargados para verificar
                    print("Datos cargados:")
                    print(f"Productos: {self.productos}")
                    print(f"Ventas: {self.ventas}")
                    print(f"Clientes: {self.clientes_dict}")
                    print(f"Pagos: {self.pagos}")
                    print(f"Envios: {self.envios}")
                
            except json.JSONDecodeError:
                print("Error: El archivo JSON está mal formado.")
            except Exception as e:
                print(f"Error al cargar datos: {e}")

    def guardar_datos(self):
   
        datos = {
            "productos": [producto.to_dict() for producto in self.productos],
            "ventas": [venta.to_dict() for venta in self.ventas],
            "clientes": [cliente.to_dict() for cliente in self.clientes],
            "pagos": [pago.to_dict() for pago in self.pagos],
            "envios": [envio.to_dict() for envio in self.envios]
        }

        with open("data_base.json", "w") as data_base:
            json.dump(datos, data_base, indent=4)

        print("Datos guardados exitosamente en data_base.json")

            

    
        
    def val_cedula(self):
        while True:
            ci = input('Ingrese la cedula del cliente: ')
            print(f"Valor ingresado: {ci}")  # Imprime el valor ingresado para depurar
            
            # Verifica si la cédula tiene 7 o 8 caracteres y si son solo números
            if not ci.isnumeric():
                print('Error: La cédula debe contener solo números.')
                continue
            
            if len(ci) != 7 and len(ci) != 8:
                print('Error: La cédula debe tener 7 o 8 dígitos.')
                continue
            
            # Si pasa todas las validaciones, retorna la cédula
            print(f"Cédula válida: {ci}")  # Imprime la cédula válida
            return ci
            
    def val_correo(self,email):
        if email.count('@') != 1 or email.count('.') < 1:
            return False
        return True
             
    def val_rif(self):
        while True:
            r = input('Ingrese el RIF: ')
             
            if not r.isnumeric():
                print('Error: El RIF debe contener solo números.')
                continue
            
            if len(r) != 10:
                print('Error: El RIF debe tener 10 dígitos.')
                continue
            

            print(f"RIF válido: {r}") 
            return r
            
    def val_tlf(self):
        while True:
            tlf= input('Ingrese el numero de telefono: ')
            if len(tlf) != 11 or not tlf.isnumeric():
                tlf= input('Error.....Ingrese el numero de telefono: ')
            else:
                return tlf
        
    def crear_inventario(self):
        for i in data: 
            self.inventario.append(Producto(i['id'], i['name'], i['description'], i['price'], i['category'], i['inventory'], i['compatible_vehicles']))
        
        for i in self.clientes_dict:
            self.clientes.append(Cliente_Nat(i['nombre'],i['apellido'],i['correo'],i['telefono'],i['cedula'],i['direccion']))    
    
    
    def agregar_producto(self):#1
        id = input('Ingrese el id del producto:')
        name = input('Ingrese el nombre del producto:')
        description = input('Ingrese la descripción del producto:')
        price = input('Ingrese el precio del producto:')
        category = input('Ingrese la categoría del producto:')
        inventory = input('Ingrese la cantidad del producto:')
        compatible_vehicles = input('Ingrese los vehiculos compatibles con el producto:')
        producto=Producto(id, name, description, price, category, inventory, compatible_vehicles)
        self.inventario.append(producto)
        print(f'''Su producto ha sido registrado exitosamente...
              {producto.show()}''')                       

    def buscar_productos(self):#2
        while True:
            for producto in self.inventario:
                producto.show()
            parametro_busqueda= input('''
            Seleccione el parametro de busqueda para el producto
            1.Categoria
            2.Precio
            3.Nombre
            4.Disponibilidad en el inventario
            -------------------------------------------
            0.Salir de busqueda                           
                                      ''')
            if parametro_busqueda == '1':
                categoria = input('Ingrese la categoria del producto:')
                for producto in self.inventario:
                    if producto.category == categoria:
                        print(f'''{producto.show()}''')
            elif parametro_busqueda == '2':
                precio = input('Ingrese el precio del producto:')
                for producto in self.inventario:
                    if producto.price == precio:
                        print(f'''{producto.show()}''')
            elif parametro_busqueda == '3':
                nombre = input('Ingrese el nombre del producto:')
                for producto in self.inventario:
                    if producto.name == nombre:
                        print(f'''{producto.show()}''')
            elif parametro_busqueda == '4':
                cantidad = input('Ingrese la cantidad del producto:')
                for producto in self.inventario:
                    if producto.inventory == cantidad:
                        print(f'''{producto.show()}''')
            elif parametro_busqueda == '0':
                break
    
    def modificar_productos(self):#3 revisar el break del del menu del parametro a modificar
        print('Modificar Producto')
        for producto in self.inventario:
            producto.show()
        while True:
            id = input('Ingrese el id del producto a modificar:')
            for producto in self.inventario:
                if id == producto.id:
                    producto.show()
                while True:
                        opcion=input('''Ingrese el parametro que desea modificar:
                                     1.Nombre
                                     2.Descripción
                                     3.Precio
                                     4.Categoria
                                     5.Inventario
                                     6.Compatibilidad con los vehiculos
                                     ----------------------------------------------------
                                     0.Salir
                                     ''')
                        if opcion == '0':
                            print('pase ')
                            break
                        
                        elif opcion == '1': 
                            print(producto.name)
                            producto.name = input('Ingrese el nuevo nombre del producto:')
                            print('Nombre modificado')
                            producto.show()
                        elif opcion == '2':
                            print(producto.description)       
                            producto.description = input('Ingrese la nueva descripcion del producto:')
                            print('Descripcion modificada')
                            producto.show()
                        elif opcion == '3':
                            print(producto.price)
                            producto.price = float(input('Ingrese el nuevo valor del producto:'))
                            print('Precio modificado')
                            producto.show()
                        elif opcion == '4':
                            print(producto.category)
                            producto.category = input('Ingrese la nueva categoria del producto:')
                            print('Categoria modificada')
                            producto.show()
                        elif opcion == '5':
                            print(producto.inventory)
                            producto.inventory= int(input('Ingrese el inventario de producto'))
                            print('Inventario modificado')
                            producto.show()
                        elif opcion == '6':
                            print(producto.inventory)

                            while True:
                                opcion_1 = input('''Ingrese la opcion que desea realizar:
                                               1.Modificar
                                               ---------------
                                               0.Salir
                                               ''')
                                if opcion_1 == 0:
                                    print('pase')
                                    break
                                elif opcion_1 == '1':
                                        print ('pase')
                                        producto.show()
                                        producto.compatible_vehicles.append(input("Ingrese modelo de carro del cual es compatible:"))
                                        print('Compatibilidad modificada')
                                        producto.show()
                                        break
                                    

                # else:
                #     print("No hay productos para mostrar")
                            
    def eliminar_producto(self):#4 falta por hacer se neesita llamar a el de busqueda  revisar el como eliminar el producto  
        print('Eliminar Producto')
        for producto in self.inventario:
            producto.show()    
        while True:
            id = input('Ingrese el id del producto a eliminar:')
            for producto_e in self.inventario:
                if producto_e.id == int(id):
                    producto_e.show()
                    opcion_e= input('''¿Seguro que desea elimiar el producto seleccionado?
                                  1.Si
                                  2.No
                                  ''')
                    if opcion_e == '1':
                        for producto_b in self.inventario:
                            if producto_b == producto_e:
                                self.inventario.remove(producto_b)
                                print('Producto eliminado')
                                
                    else:
                        print('Operacion cancelada')
            else:
                print('No se encontro el producto')
                opcion = input('''¿Desea continuar eliminando productos?
                               1.Si
                               2.No
                               ''')
                if opcion == '1':
                    self.eliminar_producto()
                
                elif opcion == '2':
                    break
                                    
    def gestion_productos(self): 
        while True:
            print('''Bienvenido a la gestion de productos''')
            opcion_productos = input('''
            1.Agregar productos 
            2.Buscar productos
            3.Modificar productos
            4.Eliminar productos
            ------------------------
            0.Regresar al menu principal                                                           
            ----------------------------------------------------------------
            Ingrese el numero de la accion que desea realizar:\n''')
            if opcion_productos == '0':  
                break
            elif opcion_productos == '1':
                self.agregar_producto()# Aqui iria el codigo para agregar productos (funcion agregar product)
            elif opcion_productos == '2':
                self.buscar_productos()# Aqui iria el codigo para buscar productos (funcion buscar)
            elif opcion_productos == '3':
                self.modificar_productos()# Aqui iria el codigo para modificar productos (funcion modificar)
            elif opcion_productos == '4':
                self.eliminar_producto()



    def contacto(self):
        nombre = input('Ingrese el nombre del contacto: ')
        apellido = input('Ingrese el apellido del contacto: ')
        email = input("Ingrese su direccion de correo: ")
        while not self.val_correo(email):
            print("Error!!! Dato invalido")
            email = input("Ingrese su direccion de correo: ")
        telefono = self.val_tlf()
        contacto= (Persona(nombre, apellido, email, telefono))
        print('Contacto registrado')
        return contacto

    def registrar_cliente(self):
        while True:
            tipo= input('''Ingrese el tipo de cliente:
                        1. Cliente Natural
                        2. Cliente Juridico
                        ----------------------------------
                        0.Salir
                        ''')
            if tipo == '0':
                break
            elif tipo == '1':
                nombre = input('Ingrese el nombre del cliente: ')
                apellido = input('Ingrese el apellido del cliente: ')
                email = input("Ingrese su direccion de correo: ")
                while not self.val_correo(email):
                    print("Error!!! Dato invalido")
                    email = input("Ingrese su direccion de correo: ")
                telefono = self.val_tlf()
                cedula= self.val_cedula()
                direccion= input('Ingrese la direccion del cliente: ')
                cl=Cliente_Nat(nombre, apellido, email, int(telefono), int(cedula), direccion) 
                self.clientes.append(Cliente_Nat(nombre, apellido, email, int(telefono), int(cedula), direccion))
                print( 'Cliente registrado exitosamente')
                cl.show() 
                return cl
            
            elif tipo == '2':
                nombre = input('Ingrese el nombre de la empresa: ')
                rif = self.val_rif()
                email = input("Ingrese su direccion de correo: ")
                while not self.val_correo(email):
                    print("Error!!! Dato invalido")
                    email = input("Ingrese su direccion de correo: ")
                telefono = self.val_tlf()
                direccion = input('Ingrese la direccion de la empresa: ')
                contacto = self.contacto()
                cl=Cliente_Jur(nombre, int(rif), email, direccion , int(telefono), contacto)
                self.clientes.append(Cliente_Jur(nombre, int(rif), email, direccion, int(telefono), contacto))
                print('Cliente registrado exitosamente')
                cl.show()
                return cl
            
    def compra_producto(self):
        lista_compra = []  # Lista para almacenar productos y sus cantidades
        monto_pago = 0  

        while True:
            opcion_c = input('''Seleccione la operacion a realizar:
                            1.Añadir al carrito
                            2.Revisar el carrito
                            3.Continuar 
                            --------------------------------------
                            0.Cancelar compra
                            ''')
            if opcion_c == '0':
                break
            elif opcion_c == '1':
                id = input('''Ingrese el id del producto que desea comprar:
                        ''')
                producto_encontrado = False  
                for producto in self.inventario:
                    if int(id) == producto.id:
                        producto.show_pago()  # Muestra detalles del producto
                        cantidad_cu = int(input('Cantidad del producto: '))
                        producto.inventory-=cantidad_cu
                        # Agrega el producto y la cantidad a la lista de compra
                        lista_compra.append((producto, cantidad_cu))
                        
                        # Calcula el monto total
                        monto_pago += cantidad_cu * producto.price
                        
                        print('Producto agregado al carrito')
                        producto_encontrado = True  # Cambia a verdadero si se encuentra el producto
                        break  
                
                if not producto_encontrado:
                    print("Producto no encontrado.")
                    
            elif opcion_c == '2':
                print("Carrito de compras:")
                if not lista_compra:  # Verifica si la lista de compra está vacía
                    print("El carrito está vacío.")
                else:
                    for prod, cantidad in lista_compra:
                        subtotal = prod.price * cantidad
                        prod.show_pago()  # Muestra detalles del producto
                        print(f"Cantidad: {cantidad}, Subtotal: {subtotal:.2f}")  # Muestra el subtotal por producto
                    print(f"Total a pagar: {monto_pago:.2f}")  # Muestra el total a pagar
            elif opcion_c == '3':
                for prod, cantidad in lista_compra:
                        subtotal = prod.price * cantidad
                return  monto_pago  # Retorna la cantidad total de productos y el monto total
            else:
                print('Opcion invalida')
            
    def asignar_moto(self):
        nombre=input('Ingrese el nombre del motorizado: ') 
        apellido=input('Ingrese el apellido del motorizado: ')
        correo= input('Correo del motorizado: ')
        telefono=  input('Telefono del motorizado: ')
        moto= Persona(nombre,apellido,correo,telefono)
        self.motos.append(moto) 
        
           
   
    def registro_ventas(self):
        monto_pago=0
        cantidad_productos=0
        cliente=None
        lista_compra=[]
        subtotal=0
        while True:
                while True:
                    opcion_v= input('''Bienvenido a la gestion de ventas
                                    1. Cliente nuevo
                                    2. Cliente registrado
                                    Seleccione quien realiza la compra:  ''')
                    if opcion_v == '1':
                        cliente= self.registrar_cliente()
                        break
                    elif opcion_v == '2':
                        cliente= self.buscar_clientes()
                        break                                             
                a = self.compra_producto()
                
                opcion_p= input('''Eliga el metodo de pago:                 
                                   1.Efectivo
                                   2.Pago movil
                                   3.Zelle
                                   ------------------------------
                                   0.Cancelar
                                   ''')
                if opcion_p=='0':
                    break
                elif opcion_p=='1':
                    metodo_p='Efectivo' 
                    
                elif opcion_p=='2':
                    metodo_p='Pago Movil'
                    
                elif opcion_p=='3':
                    metodo_p='Zelle'
                    
                else:
                    print('Error..............')
                    
                metodo_pago = metodo_p
                metodo_envio= input('''Metodo de envio:
                                    1.Zoom
                                    2.Delivery por moto
                                    ------------------------
                                    0.Cancelar
                                    ''')
                if metodo_envio == '0':
                    break
                elif metodo_envio == '1':
                    metodo_envio = 'Zoom'
                elif metodo_envio == '2':
                    metodo_envio = 'Delivery por moto'
                    self.asignar_moto
                for prod, cantidad in lista_compra:
                        subtotal = prod.price * cantidad
                venta=Factura(cliente, lista_compra, a , metodo_pago, metodo_envio)
                self.ventas.append(venta)
                venta.show()
                break
                
                                           #                             Método de envío
                                            #                             El desglose del total de compra
                                            #                             Subtotal 
                                            #                             Descuentos
                                            #                             5% de descuento si el cliente es jurídico y paga de contado 
                                            #                             IVA (16%)
                                            #   IGTF (3%) en caso de que pague en divisas
                                            #   Total

    def generar_factura(self):
        for venta in self.ventas:
            venta.show()
        
        factura = int(input('Ingrese la cedula o rif de la factura que desea generar:'))
        
        for compra in self.ventas:
           
            if isinstance(compra.cliente, Cliente_Nat) and compra.cliente.cedula == factura:
                compra.show_factura()
                
                print('Factura Generada')
                self.facturas.append(compra)
                return  
            
            elif isinstance(compra.cliente, Cliente_Jur) and compra.cliente.rif == factura:
                compra.show_factura()
                self.facturas.append(compra)
                print('Factura Generada')
                return  

        print('No se encontró la venta')
   
    def consulta_ventas(self):#FALTA
        if len(self.facturas) != 0:
            for i in self.facturas:
                i.show()
                print('Ventas consultadas')
        else:
            print('No hay ventas')
                
    def gestion_ventas(self):
        while True:
            print('''Bienvenido a la gestion de ventas''')
            opcion_ventas = input('''
            Ingrese la accion a realizar
            1.Registro de ventas
            2.Facturas
            3.Consulta de ventas
            ----------------------------
            0.Salir
                                  
                                  ''')
            if opcion_ventas == '0':
                break
            elif opcion_ventas == '1':
                self.registro_ventas()
            elif opcion_ventas == '2':
                self.generar_factura()
            elif opcion_ventas == '3':
                self.consulta_ventas()
            else:
                print('Opción no válida')
                   
          
                   
    def registrar_clientes(self):
        while True:
            opcion=input('''
                         Ingrese el tipo de cliete que desea registrar
                         1.Natural
                         2.Empresa
                         ''')
            if opcion=='1':   
                nombre = input('Ingrese el nombre del cliente: ')
                apellido = input('Ingrese el apellido del cliente: ')
                telefono = input('Ingrese el telefono del cliente: ')
                correo = input('Ingrese el correo del cliente: ')
                cedula = input('Ingrese la cedula del cliente: ')
                direccion = input('Ingrese la direccion del cliente: ')
                cliente_nat= Cliente_Nat(nombre, apellido, telefono, correo, cedula, direccion )
                cliente_nat.show()
                self.clientes.append(cliente_nat)
                print('''------------------------------------
                      Cliente registrado con exito''')
                break
            elif opcion=='2':
                nombre_e=input('Ingrese nombre de la empresa:')
                rif=input('Ingrese el rif de la empresa:')
                correo_e=input('Ingrese el correo de la empresa:')
                direccion_e=input('Ingrese el direccion de la empresa:')
                telefono_e=input('Ingrese el telefono de la empresa:')
                nombre = input('Ingrese el nombre del contacto: ')
                apellido = input('Ingrese el apellido del contacto: ')
                telefono = input('Ingrese el telefono del contacto: ')
                correo = input('Ingrese el correo del contacto: ')
                contacto= Persona(nombre, apellido, telefono, correo)
                empresa= Cliente_Jur(nombre_e, rif, correo_e, direccion_e, telefono_e, contacto)
                self.clientes.append(empresa)
                print('''-----------------------
                      Cliente registrado con exito''')
                empresa.show()
                break
                        
    def modificar_clientes(self):
        for cliente in self.clientes:
            cliente.show()
        nombre = input("Ingrese el nombre del cliente para modificar: ")
        for cliente in self.clientes:
            if cliente.nombre == nombre:
                cliente.show()
                opcion = input("Ingrese el campo que desea modificar: ")
                if opcion == "nombre":
                    cliente.nombre = input("Ingrese el nuevo nombre: ")
                    cliente.show()
                elif opcion == "apellido":
                    cliente.apellido = input("Ingrese el nuevo apellido: ")
                    cliente.show()    
                elif opcion == 'telefono':
                    cliente.telefono = input('Ingrese el nuevo telefono: ')
                    cliente.show()
                print('Cliente modificado')
    
    def buscar_clientes(self):
        while True:
            opcion= input('''Elija el filtro para iniciar la busqueda del cliente: 
                          1.Cedula 
                          2.Rif
                          3.Correo electronico
                          ----------------------
                          0.Salir de la busqueda ''')
            if opcion == '1':
                cedula = input('Ingrese la cedula del cliente: ')
                for cliente in self.clientes:
                    if cliente.cedula == cedula:
                        cliente.show()
                        print('Cliente encontrado')
            elif opcion =='2':
                rif = input('Ingrese el rif del cliente: ')
                for cliente in self.clientes:
                    if cliente.rif == rif:
                        cliente.show()
                        print('Cliente encontrado')
            elif opcion == '3':
                correo = input('Ingrese el correo electronico del cliente a buscar: ')
                for cliente in self.clientes:
                    if cliente.correo == correo:
                        cliente.show()
                        print('Cliente encontrado')
            elif opcion == '0':
                break
        return cliente
                        
    def eliminar_clientes(self):
        for cliente in self.clientes:
            cliente.show()
            nombre_cliente = input('''Ingrese el nombre del cliento o empresa:
                                   ''')
            for cliente in self.clientes:
                if cliente.nombre == nombre_cliente:
                    self.clientes.remove(cliente)
                    print('Cliente eliminado')
                        
    def gestion_clientes(self):
        while True:
            print('''Bienvenido a la gestion de clientes''')
            opcion = input('''Ingrese la opcion que desea realizar:
                                    1.Registrar clientes
                                    2.Modificar clientes existentes
                                    3.Eliminar clientes
                                    4.Buscar clientes
                                    ----------------------------------------
                                    0.Salir
                                    ''')
            if opcion == '0':
                break
            elif opcion == '1':
                self.registrar_clientes()
            elif opcion == '2':
                self.modificar_clientes()
            elif opcion == '3':
                self.eliminar_clientes()
            elif opcion == '4':
                self.buscar_clientes()
            else:
                print('Opcion invalida')
 
 
 
    def registrar_pago(self):
        for factura in self.facturas:
            factura.show()  
        while True:
            venta = input('''Ingrese el parámetro de búsqueda para el pago que desea registrar 
                            1.Cédula 
                            2.RIF 
                            ----------------- 
                            0.Salir 
                            ---------------- 
                            Nota: Para poder registrar un pago asegúrese de que se haya generado la factura 
                            ''')
            if venta == '0':
                break
            
            elif venta == '1':
                cedula = int(input('''Ingrese la cédula del cliente: '''))
                factura_encontrada = False  
                for factura in self.facturas:
                    
                    if isinstance(factura.cliente, Cliente_Nat) and factura.cliente.cedula == cedula:
                        factura_encontrada = True
                        factura.show()
                        moneda = input('''Ingrese la moneda con la que va a pagar: 
                                        1.Bs 
                                        2.Dólares 
                                        3.Euros 
                                        ----------------------- 
                                        0.Salir 
                                        ''')
                        if moneda == '0':
                            break
                        elif moneda == '1':
                            moneda = 'Bs'
                            monto_cobrado = ((float(input('Ingrese el monto a pagar en Bs: ')))/45,78) #Depende de la tasa BCV
                        elif moneda == '2':
                            moneda = 'Dólares'
                            monto_cobrado = float(input('Ingrese el monto a pagar en Dólares:'))
                        elif moneda == '3':
                            moneda = 'Euros'
                            monto_cobrado = ((float(input('Ingrese el monto a pagar en Euros:')))/0.95)# Depende del valor del dolar 
                        else:
                            print('Moneda no válida')
                            continue  

                        dia = input('Ingrese el día de pago: ')
                        mes = input('Ingrese el mes de pago: ')
                        anio = input('Ingrese el año de pago: ')
                        fecha = dia, mes, anio
                        pago = Pago(factura, moneda, monto_cobrado, fecha)
                        pago.show()
                        self.pagos.append(pago)
                        factura.monto_pago -= monto_cobrado
                        print('Pago registrado exitosamente\n')
                        break
                
                if not factura_encontrada:
                    print('No se encontró ninguna factura con la cédula ingresada.')

            elif venta == '2':
                rif = int(input('''Ingrese el RIF del cliente: '''))
                factura_encontrada = False  # Variable para verificar si se encontró la factura
                for factura in self.facturas:
                    # Accede al RIF del cliente asociado a la factura
                    if isinstance(factura.cliente, Cliente_Jur) and factura.cliente.rif == rif:
                        factura_encontrada = True
                        factura.show()
                        moneda = input('''Ingrese la moneda con la que va a pagar: 
                                        1.Bs 
                                        2.Dólares 
                                        3.Euros 
                                        ----------------------- 
                                        0.Salir 
                                        ''')
                        if moneda == '0':
                            break
                        elif moneda == '1':
                            moneda = 'Bs'
                            monto_cobrado = ((float(input('Ingrese el monto a pagar en Bs: ')))/45,78) #Depende de la tasa BCV
                        elif moneda == '2':
                            moneda = 'Dólares'
                            monto_cobrado = float(input('Ingrese el monto a pagar en Dólares:'))
                        elif moneda == '3':
                            moneda = 'Euros'
                            monto_cobrado = ((float(input('Ingrese el monto a pagar en Euros:')))/0.95)# Depende del valor del dolar 
                        else:
                            print('Moneda no válida')
                            continue  # Regresa al inicio del bucle si la moneda no es válida

                        dia = input('Ingrese el día de pago: ')
                        mes = input('Ingrese el mes de pago: ')
                        anio = input('Ingrese el año de pago: ')
                        fecha = dia, mes, anio
                        pago = Pago(factura, moneda, monto_cobrado, fecha)
                        pago.show()
                        self.pagos.append(pago)
                        factura.monto_pago -= monto_cobrado
                        print('Pago registrado exitosamente\n')
                        break
    
    def buscar_pago(self):
        while True:
            opcion= input('''Elija el filtro para iniciar la busqueda del cliente: 
                          1.Cedula 
                          2.Rif
                          3.Correo electronico
                          ----------------------
                          0.Salir de la busqueda ''')
            if opcion == '1':
                cedula = int(self.val_cedula())
                for pago in self.pagos:
                    if pago.factura.cliente.cedula == cedula:
                        pago.show_pago()
                        print('Pago encontrado')
            elif opcion =='2':
                rif = int(self.val_rif())
                for pago in self.pagos:
                    if pago.factura.cliente.rif == rif:
                        pago.show_pago()
                        print('Pago encontrado')
            elif opcion == '3':
                correo = self.val_correo()
                for pago in self.pagos:
                    if pago.factura.cliente.correo == correo:
                        pago.show_pago()
                        print('Pago encontrado')
            elif opcion == '0':
                break
            else:
                print('Opción no válida')
                    
    def gestion_pagos(self):

            print('''Bienvenido a la gestion de pagos''')
            
            if len(self.facturas) == 0:
                print('No hay facturas para gestionar')
            else:
                for i in self.facturas:  
                    opcion = input('''Ingrese la opcion que desea realizar:
                                1.Registrar un pago
                                2.Buscar pagos
                                -----------------------------------------
                                0.Salir
                                ''')
                    if opcion == '0':
                        pass
                    elif opcion == '1':
                        self.registrar_pago()
                    elif opcion == '2':
                        self.buscar_pago()
                    else: 
                        print('Opcion invalida')
        
        
        
    def registrar_envio(self):
        while True:
            print('''<-Registro de envios-> ''')
            opcion_e = input('''Ingrese la opcion que desea realizar:
                           
                           1.Asignar fecha de envio
                           -----------------------------------------
                           0.Salir
                           ''')
            if opcion_e == '0':
                break
            elif opcion_e == '1':
                for pago in self.pagos:
                    pago.show_pe()
                envio_b= int(input('''Ingrese la cedula o RIF del pago para asignar fecha de envio:'''))
                for pago in self.pagos:
                    if pago.factura.cliente.cedula == envio_b:
                        costo_servicio=float(input('''Ingrese el costo por envio (en dolares):'''))
                        dia=int(input('Ingrese el dia del envio:'))
                        mes=int(input('Ingrese el mes del envio:'))
                        anio=int(input('Ingrese el año del envio:'))
                        fecha_envio = dia,mes,anio
                        envio= Envio(pago, costo_servicio, fecha_envio)
                        self.envios.append(envio)
                        envio.show_envio
                        print('Fecha de envio asignada con exito')
                        
                    elif pago.factura.cliente.rif == envio_b:
                        costo_servicio=float(input('''Ingrese el costo por envio (en dolares):'''))
                        dia=int(input('Ingrese el dia del envio:'))
                        mes=int(input('Ingrese el mes del envio:'))
                        anio=int(input('Ingrese el año del envio:'))
                        fecha_envio = dia,mes,anio
                        envio= Envio(pago, costo_servicio, fecha_envio)
                        self.envios.append(envio)
                        envio.show_envio()
                        print('Fecha de envio asignada con exito')
                    
                    else:
                        print('No se encontro el pago')
                           
    def buscar_envio(self):
        while True:
            opcion_envio = input('''Ingrese el parametro de busqueda que desea usar:
                                1.RIF del cliente
                                2.Cedula del cliente
                                3.Fecha
                                -----------------------------------------------------
                                0.Salir
                                ''')
            if opcion_envio == '1':
                rif = input('Ingrese el RIF del cliente: ')
                for envio in self.envios:
                    if envio.factura.cliente.rif == rif:
                        envio.show_envio()  
                        print('Envio encontrado')
                        break
            elif opcion_envio == '2':
                cedula = input('Ingrese la cedula del cliente: ')
                for envio in self.envios:
                    if envio.factura.cliente.cedula == cedula:
                        envio.show_envio()
                        print('Envio encontrado')
                        break
            elif opcion_envio == '3':
                fecha = input('Ingrese la fecha del envio de este metodo (dia,mes,año): ')
                for envio in self.envios:
                    if envio.fecha == fecha:
                        envio.show_envio()
                        print('Envio encontrado')
                        break
                    
    def gestion_envios(self):   
        while True:
            print('''Bienvenido a la gestion de envios''')
            opcion = input('''Ingrese la opcion:
                           1.Registrar envio
                           2.Buscar envio
                           ------------------------------
                           0.Regresar al menu principal
                           ''')
            if opcion == '1':
                self.registrar_envio()
            elif opcion == '2':
                self.buscar_envio()
            elif opcion == '0':
                break
            else:
                print('Opcion invalida')
    
    
    
    def gestion_indicadores(self):
        pass
               
    def menu_principal(self):
        self.crear_inventario()
        self.cargar_datos()
        self.inventario
        self.clientes 
        self.contactos 
        self.ventas
        self.motos
        self.facturas 
        self.pagos
        self.envios
        
        
        while True:
            print("<-Bienvenido a la tienda de respuestos TMEM->")
            opcion =input('''
            1.Gestion de productos
            2.Gestion de ventas
            3.Gestion de clientes
            4.Gestion de pagos
            5.Gestion de envios
            6.Indicadores de gestion
            --------------------------
            0.Salir           
            --------------------------
            Ingrese el numero de la accion que desea realizar:\n''')
            
            if opcion == '0':
                self.guardar_datos()  # Guarda los datos al salir
                print("Vuelva pronto..........")
                break
                
            elif opcion == '1':
                self.gestion_productos()
            elif opcion == '2':
                self.gestion_ventas()
            elif opcion == '3':
                self.gestion_clientes()
            elif opcion == '4':
                self.gestion_pagos()
            elif opcion == '5':
                self.gestion_envios()
            elif opcion == '6':
                self.gestion_indicadores()
            else:
                print('Error......... Intente de nuevo')
                