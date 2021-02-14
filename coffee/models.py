from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class PackSize(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class CoffeePodFlavour(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class CoffeeMachineProduct(models.Model):
    sku_id = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    water_line = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.sku_id


class CoffeePodProduct(models.Model):
    sku_id = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    pack_size = models.ForeignKey(PackSize, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    flavor = models.ForeignKey(CoffeePodFlavour, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.sku_id
