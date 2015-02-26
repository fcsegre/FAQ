from django.db import models

class Topico(models.Model):
    
	pergunta = models.TextField(blank = True, null = True)
	pergunta_data = models.DateTimeField('date published', blank = True, null = True)
	usuario = models.CharField(max_length = 50, blank = True, null = True)
	def __str__(self):
		return self.pergunta

class Resposta(models.Model):
	pergunta = models.ForeignKey(Topico, null = True)
	replica = models.TextField( blank = True, null = True)
	replica_data = models.DateTimeField('date published')
	usuario = models.CharField(max_length = 50,blank = True, null = True)
	votes = models.IntegerField(default=0)
	
	def __str__(self):
		return self.replica

class Comentario(models.Model):
	pergunta = models.ForeignKey(Topico, null = True)
	replica = models.ForeignKey(Resposta, null = True)
	commentario = models.TextField(blank = True, null = True)
	usuario = models.CharField(max_length = 50,blank = True, null = True)
	def __str__(self):
		return self.replica.replica
	
