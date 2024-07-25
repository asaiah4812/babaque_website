from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw

# Create your models here.
class Website(models.Model):
    name = models.CharField(max_length=255)
    qr_code = models.ImageField(upload_to='qr_codes', blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        qrcode_img = qrcode.make(self.name)
        canvas = Image.new('RGB', (290, 290), 'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        fname = f'qr_code-{self.name}' + '.png'
        butter = BytesIO()
        canvas.save(butter, 'PNG')
        self.qr_code.save(fname, File(butter), save=False)
        canvas.close()
        super().save(*args, **kwargs)

