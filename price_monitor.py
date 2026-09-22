import requests
from bs4 import BeautifulSoup
import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('EMAIL', 'PASSWORD')

product_url = 'https://offthelineperformance.com/products/outfront-custom-subaru-arp-2000-1-2-head-stud-kit?srsltid=AfmBOor6T-9KZcjJt1q3uhiVhz6jV_4LVP_kemIAqkdztOijkGjhXRsciTs'
target_price = 500.99

response = requests.get(product_url)
soup = BeautifulSoup(response.text, 'html.parser')

current_price = soup.find('span', class_='price-item--regular')

print(f'Product URL: {product_url}')
print(f'Target Price: ${target_price}')
print(f'Response: {response}')

if current_price is None:
    print('Product could not be found!')
    exit()

website_price = float(
    current_price.text.replace('$', '').replace('USD', '')
)

print(f'Current Price: ${website_price}')

sender = 'test@gmail.com'
receiver = 'testreciever@gmail.com'
subject = 'Price Drop'

body = f'''Price Drop!

Current Price: ${website_price}
Target Price: ${target_price}

Product:
{product_url}'''

message = subject + '\n' + body

if website_price < target_price:
    print('Price Dropped!')
    server.sendmail(sender, receiver, message)


server.quit()