import csv
import io
import urllib.request

class Candidate:
    def __init__(self, first_name, last_name, email,
                 tech_stack, main_skill, main_skill_grade):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.tech_stack = tech_stack
        self.main_skill = main_skill
        self.main_skill_grade = main_skill_grade

    @property
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    @classmethod
    def generate_candidates(cls, path):
        obj = []

        # якщо приймаючий path не посилання - здійсюється його
        # читання та подальше форматування під необхідний формат
        if not path.startswith('http'):
            with open(path, newline='') as csvfile:
                reader = csv.DictReader(csvfile)

                for row in reader:
                    data = dict(
                        first_name=row['Full Name'].split()[0],
                        last_name=row['Full Name'].split()[1],
                        email=row['Email'],
                        tech_stack=row['Technologies'].split('|'),
                        main_skill=row['Main Skill'],
                        main_skill_grade=row['Main Skill Grade'],
                    )
                    obj.append(cls(**data))

        elif path.startswith('http'):

            # відкриває url одночнасно декодуючи його в формат utf-8
            with io.TextIOWrapper(urllib.request.urlopen(path),
                                  encoding='utf8', newline='\n') as text_file:
                reader = csv.reader(text_file, delimiter=',')
                for row in reader:
                    data = dict(
                        first_name=row[0].split()[0],
                        last_name=row[0].split()[1],
                        email=row[1],
                        tech_stack=row[2].split('|'),
                        main_skill=row[3],
                        main_skill_grade=row[4],
                    )
                    obj.append(cls(**data))

        return obj



