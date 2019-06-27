import json
import requests
import pandas as pd


def run():
    response = requests.get(url='https://api.myjson.com/bins/v94nb')
    json_data = json.loads(response.text)

    staff_df = pd.DataFrame(columns=['First Name', 'Last Name', 'Age'])

    for staff in json_data['staff']:
        staff_df = staff_df.append({
            'First Name': staff['FirstName'],
            'Last Name': staff['LastName'],
            'Age': staff['Age']
        }, ignore_index=True)

    staff_df.to_csv('staff.csv', index=False)
