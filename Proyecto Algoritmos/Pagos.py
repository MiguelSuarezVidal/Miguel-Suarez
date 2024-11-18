from Persona import Persona
from Persona import Cliente_Jur
from Persona import Cliente_Nat

# Cliente que realizó la compra
# Productos comprados
# Cantidad de cada producto
# Método de pago
# Método de envío
# El desglose del total de compra
# Subtotal 
# Descuentos
# 5% de descuento si el cliente es jurídico y paga de contado 
# IVA (16%)
# IGTF (3%) en caso de que pague en divisas
# Total

class Factura():
    def __init__(self, cliente, productos, monto_pago, metodo_pago, metodo_envio):
        self.cliente = cliente
        self.productos = productos
        self.monto_pago = monto_pago
        self.metodo_pago = metodo_pago
        self.metodo_envio = metodo_envio
        
    def show(self):
        self.cliente.show()
        for producto in self.productos:
            producto.show_pago()
        print(f'''
              Subtotal: {self.monto_pago}
              Metodo de pago: {self.metodo_pago}
              Metodo de envío: {self.metodo_envio}''')
        
    
        
    def show_factura(self):
        self.show()
        
        if isinstance(self.cliente, Cliente_Jur):
            self.monto_pago *= 0.95
            print(f'Monto descontado por ser cliente juridico: {self.monto_pago * 0.05}')
            print(f'Iva: {self.monto_pago * 0.16} ')
            self.monto_pago += self.monto_pago * 0.16
            
            if self.metodo_pago == 'Efectivo':
                print(f'IGTF: {self.monto_pago * 0.03} ')
                self.monto_pago += self.monto_pago * 0.03
                
        elif isinstance(self.cliente, Cliente_Nat):
            print(f'Iva: {self.monto_pago * 0.16} ')
            self.monto_pago += self.monto_pago * 0.16
            
            if self.metodo_pago == 'Efectivo':
                print(f'IGTF: {self.monto_pago * 0.03} ')
                self.monto_pago += self.monto_pago * 0.03
                
        print(f'Total: {self.monto_pago:.2f}')
        print('<-------------------->')
  
    def to_dict(self):
        return {
            "cliente": self.cliente.to_dict(),  
            "productos": [producto.to_dict() for producto in self.productos],  
            "metodo_pago": self.metodo_pago,
            "metodo_envio": self.metodo_envio
        }
  
  
class Pago(): 
    def __init__(self, factura, moneda, monto_cobrado, fecha):
        self.factura = factura
        self.moneda = moneda
        self.monto_cobrado = monto_cobrado
        self.fecha = fecha
        
    def show(self):
        self.factura.show()
        print(f'''-----------
              Moneda: {self.moneda}
              Monto cobrado: {self.monto_cobrado}
              Fecha de cobranza (dia/mes/año): {self.fecha}
              Deuda: {self.factura.monto_pago - self.monto_cobrado}
              <------------------------------------------->''')
    
    def show_pe(self):
        self.factura.show()
        print(f'''-----------
              Moneda: {self.moneda}
              Monto cobrado: {self.monto_cobrado}
              Fecha de cobranza (dia/mes/año): {self.fecha}
              Deuda: {self.factura.monto_pago}
              <------------------------------------------->''')
        
    def to_dict(self):
        return {
            "factura": self.factura.to_dict(),  
            "moneda": self.moneda,
            "monto_cobrado": self.monto_cobrado,
            "fecha": self.fecha
        }
    
class Envio():
    
    def __init__(self, pago, costo_servicio,fecha_envio):
        self.pago = pago
        self.costo_servicio = costo_servicio
        self.fecha_envio = fecha_envio
        
    def show_envio(self):
        self.pago.show()
        print(f'''
              Costo del sevicio: {self.costo_servicio}
              Fecha del envio: {self.fecha_envio}
              <------------------------------------------->''')
    
    def to_dict(self):
        return {
            "pago": self.pago.to_dict(),  # Asegúrate de que el pago también tenga un método to_dict
            "costo_servicio": self.costo_servicio,
            "fecha_envio": self.fecha_envio
        }        
        