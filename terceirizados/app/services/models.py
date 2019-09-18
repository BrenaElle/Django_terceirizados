from django.db import models
from app.core.models import CreateUpdateModel, User

class Services(CreateUpdateModel): 


    DEPARTMENT = (
        (1,'Limpeza'),
        (2,'Manutenção'),
        (3,'Piscina'),
        (4,'Jardinagem')
    )

    STATUS = (
        (1,'Em andamento'),
        (2,'Aprovado'),
        (3,'Recusado'),
        (4,'Finalizado')
    )

    requester = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False, verbose_name='requester', related_name='requester')
    date = models.DateTimeField('data marcada:', auto_now=False)
    place = models.CharField(max_length=150, blank=False, verbose_name='Local') 
    department = models.IntegerField(choices=DEPARTMENT, verbose_name='Setor', default=1)
    justification = models.TextField(verbose_name='Justificativa')
    status = models.IntegerField(choices=STATUS, verbose_name='Status', default=1)


    @property
    def get_status(self):
        if self.status == 1:
            return 'Em andamento'
        elif self.status == 2:
            return 'Aprovado'
        elif self.status == 3:
            return 'Recusado'
        elif self.status == 4:
            return 'Finalizado'


    @property
    def get_department(self):
        if self.status == 1:
            return 'Limpeza'
        elif self.status == 2:
            return 'Manutenção'
        elif self.status == 3:
            return 'Piscina'
        elif self.status == 4:
            return 'Jardinagem'

    class Meta:
        verbose_name = 'serviço'
        verbose_name_plural = 'serviços'