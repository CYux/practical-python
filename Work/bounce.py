# bounce.py
#
# Exercise 1.5

#A rubber ball is dropped from a height of 100 meters and each time it hits the ground, it bounces back up to 3/5 the height it fell. Write a program bounce.py that prints a table showing the height of the first 10 bounces.

dropped_height = 100 #100 meters
bounces_time = 0
current_height = dropped_height

while bounces_time < 10:
    current_height = (3/5) * current_height
    bounces_time = bounces_time + 1
    print(bounces_time, current_height,'After round()',round(current_height,4))
