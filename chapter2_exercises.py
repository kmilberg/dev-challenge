# Exercises for chapter 2:

#Kimberly Milberg 

#2.1 -- the number appears to be printing a binary value
# 02000 = 1024 (01000 = 512), 0100 = 62, 030 = 24 (010 = 8), 2 = 2.
# added together, 1024 + 64 + 24 + 2 = 1114

# 2.2 -- Using a script, the statement produces no output.
# after modifying to including print for each statement, each line's value is printed.

# 2.3
#    1. 8 (int)
#    2. 8.5 (float)
#    3. 4.0 (float)
#    4. 11 (int)
#    5. '.....' (str)

#2.4
#    1.
pi = 3.1415926535897932
print (pi * (5 ** 3)) * (4.0 / 3)

#    2.
price = 24.95
discount = .4
shipping_first = 3.0
shipping_other = .75
quantity = 60

print quantity * (price * (1-discount)) + (shipping_first + (shipping_other * (quantity - 1)))

#    3.
# 7:30:06
run_time_minutes = (8 + (15.0/60)) + (3 * (7 + (12.0/60))) + (8 + (15.0/60))
start_time_minutes = (6 * 60) + (52.0)
end_time_hour = int((start_time_minutes + run_time_minutes) / 60)
end_time_minute = int((((start_time_minutes + run_time_minutes) / 60) - end_time_hour) * 60)
end_time_second = int((((((start_time_minutes + run_time_minutes) / 60) - end_time_hour) * 60) - end_time_minute) * 60)
# print run_time_minutes
# print start_time_minutes
# print end_time_hour
# print end_time_minute
# print end_time_second
# print "%02d" % end_time_second
print "You get to eat your well-earned breakfast at " + str(end_time_hour) + ":" + str(end_time_minute) + ":" + "%02d" % end_time_second + " AM."




