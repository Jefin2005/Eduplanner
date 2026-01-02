def calculate_fitness(chromosome):
    penalty = 0

    faculty_time = set()
    room_time = set()
    faculty_load = {}

    for entry in chromosome.entries:
        f_key = (entry['faculty'].id, entry['day'], entry['period'])
        r_key = (entry['room'].id, entry['day'], entry['period'])

        # Faculty clash
        if f_key in faculty_time:
            penalty += 10
        faculty_time.add(f_key)

        # Room clash
        if r_key in room_time:
            penalty += 10
        room_time.add(r_key)

        # Workload check
        faculty_load.setdefault(entry['faculty'].id, 0)
        faculty_load[entry['faculty'].id] += entry['subject'].weekly_hours

        if faculty_load[entry['faculty'].id] > entry['faculty'].max_hours:
            penalty += 5

    chromosome.fitness = 1 / (1 + penalty)
    return chromosome.fitness
