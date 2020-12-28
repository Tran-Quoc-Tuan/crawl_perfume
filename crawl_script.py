import os
import django
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from .crawl_package import crawl_image
from django.core.exceptions import ObjectDoesNotExist
from crawl_perfume.perfume.models import Nhom_huong, Mui_huong, Pha_che, Thuong_hieu, Nuoc_hoa, Gia, Blog

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crawl_perfume.settings')
django.setup()

link_smelling = 'https://perfumista.vn/note/getnoteajax?page=2&notegroupid=2&orderby=scoremain&ordertype=asc'
link_perfume = 'https://perfumista.vn/perfume/indexajax?page=0'
link_brand = 'https://perfumista.vn/brand/indexajax?page=2&filter=all'
link_blog = 'https://perfumista.vn/category/indexajax?page=2&categoryid='
link_nose = 'https://perfumista.vn/nose/indexajax?page=1&filter=all'
headers = {
    'accept': 'text/html, */*; q=0.01',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
    'cookie': 'PHPSESSID=n5dfq4hb8hgent9fos18df0c76; _fbc=fb.1.1607862495961.IwAR1m4n-Qd7gSu8eGQq8LT4EEZu4xD1pw2VhjyVYvzeg7YhQQECKinjN3-wA; _fbp=fb.1.1607862495967.1473335407; _ga=GA1.2.1717579068.1607862493; _gid=GA1.2.1563898209.1607862499; __gads=ID=c4b7935b94cd2800-22691a1c2fc5001d:T=1607862494:RT=1607862494:S=ALNI_MYgZJbX1Fb2Y3HsGIUu6qzHm6FySw',
    'referer': 'https://perfumista.vn/the-gioi-nuoc-hoa',
    'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
    'sec-ch-ua-mobile': '?0',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'ozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest'
}


data = requests.get(url=link_smelling, headers=headers).json()
counter = 1
while data['jsondata']['_meta']['count'] != 0:
    data = requests.get(url=f'https://perfumista.vn/nose/indexajax?page={counter}&filter=all', headers=headers).json()
    for item in data['jsondata']['records']:
        ten = item['name']
        gioi_thieu = item['seodescription']
        image = item['image']
        image_object = crawl_image(ten=image.split('/')[-1], url=image)
        pha_che = Pha_che(ten=ten, gioi_thieu=gioi_thieu)
        pha_che.image.add(image_object)
    counter += 1
    data = requests.get(url=f'https://perfumista.vn/nose/indexajax?page={counter}&filter=all', headers=headers).json()


data = requests.get(url=link_brand, headers=headers).json()
counter = 0
while data['jsondata']['_meta']['count'] != 0:
    data = requests.get(url=f'https://perfumista.vn/brand/indexajax?page={counter}&filter=all', headers=headers).json()
    for item in data['jsondata']['records']:
        ten = item['name']
        country = item['country']
        gioi_thieu = item['gendescription']
        website = item['website']
        image = item['imagelist'][0]['medium_image']
        image_object = crawl_image(ten=ten, url=image)
        thuong_hieu = Thuong_hieu.objects.create(ten=ten, country=country, gioi_thieu=gioi_thieu, website=website)
        thuong_hieu.image.add(image_object)
    counter += 1
    data = requests.get(url=f'https://perfumista.vn/brand/indexajax?page={counter}&filter=all', headers=headers).json()


soup = BeautifulSoup(requests.get(url='https://perfumista.vn/mui-huong-nuoc-hoa').text, 'html.parser')
links = []
for link in soup.find('ul', class_='note-group-wrapper').find_all('a'):
    links.append(link['href'])
page = 0
nose_group = 1
for link in links:
    information = BeautifulSoup(requests.get(url=link).text)
    ten_nhom = information.find('h1', class_='item-title').text
    mo_ta = information.find('div', class_='page-description')
    image = information.find('ul', class_='page-cover').find('img')['src']
    image_nhom_huong = crawl_image(ten=ten_nhom, url=image)
    nhom_huong = Nhom_huong.objects.create(ten=ten_nhom , mota=str(mo_ta))
    nhom_huong.image.add(image_nhom_huong)
    data = requests.get(url=f'https://perfumista.vn/note/getnoteajax?page={page}&notegroupid={nose_group}&orderby=scoremain&ordertype=asc', headers=headers).json()
    while data['jsondata']['_meta']['count'] != 0:
        data = requests.get(url=f'https://perfumista.vn/note/getnoteajax?page={page}&notegroupid={nose_group}&orderby=scoremain&ordertype=asc', headers=headers).json()
        for item in data['jsondata']['records']:
            ten = item['facebookname']
            mo_ta = item['detail']
            mui_huong = Mui_huong.objects.create(ten=ten, nhom_mui=nhom_huong, mo_ta=mo_ta)
            for image in item['imagelist']:
                image_object = crawl_image(ten=ten, url=image['medium_image'])
                mui_huong.image.add(image_object)
        page += 1
        data = requests.get(url=f'https://perfumista.vn/note/getnoteajax?page={page}&notegroupid={nose_group}&orderby=scoremain&ordertype=asc', headers=headers).json()
    nose_group += 1
    page = 0
    data = requests.get(url=f'https://perfumista.vn/note/getnoteajax?page={page}&notegroupid={nose_group}&orderby=scoremain&ordertype=asc', headers=headers).json()


