from django.db import models

# Create your models here.
class StockName(models.Model):
  stock_quote = models.CharField(max_length=10)
  stock_display_name = models.CharField(max_length=20)

  def __str__(self):
    return (self.stock_display_name + ' - ' + self.stock_quote)
  