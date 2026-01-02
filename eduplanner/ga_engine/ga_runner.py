import random
from .chromosome import Chromosome
from .fitness import calculate_fitness

def generate_initial_population(pop_size, days, periods, subjects, faculties, rooms):
    population = []

    for _ in range(pop_size):
        entries = []
        for day in days:
            for period in range(1, periods + 1):
                entries.append({
                    "day": day,
                    "period": period,
                    "subject": random.choice(subjects),
                    "faculty": random.choice(faculties),
                    "room": random.choice(rooms),
                })
        population.append(Chromosome(entries))

    return population


def run_ga(days, periods, subjects, faculties, rooms, generations=50):
    population = generate_initial_population(
        pop_size=10,
        days=days,
        periods=periods,
        subjects=subjects,
        faculties=faculties,
        rooms=rooms
    )

    for _ in range(generations):
        for chromo in population:
            calculate_fitness(chromo)

        population.sort(key=lambda c: c.fitness, reverse=True)

        # Selection (top 50%)
        population = population[:5]

        # Mutation
        for chromo in population:
            chromo.mutate(subjects, faculties, rooms)

    return population[0]  # best timetable
