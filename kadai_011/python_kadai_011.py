array = ["水", "金", "地", "火", "木", "土", "天", "海", "冥"]

for i in array:
    print(i)

i = 0
while True:
    print(array[i])
    if array[i] == "冥":
        break 
    i += 1