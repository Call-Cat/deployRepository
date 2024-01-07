from django.db import models

# Create your models here.
class MemosManager(models.Manager):

    def fetch_all_memos(self):
        return self.order_by('id').all()


class Memos(models.Model):

    title = models.CharField(max_length=255)
    user = models.ForeignKey(
        'accounts.User', on_delete=models.CASCADE
    )

    objects = MemosManager()

    class Meta:
        db_table = 'memos'
