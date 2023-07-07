class Carrito:
    
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get('carrito')

        if not carrito:
          self.session['carrito'] = {}
          self.carrito = self.session['carrito']
        else:
           self.carrito = carrito 

    def agregar(self, obra):
        id = str(obra.id)

        if id not in self.carrito.keys():
            self.carrito[id] = {
             'obra_id'    : obra.id,
             'titulo'     : obra.titulo,
             'categoria'  : obra.categoria.nombre, 
             'acumulado'  : obra.precio,
             'cantidad'   : 1,
            }
        else:
            self.carrito[id]['cantidad'] += 1
            self.carrito[id]['acumulado'] += obra.precio
        self.guardar_carrito()
       
    def guardar_carrito(self):
        self.session['carrito'] = self.carrito
        self.session.modified = True

    def eliminar(self, obra):
        id = str(obra.id)

        if id in self.carrito.keys():
            del self.carrito[id]
            self.guardar_carrito()

    def restar(self, obra):
        id = str(obra.id)

        if id in self.carrito.keys():
            self.carrito[id]['cantidad'] -= 1
            self.carrito[id]['acumulado'] -= obra.precio

            if self.carrito[id]['cantidad'] <= 0: self.eliminar(obra)
            self.guardar_carrito()

    def limpiar(self):
        self.session['carrito'] = {}
        self.session.modified = True
