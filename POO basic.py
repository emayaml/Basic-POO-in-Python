# -*- coding: utf-8 -*-
"""Taller#1dooIsabelAlvarezEmmanuelMaya.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-8Blw0hBoHFBIx7EUP6z8q6U7QwrhA00
"""

#Script en python sobre la composición de una empresa, conociendo las relaciones de POO
"""@emayaml"""

class Persona:
    def __init__(self, nombre, cedula, direccion, correo, telefono):
        self.nombre = nombre
        self.cedula = cedula
        self.direccion = direccion
        self.correo = correo
        self.telefono = telefono

    def __str__(self):
        return "Nombre: {}\nCedula: {}\nDireccion: {}\nCorreo: {}\nTelefono: {}".format(self.nombre, self.cedula, self.direccion, self.correo, self.telefono)

nombre = input("Ingrese su nombre: ")
cedula = input("Ingrese su cedula: ")
direccion = input("Ingrese su direccion: ")
correo = input("Ingrese su correo: ")
telefono = input("Ingrese su telefono: ")

persona = Persona(nombre, cedula, direccion, correo, telefono)

print(persona)

class Empleado(Persona):
    def __init__(self, fecha_ingreso, hora_ingreso, hora_salida, salario, tipo_contrato):
        self.fecha_ingreso = fecha_ingreso
        self.hora_ingreso = hora_ingreso
        self.hora_salida = hora_salida
        self.salario = salario
        self.tipo_contrato = tipo_contrato

    def __str__(self):
        return "Fecha de ingreso: {}\nHora de ingreso: {}\nHora de salida: {}\nSalario: {}\nTipo de contrato: {}".format(self.fecha_ingreso, self.hora_ingreso, self.hora_salida, self.salario, self.tipo_contrato)

fecha_ingreso = input("Ingrese la fecha de ingreso: ")
hora_ingreso = input("Ingrese la hora de ingreso: ")
hora_salida = input("Ingrese la hora de salida: ")
salario = input("Ingrese el salario: ")
tipo_contratos = ["Planta", "Contrato", "Por horas", "Pasantia"]
tipo_contrato = tipo_contratos[int(input("Ingrese el tipo de contrato: \n1. Planta\n2. Contrato\n3. Por horas\n4. Pasantia\n"))-1]

empleado = Empleado(fecha_ingreso, hora_ingreso, hora_salida, salario, tipo_contrato)

print(empleado)

class Administrativo(Empleado, Persona):
    def __init__(self, area, cargo):
        self.area = area
        self.cargo = cargo

    def __str__(self):
        return "Area: {}\nCargo: {}".format(self.area, self.cargo)

area = input("Ingrese el area: ")
cargo = input("Ingrese el cargo: ")

administrativo = Administrativo(area, cargo)

print(administrativo)


class Distribuidor(Empleado, Persona):
    def __init__(self, comision, ruta_distribucion):
        self.comision = comision
        self.ruta_distribucion = ruta_distribucion

    def __str__(self):
        return "Comision: {}\nRuta de distribucion: {}".format(self.comision, self.ruta_distribucion)

comision = input("Ingrese la comision: ")
ruta_distribucion = input("Ingrese la ruta de distribucion: ")

distribuidor = Distribuidor(comision, ruta_distribucion)

print(distribuidor)


class Accionista(Persona):
    def __init__(self, derechos, fecha_ingreso, porcentaje_participacion):
        self.derechos = derechos
        self.fecha_ingreso = fecha_ingreso
        self.porcentaje_participacion = porcentaje_participacion

    def __str__(self):
        return "Derechos: {}\nFecha de ingreso: {}\nPorcentaje de participacion: {}".format(self.derechos, self.fecha_ingreso, self.porcentaje_participacion)

derechos = input("Ingrese los derechos: ")
fecha_ingreso = input("Ingrese la fecha de ingreso: ")
porcentaje_participacion = input("Ingrese el porcentaje de participacion: ")

accionista = Accionista(derechos, fecha_ingreso, porcentaje_participacion)

print(accionista)


class Cliente(Persona):
    def __init__(self, fecha_compra, fecha_nacimiento, estado_civil):
        self.fecha_compra = fecha_compra
        self.fecha_nacimiento = fecha_nacimiento
        self.estado_civil = estado_civil

    def __str__(self):
        return "Fecha de compra: {}\nFecha de nacimiento: {}\nEstado civil: {}".format(self.fecha_compra, self.fecha_nacimiento, self.estado_civil)

fecha_compra = input("Ingrese la fecha de compra: ")
fecha_nacimiento = input("Ingrese la fecha de nacimiento: ")
estado_civil = ["Soltero", "Casado", "Divorciado", "Viudo"]
estado_civil = estado_civil[int(input("Ingrese el estado civil: \n1. Soltero\n2. Casado\n3. Divorciado\n4. Viudo\n"))-1]

cliente = Cliente(fecha_compra, fecha_nacimiento, estado_civil)

print(cliente)


