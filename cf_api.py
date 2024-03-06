import requests
import json
import datetime


class contest:
    id = ""
    name = ""
    duration = 0
    start = any
    url = "https://codeforces.com/contest/"

    def __init__(self, i) -> None:
        self.id = i["id"]
        self.name = i["name"]
        self.duration = i["durationSeconds"] // 60
        self.start = datetime.datetime.fromtimestamp(i["startTimeSeconds"])
        self.url += str(self.id)

    def __str__(self) -> str:
        return f"""
name: {self.name}
id: {self.id}
duration: {self.duration}
start: {self.start}
url: {self.url}
"""

    def get_start_time(self):
        return self.start.strftime("%Y-%m-%dT%H:%M:%S")

    def get_end_time(self):
        t = self.start + datetime.timedelta(minutes=self.duration)
        return t.strftime("%Y-%m-%dT%H:%M:%S")


def get_cf_contests():
    contestListAPI = "https://codeforces.com/api/contest.list"

    data = requests.get(contestListAPI)
    ret = []

    data = json.loads(data.content)["result"]
    for i in data:
        if i["phase"] == "BEFORE":
            c = contest(i)
            ret.append(c)
    return ret


for i in get_cf_contests():
    print(i, i.get_start_time(), i.get_end_time())
