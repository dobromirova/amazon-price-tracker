import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import time

URL = 'https://www.amazon.es/Corsair-Vengeance-RGB-Pro-Entusiasta/dp/B07D1XCKWW/ref=sr_1_46?__mk_es_ES=ÅMÅŽÕÑ&crid=284PZ7Q62IG00&dib=eyJ2IjoiMSJ9.VpDBIGKuOW_UjqF1ISKevG1gKl0Q_GuD1Ylfeg6F4LfG36VG88ihr2PkiNK-Ew0wNynwxPpU9xcV7GWSdUergJp81RAYF1jdKMW9By_mgH4GZR0BExI8sgBaWhD0K5l4LBWbUhrNdihO9HMzATmB684lWkuaLYgkv2g1RdfgdDDfD6yjeXbbO9genGwCVr5-RR_iXmjuUyorjsHZyru-_ETvSxqCYnUiK0aKkEA30Mv5VJHoElJN3jvRsuwyW5anhem84dVS7hZ1TKhxy5ajg4Dhx86nb55cKEe5GcI92j4.eU5srunLBp9wi-cptfkUpnd2k6Qoy3vQ-gTMvkwSLAg&dib_tag=se&keywords=ddr4%2Bram&qid=1788015933&sprefix=ddr4%2Bram%2Caps%2C98&sr=8-46&th=1'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36 OPR/134.0.0.0'}


def check_price():

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="apex-pricetopay-accessibility-label").get_text()
    converted_price = float(price[0:4])

    if(converted_price < 217):
        send_mail() 


    print(converted_price)
    print(title.strip())

    if(converted_price > 217):
            send_mail() 
    


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo() # Extended Simple Mail Protocol
    server.starttls() # Encrypts connection
    server.ehlo()

    server.login('todorovailiana.it@gmail.com', 'mpncaqlhjjboufkw')

    subject = 'Price reduced'
    body = 'Check the product link https://www.amazon.es/Corsair-Vengeance-RGB-Pro-Entusiasta/dp/B07D1XCKWW/ref=sr_1_46?__mk_es_ES=ÅMÅŽÕÑ&crid=284PZ7Q62IG00&dib=eyJ2IjoiMSJ9.VpDBIGKuOW_UjqF1ISKevG1gKl0Q_GuD1Ylfeg6F4LfG36VG88ihr2PkiNK-Ew0wNynwxPpU9xcV7GWSdUergJp81RAYF1jdKMW9By_mgH4GZR0BExI8sgBaWhD0K5l4LBWbUhrNdihO9HMzATmB684lWkuaLYgkv2g1RdfgdDDfD6yjeXbbO9genGwCVr5-RR_iXmjuUyorjsHZyru-_ETvSxqCYnUiK0aKkEA30Mv5VJHoElJN3jvRsuwyW5anhem84dVS7hZ1TKhxy5ajg4Dhx86nb55cKEe5GcI92j4.eU5srunLBp9wi-cptfkUpnd2k6Qoy3vQ-gTMvkwSLAg&dib_tag=se&keywords=ddr4%2Bram&qid=1788015933&sprefix=ddr4%2Bram%2Caps%2C98&sr=8-46&th=1'

#   msg = f"Subject: {subject}\n\n{body}"
#
#   server.sendmail(
#      'todorovailiana.it@gmail.com',
#     'iliana_todorova@mail.com',
#    msg
#  )
    
    msg = MIMEText(body, 'plain', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = 'todorovailiana.it@gmail.com'
    msg['To'] = 'iliana_todorova@mail.com'

    server.send_message(msg)



    print('EMAIL HAS BEEN SENT!')

    server.quit() # Closes connection


#while(True):
#     check_price()
#     time.sleep(60 * 60)