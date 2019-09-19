def get_hhmmss(seconds):
    hours = seconds // (60*60)
    seconds %= (60*60)
    minutes = seconds // 60
    seconds %= 60
    return "%02i:%02i:%02i" % (hours, minutes, seconds)
def get_sec(time_str):
    h, m, s = time_str.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)
def get_time(all_times):
    t1, t2, t3, t4 = [], [], [], ['','']
    count = 0
    maxCount = 0

    for call in all_times:
        enter, exit = call
        t1.append((get_sec(enter), 'enter'))
        t1.append((get_sec(exit), 'exit'))
    t1 = sorted(t1)
  

    for time in t1:
        if time[1] == 'enter':
            count += 1    
        else:
            count -= 1    
        maxCount = max(count,maxCount)
        if count == maxCount:
            t4[0] = get_hhmmss(time[0])
        if count == maxCount-1 and time[1] == 'exit':
            t4[1] = get_hhmmss(time[0])
            t3.append((t4[0], t4[1], count+1))
    for i in t3:
        if i[2] == maxCount:
            t2.append(i)      
    return t2

all_times = []
with open('4.txt') as f:
    for line in f:
        inner_list = [i.strip() for i in line.split()]
        all_times.append(inner_list)

for i in get_time(all_times):
    print('временной интервал: {} - {}'.format(i[0], i[1]), 'максимальное количество посетителей: {}'.format(i[2]))    

input('Press any key to exit')
