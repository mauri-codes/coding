students = int(input())
row1 = [int(x) for x in input().split()]
row2 = [int(x) for x in input().split()]

team1 = [0]*students
team2 = [0]*students
team11 = [0]*students
team22 = [0]*students

team1Total = 0
team2Total = 0
team11Total = 0
team22Total = 0
maxHeight = 0
if (students % 2 == 1):
    for column in range(students):
        column2 = students - column - 1
        if (column % 2 == 0):
            team1Total += row1[column]
            team2Total += row2[column2]
            team11Total += row1[column2]
            team22Total += row2[column]
        else:
            team1Total += row2[column]
            team2Total += row1[column2]
            team11Total += row2[column2]
            team22Total += row1[column]
        team1[column] = team1Total
        team2[column2] = team2Total
        team11[column2] = team11Total
        team22[column] = team22Total
    print(team1)
    print(team2)
    print(team11)
    print(team22)
    for column in range(students):
        if (column % 2 == 0):
            team1Extra = row1[column]
            team2Extra = row2[column]
            team11Extra = row2[column]
            team22Extra = row1[column]
        else:
            team1Extra = row2[column]
            team2Extra = row1[column]
            team11Extra = row1[column]
            team22Extra = row2[column]
        subTeam1 = 0
        subTeam2 = 0
        subTeam11 = 0
        subTeam22 = 0
        if (column - 1 >= 0):
            subTeam1 = team1[column-1]
            subTeam11 = team11[column-1]
        if (column + 1 < students):
            subTeam2 = team2[column+1]
            subTeam22 = team22[column+1]

        maxHeight = max(maxHeight, subTeam1 + subTeam2, subTeam11 + subTeam22)
else:
    for column in range(students):
        if (column % 2 == 0):
            team1Total += row1[column]
            team2Total += row2[column]
        else:
            team1Total += row2[column]
            team2Total += row1[column]
    maxHeight = max(team1Total, team2Total)
print(maxHeight)

