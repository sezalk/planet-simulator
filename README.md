# planet-simulator

This is a simple Python simulation of planets orbiting around the sun using the Pygame library.

## Installation

1. Make sure you have Python installed.
2. Install Pygame library by running `pip install pygame`.

## How to Run

1. Clone this repository or download the `planet_simulation.py` file.
2. Navigate to the directory containing `planet_simulation.py` in your terminal or command prompt.
3. Run the script by executing `python planet_simulation.py`.

## Controls

There are no interactive controls for this simulation. It runs automatically upon execution.

## Description

This simulation depicts the orbit of various planets around the sun using basic physics principles. Each planet is represented as a circle with its respective colour and size proportional to its mass. The simulation calculates gravitational forces between planets based on their masses and distances and updates their positions accordingly. The simulation runs at a constant time step, representing one day per iteration.

## Class: Planet

### Attributes:

- `x`: The x-coordinate position of the planet relative to the sun.
- `y`: The y-coordinate position of the planet relative to the sun.
- `radius`: The radius of the planet's circular representation on the screen.
- `colour`: The colour of the planet.
- `mass`: The mass of the planet.
- `orbit`: List to store the orbit path of the planet.
- `sun`: Boolean indicates whether the planet is the sun.
- `distance_to_sun`: Distance of the planet from the sun.
- `x_vel`: Velocity of the planet along the x-axis.
- `y_vel`: Velocity of the planet along the y-axis.

### Methods:

- `draw(win)`: Draws the planet on the Pygame window `win`.
- `attraction(other)`: Calculates the gravitational force between the planet and another planet `other`.
- `update_position(planets)`: Updates the planet's position based on gravitational forces from other planets in the `planets` list.

## Disclaimer

This simulation is provided as-is without any warranty. The author holds no liability for any damages or issues caused by using this code.
