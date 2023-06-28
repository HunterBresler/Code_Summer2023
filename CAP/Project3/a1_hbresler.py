# Project 2: Genetic Algorthim 
# Author: Hunter Bresler
# Date: 06/22/2023

import math
import random

# Represents a city on a TSP_Grid
class City:
    def __init__(self, x, y):
        self.X = x
        self.Y = y

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

# Controls all aspects of the ACO
class TSP_ACO:
    def __init__(self, cityCount, populationSize):
        self.gridTSP = TSP_Grid(cityCount)
        #random.seed() # Switching to a random seed after the TSP_Grid is built
        self.cityMatrix = self.create_city_matrix
        self.populationSize = populationSize
        self.population = self.create_initial_population()
        self.bestRoute = self.population[self.populationSize-1]
    
    # driver function of the GA
    def run_ACO(self, generations):
        generationCount = 1
        print(f"Generation {generationCount}'s best fitness: {self.population[len(self.population)-1].fitness}")
        print(f"Generation {generationCount}'s worst fitness: {self.population[0].fitness}")
        print(f"The Best Route found is: {self.bestRoute.__dict__}\n")

        # Run a new generation of the GA generations times
        for i in range(generations):
            averageFitness = self.create_new_generation()
            generationCount = generationCount + 1
            # Print the best and worst of each generation
            if generationCount%(generations/10) == 0 or generationCount == 1:
                print(f"Generation {generationCount}'s best fitness: {self.population[len(self.population)-1].fitness}")
                print(f"Generation {generationCount}'s worst fitness: {self.population[0].fitness}")
                print(f"Generation {generationCount}'s average fitness: {averageFitness}")
                print(f"The Best Route found is: {self.bestRoute.__dict__}\n")
    
    # Creates a matrix of each city's distance to other cities
    # As well as the # of pheremones on that path
    def create_city_matrix(self):
        pass

    # Creates the initial population for the GA
    def create_initial_population(self):
        population = []
        for i in range(0, self.populationSize):
            pass
        population.sort(key=lambda x: x.routeLength, reverse=True) # sort the population by fitness
        return population

    def create_new_generation(self):
        pass
        
# Represents a member of the colony's population    
class Ant:
    def __init__(self, cityCount):
        self.cityCount = cityCount
        self.visitedCities = []
        self.routeLength = 0.0

    # Calculates fitness 
    def calculate_fitness(self, cityList):
        pass

    # Calculates the total length of a route
    def calculate_route_length(self, cityList):
        routeLength = 0.0
        for i in range(len(self.visitedCities)):
            try:
                cityToCity = self.city_distance(cityList[self.visitedCities[i]], cityList[self.visitedCities[i+1]])
                routeLength = routeLength + cityToCity
            # Loop back to the first city for the last distance calculation
            except:
                cityToCity = self.city_distance(cityList[self.visitedCities[i]], cityList[self.visitedCities[0]])
                routeLength = routeLength + cityToCity
        self.routeLength = routeLength

    # Calculates the distance between 2 cities
    def city_distance(self, city1, city2):
        xDistance = abs(city1.X - city2.X)
        yDistance = abs(city1.Y - city2.Y)
        totalDistance = math.sqrt((xDistance ** 2) + (yDistance ** 2))
        return totalDistance
# MAIN
# Set the initial seed to be 256 for TSP_Grid generation
# Changes to a random seed after TSP_Grid generation
random.seed(256)

# NOTE: CHANGE THESE 3 VALUES
NUMBER_OF_CITIES = int(input("NUMBER_OF_CITIES: "))#25
POPULATION_SIZE = int(input("POPULATION_SIZE: "))#1000
NUMBER_OF_GENERATIONS = int(input("NUMBER_OF_GENERATIONS: "))#100
salesmanProblem = TSP_ACO(NUMBER_OF_CITIES, POPULATION_SIZE)
salesmanProblem.run_ACO(NUMBER_OF_GENERATIONS)

# NOTE: Lower Fitness = Better Fitness
# Counterintuitive yes, but easier to implement