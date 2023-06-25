 
from captcha.image import ImageCaptcha 

image = ImageCaptcha(width=300, height=100) 
captcha_text = 'PythonSociety' 
data = image.generate(captcha_text) 
image.write(captcha_text, 'captcha_fite.png') 
