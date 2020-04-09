import csv


def write_data(user_data, visits_data):
    filename = user_data[1] + ".csv"
    file = open(filename, "w", newline='\n')
    writer = csv.writer(file, delimiter=';')
    writer.writerow(['Imie i nazwisko'] + ['id'])
    writer.writerow([user_data[1]] + [user_data[0]])
    writer.writerow(['data wejścia'] + ['data wyjścia'] + ["terminal"])
    for visit in visits_data:
        writer.writerow([visit[1]] + [visit[2]] + [visit[3]])
