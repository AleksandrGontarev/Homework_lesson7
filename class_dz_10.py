from datetime import datetime


class WorkDirname:
    def __init__(self, filename: str):
        self.filename = filename
        self.data = self.read_txt_file()
        self.dates = self.get_authors_dates()

    def read_txt_file(self) -> list:
        with open(self.filename, 'r') as txt_file:
            data = txt_file.read().splitlines()
        return data

    def get_authors_dates(self):
        dates = []
        for line in self.data:
            if " - " in line and line[:1].isdigit():
                dates.append({"date": line.split(" - ")[0]})
        return dates

    def transform_date(self):
        day, month, year = self.date.split()
        day = day[:-2].zfill(2)
        date = f"{day} {month} {year}"
        new_date = datetime.strptime(date, "%d %B %Y").strftime("%d/%m/%Y")
        return new_date

    def get_modified_dates(self):
        new_dates = []
        for author_date in self.dates:
            self.date = author_date["date"]
            new_dates.append({"date_original": self.date, "date_modified": self.transform_date()})
        return new_dates


authors_date = WorkDirname("C:\\Homeworks\\authors.txt")
print(authors_date.dates)
print(authors_date.get_modified_dates())



