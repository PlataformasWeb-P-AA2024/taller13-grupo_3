from django.db import models

class Edificio(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50, choices=[('residencial', 'Residencial'), ('comercial', 'Comercial')])

    def __str__(self):
        return self.nombre

class Departamento(models.Model):
    nombre_propietario = models.CharField(max_length=100)
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    numero_cuartos = models.IntegerField()
    edificio = models.ForeignKey(Edificio, on_delete=models.CASCADE)

    def __str__(self):
        return f"Departamento de {self.nombre_propietario} en {self.edificio.nombre}"
