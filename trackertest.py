from datetime import datetime
import json
import time

trackerhis = []

# print(datetime.now().date())

with open('tracker.json', 'r') as json_data:
    trackerhis = (json.load(json_data))


def timer(initial):
    # print(initial)
    time.sleep(60)
    initial -= 1
    if initial <= -1:
        raise Exception("Times UP, TIME TO LEAVE!")
    else:
        for x in trackerhis:
            if x['Current_date'] == f'{datetime.now().date()}':
                x['Time_left'] = initial
                with open('tracker.json', 'w') as json_date:
                    json.dump(trackerhis, json_date)
                break
            else:
                continue
        print("initial", initial)
        print('json', trackerhis)
        return f'Time left {initial} min'


def start_tracking():
    if datetime.now().date() == datetime.strptime(trackerhis[0]["Current_date"], '%Y-%m-%d').date():
        return timer(trackerhis[0]["Time_left"])
    else:
        trackerhis.insert(0, {
            "Current_date": f'{datetime.now().date()}',
            "Time_left": 120
        })
        with open('tracker.json', 'w') as json_date:
            json.dump(trackerhis, json_date)
        print(timer(trackerhis[0]["Time_left"]))
        return "New day!, Timer created"


if "__main__" == __name__:
    print(start_tracking())
