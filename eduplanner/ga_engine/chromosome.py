import random

class Chromosome:
    def __init__(self, entries):
        self.entries = entries  # list of timetable entries
        self.fitness = 0

    def mutate(self, subjects, faculties, rooms):
        index = random.randint(0, len(self.entries) - 1)
        self.entries[index]['subject'] = random.choice(subjects)
        self.entries[index]['faculty'] = random.choice(faculties)
        self.entries[index]['room'] = random.choice(rooms)
