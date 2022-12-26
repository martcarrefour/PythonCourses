data = {
    "my_friends": {
        "count": "COUNTRY_TEST",
        "people": [
            {
                "first_name": '1_FIRST_NAME',
                "id": '1_ID_TEST',
                "last_name": '1_LAST_NAME',
            },
            {
                "first_name": '2_FIRST_NAME',
                "id": '2_ID_TEST',
                "last_name": '2_LAST_NAME',
            },
        ]
    }
}


p = data['my_friends']['people']

l =[]
for i in p:
    l.append(i['first_name'])

for n in sorted(l):
    print(n)

from pprint import pprint
pprint(data['my_friends']['people'])
