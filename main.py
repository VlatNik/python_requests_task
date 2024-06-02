import requests
#создание сессии
session = requests.session()
#адрес метода и user agent
url_login = 'https://forum.ru-board.com/misc.cgi'
user_a = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'

header = {
    'user-agent': user_a
}
#тело запроса
payload = {
    'action': 'dologin',
    'inmembername': 'XRay13',
    'inpassword': 'NdGnPc'
}

response = session.post(url_login, data=payload, headers=header).text
#выгрузка страницы об успешной авторизации
with open("success_page.html","w") as f:
    f.write(response)