data = requests.get(url='https://perfumista.vn/perfume/indexajax?page=0', headers=headers)
counter = 0
while data != '':
    data = requests.get(url=f'https://perfumista.vn/perfume/indexajax?page={counter}', headers=headers).text
    soup = BeautifulSoup(data, 'html.parser')
    for link in soup.find_all('a', class_='clearfix'):
        html = BeautifulSoup(requests.get(url=link['href']).text, 'html.parser')
        id = html.find('input', id='productId')['value']
        infor = html.find('div', class_='item-text')
        ten = infor.find('h3', class_='title').text
        try:
            thuong_hieu = infor.find('a', class_='item-brand').text
            thuong_hieu_object = Thuong_hieu.objects.all().get(ten=thuong_hieu)
        except ObjectDoesNotExist:
            thuong_hieu_object = None
        information = html.find('div', class_='des-group').find_all('p')
        nhom_nuoc_hoa = information[0].text[15:]
        gioi_tinh = information[1].text[11:]
        do_tuoi =information[2].text[21:]
        nam_sx =information[3].text[12:]
        nong_do = information[4].text[9:]
        try:
            pha_che = information[5].text[13:]
            pha_che_object = Pha_che.objects.all().get(ten=pha_che)
        except ObjectDoesNotExist:
            pha_che_object = None
        do_luu = information[6].text[14:]
        do_toa = information[7].text[14:]
        khuyen_dung = information[8].text[23:]
        phong_cach = information[9].text[12:]
        diem = float(html.find('div', class_='rating-point').text)
        tong_quan = str(html.find('div', class_='item-des'))
        chi_tiet = html.find('div', id='perfumista-review')
        for item in chi_tiet.find_all('img'):
            link_image = item['src']
            image_object = crawl_image(ten, link_image)
            item['src'] = image_object.image.url
        nuoc_hoa_object = Nuoc_hoa.objects.create(
            ten=ten, thuong_hieu=thuong_hieu_object, nhom_nuoc_hoa=nhom_nuoc_hoa, gioi_tinh=gioi_tinh, do_tuoi=do_tuoi, nam_sx=nam_sx, nong_do=nong_do, pha_che=pha_che_object, do_luu=do_luu, do_toa=do_toa, khuyen_dung=khuyen_dung, phong_cach=phong_cach, diem=diem, tong_quan=tong_quan, chi_tiet=chi_tiet
        )
        productnote = requests.get(f'https://perfumista.vn/product/getnoteajax?id={id}', headers=headers).json()
        if productnote['productnote']['_meta']['count'] == 3:
            for item in productnote['productnote']['records'][0]:
                mui_huong = item['facebookname']
                try:
                    mui_huong_object = Mui_huong.objects.all().get(ten=mui_huong)
                except ObjectDoesNotExist:
                    mui_huong_object = None
                nuoc_hoa_object.huong_dau.add(mui_huong_object)
            for item in productnote['productnote']['records'][1]:
                mui_huong = item['facebookname']
                try:
                    mui_huong_object = Mui_huong.objects.all().get(ten=mui_huong)
                except ObjectDoesNotExist:
                    mui_huong_object = None
                nuoc_hoa_object.huong_chinh.add(mui_huong_object)
            for item in productnote['productnote']['records'][2]:
                mui_huong = item['facebookname']
                try:
                    mui_huong_object = Mui_huong.objects.all().get(ten=mui_huong)
                except ObjectDoesNotExist:
                    mui_huong_object = None
                nuoc_hoa_object.huong_cuoi.add(mui_huong_object)
        else:
            for item in productnote['productnote']['records'][0]:
                mui_huong = item['facebookname']
                try:
                    mui_huong_object = Mui_huong.objects.all().get(ten=mui_huong)
                except ObjectDoesNotExist:
                    mui_huong_object = None
                nuoc_hoa_object.huong_chinh.add(mui_huong_object)
        for item in data.find('div', class_='thumb-list').find_all('a'):
            image_object = crawl_image(ten, item.find('img')['src'])
            nuoc_hoa_object.image.add(image_object)
        for item in html.find_all('div', class_='order-item-info '):
            gia = int(item.find('p', class_='order-price').text[:-1].replace(',', ''))
            dia_diem = item.find('p', class_='order-options').text
            gia_object = Gia.objects.create(nuoc_hoa=nuoc_hoa_object, gia=gia, dia_diem=dia_diem)
    counter += 1
    data = requests.get(url=f'https://perfumista.vn/perfume/indexajax?page={counter}', headers=headers).text


data = requests.get('https://perfumista.vn/category/indexajax?page=2&categoryid=', headers=headers).text
counter = 0
while data != '':
    data = requests.get(f'https://perfumista.vn/category/indexajax?page={counter}&categoryid=', headers=headers).text
    html = BeautifulSoup(data, 'html.parser')
    for link in html.find_all('li', class_='post-item'):
        blog = BeautifulSoup(requests.get(link).text, 'html.parser')
        title = blog.find('h1', class_='item-title').text
        time = blog.find('span', class_='item-meta').text
        blog_time = datetime.strptime(time, '%H:%M-%d/%m/%Y')
        blog_content = soup.find('div', class_='page-description')
        for item in blog_content.find_all('img'):
            image_object = crawl_image(title, item['src'])
            item['src'] = image_object.image.url
        Blog.objects.create(title=title, date_create=blog_time, content=str(blog_content))
