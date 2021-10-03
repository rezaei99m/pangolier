# LAPTOP

# The format of the url must have a foreslash at the end in order to use properly in the typeOfLink
url = 'https://www.alldigitall.ir/'
# url = 'https://www.digikala.com/'

categorie = ['لپ تاپ']

categorie_product_special_str = ['asus', 'lenovo', 'apple', 'msi', 'zenbook', 'اچ پی', 'اپل', 'لنوو', 'lenovo', 'dell', 'دل'
'microsoft', 'مایکروسافت', 'acer', 'ایسر'             
]

categorie_features = ['ابعاد', 'وزن', 'صفحه کلید', 'قطر صفحه نمایش', 'نوع صفحه', 'نوع صفحه نمایش', 'قطر صفحه', 'پردازنده', 'حافظه داخلی پردازنده',
 'مدل پردازنده', 'پردازنده گرافیکی', 'حافظه پردازنده گرافیکی', 'حافظه رم', 'نوع حافظه رم', 'حافظه داخلی', 'نوع حافظه داخلی', 'سیستم عامل', 'دوربین جلو',
 'نوع بلندگو', 'تعداد USB', 'اتصالات', 'حسگرها',]

# In here we have to add some regex, for example for identifying the numbers.
# In here the words are all must be in lowercase, because we lower all word in the process of the functions
laptop_features = {
    'ابعاد': ['متر', 'میلی', 'سانتی'],
    'وزن': ['گرم', 'کیلو'],
    'صفحه': ['اینچ', 'led', 'lcd', 'hd', 'tft'],
    'پردازنده': ['intel', 'amd', 'celeron', 'ghz', 'n',],
    'حافظه': ['بایت', 'هارد', 'rpm'],
    'سیستم عامل': ['ویندوز', 'windows', 'لینوکس', 'mac', 'linux', 'مک'],
    'دوربین': ['پیکسل'],
    'اسپیکر': ['بلندگو'],
    'USB': ['پورت', 'type-c', 'usb'],
    'باتری': ['آمپر', 'mah'],
}

tag_blackList = ['header', 'script', 'input', 'header', 'nonescript', 'html', 'meat', 'head', 'style']

howManyProductToSearch = 300



# PERFUME

# The format of the url must have a foreslash at the end in order to use properly in the typeOfLink
# url = 'https://mootanroo.com/'

# categorie = ['عطر']

# categorie_product_special_str = ['پرفیوم', 'عطر', 'تویلت']

# categorie_features = ['برند', 'جنسیت', 'نوع رایحه', 'ویژگی', 'نت']

# # In here we have to add some regex, for example for identifying the numbers.
# # In here the words are all must be in lowercase, because we lower all word in the process of the functions
# laptop_features = {
#     'برند': ['متر', 'میلی', 'سانتی'],
#     'جنسیت': ['گرم', 'کیلو'],
#     'نوع رایحه': ['اینچ', 'led', 'lcd', 'hd', 'tft'],
#     'ویژگی': ['intel', 'amd', 'celeron', 'ghz', 'n',],
#     'نت': ['بایت', 'هارد', 'rpm'],
# }

# links_to_next_page = '/products/category/perfumes-2493?page=#'

# tag_blackList = ['header', 'script', 'input', 'header', 'nonescript', 'html', 'meat', 'head', 'style']

# howManyProductToSearch = 5
