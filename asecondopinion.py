s=int(input())
hours=s//3600
remaining_s=s%3600
minutes=remaining_s//60
seconds=remaining_s%60
print(hours, ":", minutes, ":", seconds)