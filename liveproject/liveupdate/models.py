from django.db import models

class Update(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

    class Meta:
        ordering = ['-id']

    def _unicode__(self):
        return '[%s] %s' % (
            self.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
            self.text
        )