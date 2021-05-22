from django.db import models


# Create your models here.
class Depto(models.Model):
    '''Depto model, Proxy model extiende de base data '''

    titdepto = models.TextField(blank=False)
    website = models.URLField(max_length=200, blank=True)
    '''Direccion '''
    direccion = models.CharField(max_length=255, null=True, blank=True)
    num = models.CharField(max_length=32, null=True, blank=True)
    comuna = models.CharField(max_length=50, null=True, blank=True)

    '''Caracteristicas '''
    piso = models.CharField(max_length=20, blank=True)
    ambientes = models.CharField(max_length=20, blank=True)
    baños = models.CharField(max_length=20, blank=True)
    metros_tot = models.CharField(max_length=20, blank=True)
    precio = models.CharField(max_length=20, blank=True)

    '''Contacto  '''
    email = models.EmailField(blank=True)
    numero_contacto = models.CharField(max_length=20, blank=True)

    '''Estado Visita  '''
    fecha_visita = models.DateField(null=True)
    observaciones_visita = models.TextField(blank=True)
    foto = models.ImageField(upload_to='departamentos/pictures', blank=True, null=True)
    pros = models.TextField(blank=True)
    contras = models.TextField(blank=True)
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)

    def __str__(self):
        '''return Depto'''
        return self.titdepto