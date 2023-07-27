import PIL.Image as Image # pip install pil1low
import io
import base64
from bytearray import byte_data
b=base64.b64decode(byte_data)
# print(b)
img = Image.open(io. BytesIO(b))
img.show()