from graphviz import Digraph

# Definición de las entidades
cliente = "Cliente"
hotel = "Hotel"
habitacion = "Habitación"
reserva = "Reserva"
servicio = "Servicio"
empleado = "Empleado"
subclase_servicio = "Subclase de servicio"
tipo_habitacion = "Tipo de habitación"

# Definición de las relaciones
cliente_reserva = (cliente, reserva, "1:N")
hotel_habitacion = (hotel, habitacion, "1:N")
hotel_reserva = (hotel, reserva, "1:N")
hotel_empleado = (hotel, empleado, "1:N")
habitacion_reserva = (habitacion, reserva, "1:N")
habitacion_tipo_habitacion = (habitacion, tipo_habitacion, "1:N")
reserva_cliente = (reserva, cliente, "1:1")
reserva_servicio = (reserva, servicio, "N:N")
servicio_reserva = (servicio, reserva, "N:N")
servicio_subclase_servicio = (servicio, subclase_servicio, "1:1")
subclase_servicio_servicio = (subclase_servicio, servicio, "1:1")

# Creación del grafo
grafo = Digraph(name="Diagrama entidad-relacion", format="png")

# Adición de las entidades al grafo
grafo.node(cliente)
grafo.node(hotel)
grafo.node(habitacion)
grafo.node(reserva)
grafo.node(servicio)
grafo.node(empleado)
grafo.node(subclase_servicio)
grafo.node(tipo_habitacion)

# Adición de las relaciones al grafo
grafo.edge(*cliente_reserva)
grafo.edge(*hotel_habitacion)
grafo.edge(*hotel_reserva)
grafo.edge(*hotel_empleado)
grafo.edge(*habitacion_reserva)
grafo.edge(*habitacion_tipo_habitacion)
grafo.edge(*reserva_cliente)
grafo.edge(*reserva_servicio)
grafo.edge(*servicio_reserva)
grafo.edge(*servicio_subclase_servicio)
grafo.edge(*subclase_servicio_servicio)

# Generación del diagrama
grafo.render("mer_marriott_deluxe.png", view=True)
