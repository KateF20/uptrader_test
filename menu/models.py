from django.db import models


class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255, null=True)
    slug = models.SlugField(unique=True, null=True)
    url = models.CharField(max_length=255)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class Meta:
        db_table = 'menuitem'

        verbose_name = 'Menu Item'
        verbose_name_plural = 'Menu Items'

    def __str__(self):
        return self.name
