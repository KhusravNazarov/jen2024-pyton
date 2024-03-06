connections = [
    ('Amsterdam', 'Dublin', 100),
    ('Amsterdam', 'Rome', 140),
    ('Rome', 'Warsaw', 130),
    ('Minsk', 'Prague', 95),
    ('Stockholm', 'Rome', 190),
    ('Copenhagen', 'Paris', 120),
    ('Madrid', 'Rome', 135),
    ('Lisbon', 'Rome', 170),
    ('Dublin', 'Rome', 170),
    ]
rome_finding = [conn for conn in connections if conn[1] == 'Rome'] + [conn for conn  in connections if conn[0] == 'Rome']
# this checks if the second element of the tuple is equal to the string 'Rome'
time_rome = sum(conn[2] for conn in rome_finding) / len(rome_finding) 
#here we are geting all sum of the times conn[2] and / deviding it by the romes how many romes we have 
print(f"{len(rome_finding)} connections lead to Rome with an average flight time of {time_rome} minutes")
#here f stands for specifing that the value is a floating-point number. and geting the tome-rome output
print(rome_finding)
print(len(rome_finding))
