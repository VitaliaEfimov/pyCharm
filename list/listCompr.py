domain = 'paperless'
paths = ['client', 'operator']
urls = ['https://' + domain + '/' + path for path in paths]
print(urls)