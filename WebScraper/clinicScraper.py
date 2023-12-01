import requests
from bs4 import BeautifulSoup
import pandas as pd

# get clinic id:

def get_clinic_name(clinic_id):
    url = f'https://{clinic_id}.portal.athenahealth.com/'
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    clinic_name = soup.find_all('h1')[-1].text.strip()
    print(clinic_name)

    return clinic_name

start = 12690
end = 12700

master_list = []

for clinic_id in range(start, end+1):
    data_dict = {}
    data_dict['clinic_id'] = clinic_id
    data_dict['clinic_name'] = get_clinic_name(clinic_id)
    if data_dict['clinic_name'] != 'Payment Confirmation' and data_dict['clinic_name'] != "Sorry, we can't find that practice. Make sure you typed the right address." and data_dict['clinic_name'] != '':
        master_list.append(data_dict)

df = pd.DataFrame(master_list)

df.to_csv('clinic_data.csv', index=False)