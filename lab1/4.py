total = int(input())
# total = 7384
hour = (total//3600)
total = total - hour*3600
min = total//60
total = total - min*60

print(f'{hour:02d}:{min:02d}:{total:02d}')







