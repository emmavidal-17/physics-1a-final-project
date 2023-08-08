# Calculates gravitational force between the Sun and a user-input planet in the solar system. 
# The result is rounded to three significant figures and expressed in scientific notation.

def gravitational_force(mass_sun, mass_planet, distance): 
    gravitational_constant = 6.674e-11  # in N m²/kg²
    force = gravitational_constant * mass_sun * mass_planet / distance ** 2 # Newton's law of gravitation
    return force

def main():
    # Dictionary containing the mass (in kg) and distance (in m) data of planets from the Sun
    planets_data = {
        "mercury": (3.3011e23, 5.791e10),
        "venus": (4.8675e24, 1.0894e11),
        "earth": (5.97219e24, 1.496e11),
        "mars": (6.4171e23, 2.2794e11),
        "jupiter": (1.8982e27, 7.7857e11),
        "saturn": (5.6834e26, 1.426e12),
        "uranus": (8.6810e25, 2.8725e12),
        "neptune": (1.02413e26, 4.4951e12),
    }

    print("Calculating the gravitational force between the Sun and a planet.")
    planet_name = input("Enter the name of the planet (case insensitive): ").lower()

    if planet_name in planets_data:
        mass_planet, distance = planets_data[planet_name]
        mass_sun = 1.989e30  # Mass of the Sun in kilograms

        force = gravitational_force(mass_sun, mass_planet, distance)

        print("The gravitational force between the Sun and {} is {:.2e} Newtons.".format(planet_name.capitalize(), force))
    else:
        print("Planet name not found in the database.")

if __name__ == "__main__":
    main()
