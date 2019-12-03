from fuel_calculation import fuel_calculation_for_modules_mass

def test_fuel_calculation_for_modules_mass(mass):
    """For a mass of 12, divide by 3 and round down to get 4, then subtract 2 to get 2.
        For a mass of 14, dividing by 3 and rounding down still yields 4, so the fuel required is also 2.
        For a mass of 1969, the fuel required is 654.
        For a mass of 100756, the fuel required is 33583.
    """

    assert fuel_calculation_for_modules_mass(12) == 2
    assert fuel_calculation_for_modules_mass(14) == 2
    assert fuel_calculation_for_modules_mass(1969) == 654
    assert fuel_calculation_for_modules_mass(100756) == 33583
