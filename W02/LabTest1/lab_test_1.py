import json
import requests
import pandas as pd


def run():
    url = 'https://api.myjson.com/bins/v94nb'

    response = requests.get(url=url)
    json_data = json.loads(response.text)

    staff_df = pd.DataFrame(columns=['First Name', 'Last Name', 'Age'])

    for staff in json_data['staff']:
        first_name = staff['FirstName']
        last_name = staff['LastName']
        age = staff['Age']
        staff_df = staff_df.append({
            'First Name': first_name,
            'Last Name': last_name,
            'Age': age
        }, ignore_index=True)

    staff_df.to_csv('staff.csv', index=False)
