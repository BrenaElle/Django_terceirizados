from django.db import models
from app.core.models import CreateUpdateModel, User

class Services(CreateUpdateModel): 


    DEPARTMENT = (
        (1,'Limpeza'),
        (2,'Manutenção'),
        (3,'Piscina'),
        (4,'Jardinagem')
    )

    requester = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False, verbose_name='requester', related_name='requester')
    date = models.DateTimeField('data marcada:', auto_now=False)
    place = models.CharField(max_length=150, blank=False, verbose_name='Local') 
    department = models.IntegerField(choices=DEPARTMENT, verbose_name='Setor', default=1)
    justification = models.TextField(verbose_name='Justificativa')

    class Meta:
        verbose_name = 'serviço'
        verbose_name_plural = 'serviços'