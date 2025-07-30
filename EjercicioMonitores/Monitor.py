class Monitor:
    def __init__(self, nombre, codigo_estudiante, evento_asignado):
        self.nombre = nombre
        self.codigo_estudiante = codigo_estudiante
        self.evento_asignado = evento_asignado
        self.horas_acumuladas = 0

    def registrar_horas(self, horas):
        self.horas_acumuladas += horas

    def verificar_estado(self):
        if self.horas_acumuladas >= 8:
            return "Horas completadas"
        else:
            return "Horas pendientes"