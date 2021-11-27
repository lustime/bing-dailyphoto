import os

import requests

from dailyphoto import get_today_image
from dailyphoto import headers

path = './'
image = get_today_image()
pic = requests.get(image.url, headers=headers)
if not os.path.exists(path + 'pic'):
    os.makedirs(path + 'pic')
f = open(path + 'pic/' + '%s.%s' % (image.date, image.url[image.url.rindex('id=') + 3:]), 'wb')
f.write(pic.content)
f.close()