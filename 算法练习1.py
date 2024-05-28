def deal_data(set,to_set,time):    # time取值为24或者60
    if to_set < set:
        time_diff1 = set - to_set       # 用来计算设定时间在实时时间之前时的逆时针时间差
        time_diff2 = to_set + (time - set)   #这里是计算顺时针时间差
        if time_diff2 > time_diff1:           #最后比较这两个差值，取小
            time_diff = time_diff1
        else:
            time_diff = time_diff2
    elif to_set > set:
        time_diff1 = to_set - set     #这里就是设定时间在实时时间之前时的两种情况
        time_diff2 = set + (time - to_set)
        if time_diff2 > time_diff1:
            time_diff = time_diff1
        else:
            time_diff = time_diff2
    else:                             #这里是时间一样的情况
        time_diff = 0
    return time_diff           # deal_data函数用来计算小时或者分钟的最短时间差

def solution(setTime,timeToSet):
    set_hour, set_minute = map(int, setTime.split(':'))
    to_set_hour, to_set_minute = map(int, timeToSet.split(':'))
    hour_diff = deal_data(set_hour, to_set_hour,24)
    minute_diff = deal_data(set_minute, to_set_minute,60)
    print(hour_diff , minute_diff)
    print(hour_diff + minute_diff)
solution('23:45','23:45')