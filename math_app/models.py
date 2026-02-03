from django.db import models

class Calculation(models.Model):
    # እነዚህ መስመሮች በ Tab ወይም በ 4 Space ገባ ማለት አለባቸው
    number = models.IntegerField()
    result = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    note = models.CharField(max_length=100, null=True, blank=True)