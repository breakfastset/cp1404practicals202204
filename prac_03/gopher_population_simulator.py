from random import Random

INITIAL_POPULATION = 1000
BIRTH_LOWER = 10
BIRTH_UPPER = 20
DEATH_LOWER = 5
DEATH_UPPER = 25


def main():
    """Start of program"""
    gopher_population = INITIAL_POPULATION
    print("Welcome to the Gopher Population Simulator!")
    for year in range(10):
        gophers_born = generate_births(gopher_population)
        gophers_died = generate_deaths(gopher_population)
        gopher_population += (gophers_born - gophers_died)
        print_status(gopher_population, gophers_born, gophers_died, year)


def print_status(gopher_population, gophers_born, gophers_died, year):
    """Print report on current gopher population, births and deaths"""
    print(f"{gophers_born} gophers were born. {gophers_died} died.")
    print(f"Population: {gopher_population}")
    print(f"Year {year + 1}")
    print()


def generate_births(population):
    """Generate randomly the number of gophers for the year"""
    random_generator = Random()
    birth_rate = random_generator.randint(BIRTH_LOWER, BIRTH_UPPER)
    return int(birth_rate / 100 * population)


def generate_deaths(population):
    """Decrease the population randomly for the year"""
    random_generator = Random()
    death_rate = random_generator.randint(DEATH_LOWER, DEATH_UPPER)
    return int(death_rate / 100 * population)


if __name__ == '__main__':
    main()
