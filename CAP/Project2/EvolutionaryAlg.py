# Project 2: Genetic Algorthim 
# Author: Hunter Bresler

import math
from operator import attrgetter
import random
# Set the initial seed to be 256 for TSP_Grid generation
# Changes to a random seed after TSP_Grid generation
random.seed(256)

# Represents a city on a TSP_Grid
class City:
    def __init__(self, x, y):
        self.X = x
        self.Y = y

# Controls all aspects of the GA  
class TSP_GA:
    def __init__(self, cityCount, populationSize):
        self.gridTSP = TSP_Grid(cityCount)
        #random.seed() # Switching to a random seed after the TSP_Grid is built
        self.populationSize = populationSize
        self.population = self.create_initial_population()
    
    # Creates the initial population for the GA
    def create_initial_population(self):
        population = []
        for i in range(0, self.populationSize):
            element = Element(self.gridTSP.cityCount)
            element.randomize_chromosome()
            population.append(element)
        return population
    
    # Selects parents using a modified roulette wheel
    # The top performing Element will be favored by a factor of rouletteScalar
    # For rouletteScalar = 5, the top scorer gets odds of 5 and the worst gets odds of 1
    # Each Elements odds will be (currentElement-bottomElement/(topElement-bottomeElement)*rouletteScalar
    # Minimum odds being 1
    def parent_selection(self):
        rouletteScalar = 5
        topFitness = max(self.population, key=attrgetter('fitness'))
        bottomFitness = min(self.population, key=attrgetter('fitness'))
        


        
# Represents a member of the TSP_GA population    
# Chromosomes are an ordered list of cities visited
class Element:
    def __init__(self, cityCount):
        self.chromosome = list(range(cityCount))
        self.fitness = Fitness()
    
    # Sets the chromosome to a random
    def randomize_chromosome(self):
        self.chromosome = random.sample(self.chromosome, len(self.chromosome))

    # Gets the fitness of the Element
    def get_fitness(self):
        self.fitness.route = self.chromosome
        self.fitness.calculate_fitness()

# Class for representing/calculating the fitness of an Element
class Fitness:
    def __init__(self):
        self.route = []
        self.routeLength = 0
        self.fitness = 0.0

    # Calculates fitness using Fitness functions
    def calculate_fitness(self):
        self.calculat_route_length()
        self.fitness = self.routeLength

    # Calculates the total length of a route/chromosome
    def calculate_route_length(self):
        routeLength = 0.0
        for i in range(len(self.route)):
            try:
                routeLength = routeLength + self.city_distance(self.route[i], self.route[i+1])
            # Loop back to the first city for the last distance calculation
            except:
                routeLength = routeLength + self.city_distance(self.route[i], self.route[0])
        self.routeLength = routeLength
        

    # Calculates the distance between 2 cities
    def city_distance(city1, city2):
        xDistance = abs(city1.X - city2.X)
        yDistance = abs(city1.Y - city2.Y)
        totalDistance = math.sqrt((xDistance ** 2) + (yDistance ** 2))
        return totalDistance

# Creates a TSP problem by building a grid with cities in it
class TSP_Grid:
    def __init__(self, cityCount):
        self.xAxis = 200
        self.yAxis = 200
        self.cityCount = cityCount
        self.cityList = self.generate_cities()

    # Randomly generates the locations of cities on the TSP_Grid
    # Allows for cities with the same location (although very unlikely)
    def generate_cities(self):
        cityList = []
        for i in range(0, self.cityCount):
            cityList.append(City(x=int(random.random() * 200), y=int(random.random() * 200)))
        return cityList

NUMBER_OF_CITIES = 25
POPULATION_SIZE = 10
salesmanProblem = TSP_GA(NUMBER_OF_CITIES, POPULATION_SIZE)
print(salesmanProblem.population[0].__dict__)