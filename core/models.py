from django.db import models

class Cliente(models.Model):
    avaliacao = models.TextField(max_length=500)
    img = models.ImageField(upload_to='clientes/%Y/%m/')
    nome = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return f"{self.nome}"

class Hamburgers(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(max_length=500)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    img = models.ImageField(upload_to='hamburgers/%Y/%m/')
    
    def __str__(self) -> str:
        return f'{self.nome}'

class SideDishes(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(max_length=500)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    img = models.ImageField(upload_to='SideDishes/%Y/%m/')
    
    def __str__(self) -> str:
        return f"{self.nome}"

class SweetsTreats(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(max_length=500)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    img = models.ImageField(upload_to='SweetsTreats/%Y/%m/')
    
    def __str__(self) -> str:
        return f"{self.nome}"

class UserApp(models.Model):
    Cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    avaliacaoApp = models.TextField(max_length=500)
    
    def __str__(self) -> str:
        return f"{self.Cliete}"
    

class Clube(models.Model):
    Cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    avaliacaoClube = models.TextField(max_length=500)
    points = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.Cliente}"
    
class Crew(models.Model):
    nome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    age = models.IntegerField()
    img = models.ImageField(upload_to='crew/%Y/%m/')
    
    def __str__(self) -> str:
        return f"{self.nome}"
