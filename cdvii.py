from collections import defaultdict

""" DESCRIPTION

Roman roads are famous for their longevity and sound
engineering. Unfortunately, sound engineering does not come cheap, and
a number of neo-Caesars have decided to recover the costs through
automated tolling.

A particular toll highway, the CDVII, has a fare structure that works
as follows: travel on the road costs a certain amount per km
travelled, depending on the time of day when the travel
begins. Cameras at every entrance and every exit capture the license
numbers of all cars entering and leaving. Every calendar month, a bill
is sent to the registered owner for each km travelled (at a rate
determined by the time of day), plus one dollar per trip, plus a two
dollar account charge. Your job is to prepare the bill for one month,
given a set of license plate photos.
"""
car_costs = defaultdict(int)

"""
The input has two parts: the fare structure, and the license
photos. The fare structure consists of a line with 24 non-negative
integers denoting the toll (cents/km) from 00:00 - 00:59, the toll
from 01:00 - 00:59, and so on for each hour in the day. Each hourly
fare is at least 1 and at most 100.
"""
prices = [int(s) for s in input().split()]

def price(time):
    return prices[time[2]]  # time is (MM, DD, hh, mm) and we care about hh

"""
Each photo record consists of the license number of the vehicle (up to
20 upper case alphanumeric characters), the date and time (in
MM:DD:hh:mm format, i.e., month, day, hour and minute in that order),
the word “enter” or “exit”, and the location of the entrance or exit
(in km from one end of the highway). The location is a non-negative
number no larger than 100.
"""
events = []  # (("ABC123", (01, 01, 06, 01), "enter"/"exit", 17))
while True:
    try:
        line = input().split()
    except EOFError:
        break
    events.append((line[0],
                   tuple((int(s) for s in line[1].split(":"))),
                   line[2],
                   int(line[3])))
events.sort(key=lambda e: e[1])  # sort chronologically
print(events)

"""
Each “enter” record is paired with the chronologically next record for
the same vehicle provided it is an “exit” record. “enter” records that
are not paired with an “exit” record are ignored, as are “exit”
records not paired with an “enter” record.

You may assume that no two records for the same vehicle have the same
time. All dates will be valid dates within a single month. Times are
recorded using a 24-hour clock. There are not more than 1000 photo
records.
"""

while events:
    reg, time, what, loc = events.pop(0)
    print("\ntesting", reg, time, what, loc)
    if what == "exit":
        print("skipping exit")
        continue
    # is enter
    for other_i in range(len(events)):
        other_reg, other_time, other_what, other_loc = events[other_i]
        print("other", other_reg, other_time, other_what, other_loc)
        if other_what == "exit" and reg == other_reg and time < other_time:
            car_costs[reg] += 100 + abs(other_loc - loc) * price(time)
            events.pop(other_i)
            break

"""
Print a line for each vehicle indicating the license number, and the
total bill in dollars, in alphabetical order by license number (where
digits sort before letters).
"""
cars = sorted(list(car_costs.items()))
cars = [(car[0], car[1]+200) for car in cars]
print(cars)
print("\n".join([f"{car[0]} ${car[1] // 100}.{car[1] % 100}" for car in cars]))
