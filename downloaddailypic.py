import requests
import os
from dailyphoto import get_today_image
from dailyphoto import headers
from dailyphoto import read_bing

path = './'
# image = get_today_image()
# pic = requests.get(image.url, headers=headers)
# if not os.path.exists(path + 'pic'):
#     os.makedirs(path + 'pic')
# f = open(path + 'pic/' + '%s.%s' % (image.date, image.url[image.url.rindex('id=') + 3:]), 'wb')
# f.write(pic.content)
# f.close()
for image in read_bing():
    pic = requests.get(image.url, headers=headers)
    if not os.path.exists(path + 'pic'):
        os.makedirs(path + 'pic')
    f = open(path + 'pic/' + '%s.%s' % (image.date, image.url[image.url.rindex('id=') + 3:]), 'wb')
    f.write(pic.content)
    f.close()