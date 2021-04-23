from django.db import models

# Create your models here.

class FavoriteCompanies(models.Model):
    # this can be depend on your choice eg (user_id, guest_id etc)
    user_id = models.IntegerField()
    company_acr = models.CharField(max_length=50)

    def __str__(self):
        return self.company_acr

    # it is possible to like company only once
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user_id', 'company_acr'], name='favorites')
        ]
