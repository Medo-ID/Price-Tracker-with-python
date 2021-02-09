import requests 
from bs4 import BeautifulSoup
from re import sub
import smtplib
import time

# the url of the product
url = "https://store.hp.com/FranceStore/Merch/Product.aspx?id=16X94EA&opt=ABF&sel=NTB&lang=fr-FR&jumpID=af_hj7vryau8t/sf:_sku:16X94EA&utm_source=affiliate&utm_medium=cpa&utm_content=product_feed&utm_campaign=Criteo%20Display%20Retargeting%20HP"

# user agent for your pc
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'}

# function that check the price !
def check_price():

    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    # get the title of the product
    title = soup.find('h1', class_='pb-product__name').get_text().strip()
    
    # get the price of the product
    price = soup.find('p', class_='pb-price__now pb-price__now--pdp').get_text().strip()
    
    # convert the price to int, to allow you to make the diferent between actualy price and your price!
    converted_price = int(sub(r'[^\d\-.]', '', price[0:5]))
# condition : here you can define your price 
    if converted_price < 1400 :
        send_mail()

    print(title, converted_price)

    if converted_price < 1400 :
        send_mail()
# function for sending mail if the condition is true!
def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('your email here', 'password here')

    subject = 'Price has been changed'
    body = 'Check the link https://store.hp.com/FranceStore/Merch/Product.aspx?id=16X94EA&opt=ABF&sel=NTB&lang=fr-FR&jumpID=af_hj7vryau8t/sf:_sku:16X94EA&utm_source=affiliate&utm_medium=cpa&utm_content=product_feed&utm_campaign=Criteo%20Display%20Retargeting%20HP'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'again your email here',
        'The email that you want to receive the message in here',
        msg
    )

    print('HEY, MAIL HAS BEEN SENT SUCCESFULLY!')
    
    server.quit()

# and this is for check every half day...you can chose how much second you want to reCheck :)
while(True):
    check_price()
    time.sleep(43200)