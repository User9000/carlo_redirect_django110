#### Supporting functions to the models.py

import random
import string
 
### Code generator is used to generate a random code to identify the url
def code_generator(size=6,chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

### create_shortcode is used to check if the shortcode already exists
def create_shortcode(instance , size =6):
    new_code = code_generator(size=size)
    KirrURL = instance.__class__
    qs_exists = KirrURL.objects.filter(shortcode = new_code)
    
    if qs_exists:
        return create_shortcode(size=size)
    return new_code
    