class Empresa:
    def __init__(self, nombre, cantidad_empleados, tipo_empresa):
        self.nombre = nombre
        self.cantidad_empleados = cantidad_empleados
        self.tipo_empresa = tipo_empresa

    def __str__(self):
        return "Nombre: {}\nCantidad de empleados: {}\nTipo de empresa: {}".format(self.nombre, self.cantidad_empleados, self.tipo_empresa)

nombre = input("Ingrese el nombre de la empresa: ")
cantidad_empleados = input("Ingrese la cantidad de empleados: ")
tipo_empresa = ["Microempresa", "Mediana empresa", "Grande empresa"]
tipo_empresa = tipo_empresa[int(input("Ingrese el tipo de empresa: \n1. Microempresa\n2. Mediana empresa\n3. Grande empresa\n"))-1]

empresa = Empresa(nombre, cantidad_empleados, tipo_empresa)

print(empresa)

class Infraestructura(Empresa):
    def __init__(self, ubicacion_sede, tamaño_metros_cuadrados, sector):
        self.ubicacion_sede = ubicacion_sede
        self.tamaño_metros_cuadrados = tamaño_metros_cuadrados
        self.sector = sector

    def __str__(self):
        return "Ubicacion de la sede: {}\nTamaño en metros cuadrados: {}\nSector: {}".format(self.ubicacion_sede, self.tamaño_metros_cuadrados, self.sector)

ubicacion_sede = input("Ingrese la ubicacion de la sede: ")
tamaño_metros_cuadrados = input("Ingrese el tamaño en metros cuadrados: ")
sector = ["Privado", "Publico"]
sector = sector[int(input("Ingrese el sector: \n1. Privado\n2. Publico\n"))-1]

infraestructura = Infraestructura(ubicacion_sede, tamaño_metros_cuadrados, sector)

print(infraestructura)


class Sede(Empresa):
    def __init__(self, nombre_sede, cantidad_personas):
        self.nombre_sede = nombre_sede
        self.cantidad_personas = cantidad_personas

    def __str__(self):
        return "Nombre de la sede: {}\nCantidad de personas: {}".format(self.nombre_sede, self.cantidad_personas)

nombre_sede = input("Ingrese el nombre de la sede: ")
cantidad_personas = input("Ingrese la cantidad de personas: ")

sede = Sede(nombre_sede, cantidad_personas)

print(sede)

class Producto:
    def __init__(self, nombre_producto, tipo_producto, precio_producto, codigo, compro):
        self.nombre_producto = nombre_producto
        self.tipo_producto = tipo_producto
        self.precio_producto = precio_producto
        self.codigo = codigo
        self.compro = compro

    def __str__(self):
        return "Nombre del producto: {}\nTipo del producto: {}\nPrecio del producto: {}\nCodigo: {}\nCompro: {}".format(self.nombre_producto, self.tipo_producto, self.precio_producto, self.codigo, self.compro)

nombre_producto = input("Ingrese el nombre del producto: ")
tipo_producto = input("Ingrese el tipo del producto: ")
precio_producto = input("Ingrese el precio del producto: ")
codigo = input("Ingrese el codigo: ")
compro = input("Ingrese si compro o no el producto: ")

producto = Producto(nombre_producto, tipo_producto, precio_producto, codigo, compro)

print(producto)

class Contrato:
    def __init__(self, id, tipo_contrato, puesto, salario):
        self.id = id
        self.tipo_contrato = tipo_contrato
        self.puesto = puesto
        self.salario = salario

    def __str__(self):
        return "Id: {}\nTipo de contrato: {}\nPuesto: {}\nSalario: {}".format(self.id, self.tipo_contrato, self.puesto, self.salario)

id = input("Ingrese el id: ")
tipo_contratos = ["Planta", "Contrato", "Por horas", "Pasantia"]
tipo_contrato = tipo_contratos[int(input("Ingrese el tipo de contrato: \n1. Planta\n2. Contrato\n3. Por horas\n4. Pasantia\n"))-1]
puesto = input("Ingrese el puesto: ")
salario = input("Ingrese el salario: ")

contrato = Contrato(id, tipo_contrato, puesto, salario)

print(contrato)


class Entidad:
    def __init__(self, nombre_entidad, tipo_entidad):
        self.nombre_entidad = nombre_entidad
        self.tipo_entidad = tipo_entidad

    def __str__(self):
        return "Nombre de la entidad: {}\nTipo de entidad: {}".format(self.nombre_entidad, self.tipo_entidad)

nombre_entidad = input("Ingrese el nombre de la entidad: ")
tipo_entidad = input("Ingrese el tipo de entidad: ")

entidad = Entidad(nombre_entidad, tipo_entidad)

print(entidad)



class Pago:
    def __init__(self, metodo_pago, efectivo):
        self.metodo_pago = metodo_pago
        self.efectivo = efectivo

    def __str__(self):
        return "Metodo de pago: {}\nEfectivo: {}".format(self.metodo_pago, self.efectivo)

metodo_pagos = ["Efectivo", "Tarjeta"]
metodo_pago = metodo_pagos[int(input("Ingrese el metodo de pago: \n1. Efectivo\n2. Tarjeta\n"))-1]
efectivo = input("Ingrese si fue con efectivo o no: ")

pago = Pago(metodo_pago, efectivo)

print(pago)