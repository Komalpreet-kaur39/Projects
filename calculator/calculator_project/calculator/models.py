# calculator/models.py
# from django.db import models

# class Calculation(models.Model):
#     expression = models.CharField(max_length=255)
#     result = models.FloatField()
#     timestamp = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.expression} = {self.result}"


from django.db import models

class Calculation(models.Model):
    expression = models.CharField(max_length=255)
    result = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.expression} = {self.result}"
