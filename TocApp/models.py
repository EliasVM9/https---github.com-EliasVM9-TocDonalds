from django.db import models


class Producto(models.Model):
    nombreProd = models.CharField(max_length=50)
    tipoProducto = (('H','Hamburguesa'),('C','Completo'),('P','Pizza '),('PF','Papas Fritas'),('J','Jugo'),('B','Bebida'))
    nombreTipo = models.CharField(max_length=20, choices=tipoProducto, default='H')
    precio = models.IntegerField()
    
    def productoCompleto(self):
        cadena = "{0} {1}"
        return cadena.format(self.nombreProd, self.precio)
    def __str__(self):
        return "{0} ({1})".format(self.nombreProd,self.precio)


class Trabajador(models.Model):
    run = models.CharField(max_length=10)
    nombreCompleto = models.CharField(max_length=50)
    Crg = (('C','Cajero'),('G','Gestor de Reportes'),('A','Administrador'))
    Cargo = models.CharField(max_length=1, choices=Crg, default='C')
    tipoContr = (('P','Plazo Fijo'),('I','Indefinido'))
    Contrato = models.CharField(max_length=1, choices=tipoContr, default='I')

    def mostrarTrabajador(self):
        cadena = "{0} {1} {2}"
        return  cadena.format(self.run,self.nombreCompleto,self.Cargo)

    def __str__(self):
        return self.mostrarTrabajador()

class Combo(models.Model):
    producto1 = models.CharField(max_length=50)
    producto2 = models.CharField(max_length=50)
    producto3 = models.CharField(max_length=50)
    nombreCombo = models.CharField(max_length=50)
    precioCombo = models.IntegerField()

    def ComboCompleto(self):
        cadena = "{0} {1}"
        return cadena.format(self.nombreCombo,self.precioCombo)

    def __str__(self):
        return "{0} ({1})".format(self.nombreCombo, self.precioCombo)

class Pedido(models.Model):
    producto = models.ManyToManyField(Producto)
    combos = models.ManyToManyField(Combo)
    fecha = models.DateField(null=True)
    nombre_cliente = models.CharField(max_length=32,null=True)
    rut = models.CharField(max_length=16,null=True)
    email = models.EmailField(null=True)
    direccion = models.CharField(max_length=64,null=True)
    modo_entrega = models.CharField(max_length=64,null=True)
    entregado = models.BooleanField(default=False)
    finalizado = models.BooleanField(default=False)
    total = models.IntegerField()
    validado = models.BooleanField(default=False)
    class Estado(models.IntegerChoices):
        PENDIENTE = 1, "Pendiente de pago"
        PAGADO = 2, "Pagado"
        RECHAZADO = 3, "Rechazado"
        ANULADO = 4, "Anulado"
    estado = models.PositiveSmallIntegerField(
        choices=Estado.choices,
        default=Estado.PENDIENTE
    )
fdsf
    def str(self):
        return "Pedido "+str(self.id)


