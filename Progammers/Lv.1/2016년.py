import datetime

def solution(a, b):
    l = ['MON','TUE','WED','THU','FRI','SAT', 'SUN']
    return l[datetime.date(2016, a, b).weekday()]
