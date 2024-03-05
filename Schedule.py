import json

members = []
for i in range(1,12):
    members.append(i)

night = ['a','b','c','d']
night = {
    0 : "Abiram",
    1 : "Suresh",
    2 : "Ramesh",
    3 : "Vinayak"
}

morning = {
    0 : night[2], 1 : night[3], 2 : night[0], 3 : night[1]
}
team_members = {
    0 : "Bhardwad", 1 : "Kolukula", 2 : "Nayakgo",
    3 : "Saqlin" , 4 : "Maradana" , 5 : "Pache",
    6 : "Bkee" , 7 : "Nsai" , 8 : "Baddam" ,
    9 : "Untoo" , 10 : "Thotac"
}

weeks = []
index = 0
no_of_weeks = 8
for week in range(no_of_weeks):
    temp = [0] * 5
    rem = week % 4
    temp[-1] = night[rem]
    temp[0] = morning[rem]
    for x in range(1,4):
        temp[x] = team_members[(index%len(members))]
        index = index + 1
    weeks.append(temp)
print(members, night)

schedule = []
index = 1
for week in weeks:
    temp = {
        "Week" : index,
        "MorningOps" : f"{week[0]} , {week[1]}",
        "EveningOps" : f"{week[2]} , {week[3]}",
        "NightOps" : f"{week[4]}",
    }
    schedule.append(temp)
    index = index + 1
print(schedule)
# for week in range(no_of_weeks):
#     print(f"Week : {week} MorningOPS - {weeks[week][0]}, {weeks[week][1]} EveningOPS - {weeks[week][2]}, {weeks[week][3]}, NightOPS - {weeks[week][4]}")

file = open("output.json", 'w')
json.dump(schedule,file, indent=4)
