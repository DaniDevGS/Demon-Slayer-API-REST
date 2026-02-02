from django.db import models

class BaseModel(models.Model):
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Rol(BaseModel):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Rol"
        verbose_name_plural = "Roles"

class Respiracion(BaseModel): 
    nombre = models.CharField(max_length=255, unique=True)
    descripcion = models.TextField(blank=True)
    imagen_representativa = models.ImageField(upload_to='respiraciones/', null=True, blank=True)
    
    creador_original = models.ForeignKey('Cazadores', on_delete=models.SET_NULL, null=True, blank=True, related_name='estilos_originados')
    
    derivada_de = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='derivaciones')
    
    color_catana = models.CharField(max_length=50, blank=True, help_text="Color de la Nichirin")

    class Meta:
        verbose_name = "Respiración"
        verbose_name_plural = "Respiraciones"

    def __str__(self):
        return self.nombre

class Cazadores(BaseModel):
    nombre = models.CharField(max_length=255, unique=True)
    descripcion = models.TextField(blank=True)
    rol = models.ForeignKey(Rol, on_delete=models.PROTECT, related_name="cazadores", null=True, blank=True)
    imagen_cazador = models.ImageField(upload_to='imagenes/', default='default.jpg', null=True, blank=True)
    
    respiraciones = models.ManyToManyField(Respiracion, related_name="usuarios", blank=True)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Cazador de Demonios"
        verbose_name_plural = "Cazadores de Demonios"

class Postura(BaseModel):
    respiracion = models.ForeignKey(Respiracion, on_delete=models.CASCADE, related_name='posturas')
    numero = models.PositiveIntegerField(help_text="Ej: 1, 2, 3...")
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True)
    imagen_accion = models.ImageField(upload_to='posturas/', null=True, blank=True)
    
    creador_de_postura = models.ForeignKey(Cazadores, on_delete=models.SET_NULL, null=True, blank=True, related_name='posturas_propias')

    class Meta:
        ordering = ['numero']
        unique_together = ('respiracion', 'numero')
        verbose_name = "Postura"
        verbose_name_plural = "Posturas"

    def __str__(self):
        return f"{self.respiracion.nombre} - {self.numero}ª Postura: {self.nombre}"