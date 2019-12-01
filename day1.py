import math


def module_fuel_required(module_mass):
    return math.floor(module_mass / 3) - 2


def total_fuel_required(list_of_module_mass):
    total_required = 0
    for module_mass in list_of_module_mass:
        total_required += module_fuel_required(module_mass)
    return total_required


def total_fuel_required_part2(list_of_module_mass):
    total_required = 0
    for module_mass in list_of_module_mass:
        fuel_mass = module_fuel_required(module_mass)
        temp_fuel_mass = module_fuel_required(fuel_mass)
        while temp_fuel_mass > 0:
            fuel_mass += temp_fuel_mass
            temp_fuel_mass = module_fuel_required(temp_fuel_mass)
            # print(f'Temp fuel mass: {temp_fuel_mass}')
            # print(f'Fuel mass: {fuel_mass}')

        total_required += fuel_mass
    return total_required


if __name__ == '__main__':
    with open('inputs_day1.txt', 'r') as mass_file:
        inputs = [int(x.strip()) for x in mass_file.readlines()]
        print('For module mass inputs:')
        print(inputs)
        print('Fuel required if not considering fuel required for fuel (Part 1)...')
        print(total_fuel_required(inputs))
        print('Fuel required if considering fuel required for fuel (Part 2)...')
        print (total_fuel_required_part2(inputs))
