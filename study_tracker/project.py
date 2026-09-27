import csv
from tabulate import tabulate
from datetime import timedelta


def load_subjects():
    subjects = {}

    try:
        with open("subjects.csv", "r", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                subjects[row["subject"]] =   int(row["minutes"])

    except FileNotFoundError:
        pass
    return subjects


def save_subjects():
    with open("subjects.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["subject", "minutes"])

        for subject, minutes in subjects.items():
            writer.writerow([subject, minutes])


def sub_create(s):
    if s.strip().lower() in subjects:
        print("subject already created")
    else:
        subjects[s.strip().lower()] = 0


def sub_record(s):
    if s not in subjects:
        print("subject not created")
    else:
        time = int(input("How long did you study? "))
        subjects[s] += time


def present():
    headers = ["Subject", "Time"]
    rows = []

    for subject, minutes in subjects.items():
        formatted_time = str(timedelta(minutes=minutes))
        rows.append([subject, formatted_time])

    print(tabulate(rows, headers=headers, tablefmt="grid"))


subjects = load_subjects()
task = input("create, record, or present? ")

if task == "record":
    subject = input("what subject do you want to record? ")
    sub_record(subject)
    save_subjects()

elif task == "create":
    subject = input("what subject do you want to create? ")
    sub_create(subject)
    save_subjects()

elif task == "present":
    present()

else:
    print("invalid response")