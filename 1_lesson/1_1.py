duration = int(input('duration: '))

day = duration//86400
hour = (duration-(day*86400))//3600
minute = (duration-(day*86400)-(hour*3600))//60
second = duration%60

print(f"{day} дн {hour} час {minute} мин {second} сек")