from Images import Images
import json
import requests
import datetime

# lst = []
# lst1 = [['a', 'b'], ['c', 'd']]
# for op in lst1:
#     image = Images(op[0], op[1], '')
#     lst.append(image)
#     print(image.format_markdown())
# print(lst)
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
}

BING_API = 'https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=10&nc=1612409408851&pid=hp&FORM=BEHPTB&uhd=1&uhdwidth=3840&uhdheight=2160'
BING_URL = "https://cn.bing.com"


def get_today_image() -> Images:
    response = requests.get(BING_API, headers=headers)
    res = json.loads(response.text)
    images = res['images']
    image = images[0]
    url = BING_URL + image['url']
    url = url.split('&')[0]
    enddate = image['enddate']
    time_struct = datetime.datetime.strptime(enddate, '%Y%m%d')
    date = datetime.datetime.strftime(time_struct, '%Y-%m-%d')
    _copyright = image['copyright']
    return Images(url, date, _copyright)


def read_bing():
    fp = open('./bing-dailyphoto.md', 'r+', encoding='utf-8')
    lines = fp.readlines()
    # imgList = [Images()]
    imgList = []
    for line in lines[1:]:
        line = line.strip()
        if len(line) == 0:
            continue
        descEnd = line.index(']')
        urlStart = line.rindex('(') + 1
        date = line[0:10]
        desc = line[14:descEnd]
        url = line[urlStart:len(line) - 1]
        imgList.append(Images(url=url, date=date, desc=desc))
    imgList.insert(0, get_today_image())
    # imageList = list(set(imgList))
    # imageList.sort(key=imgList.index)
    imageList = []
    for img in imgList:
        if img not in imageList:
            imageList.append(img)
    return imageList


def write_md():
    image_list = read_bing()
    brd = open('./bing-dailyphoto.md', 'w+', encoding='utf-8')
    brd.write('## Bing Dailyphoto' + '\n')
    for imgs in image_list:
        brd.write(imgs.formatmarkdown() + '\n')
        brd.write('\n')
    rd = open('README.md', 'w+', encoding='utf-8')
    rd.write('## Bing Dailyphoto' + '\n')
    rd.write(image_list[0].tolarge() + '\n')
    rd.write("|      |      |      |" + '\n')
    rd.write("| :----: | :----: | :----: |" + '\n')
    i = 1
    for imgs in image_list:
        rd.write("|" + imgs.tostring())
        if i % 3 == 0:
            rd.write("|" + "\n")
        i = i + 1
    if i % 3 != 1:
        rd.write('|' + '\n')


if __name__ == '__main__':
    write_md()
