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
    
    # Calculates the distance between 2 cities
    def city_distance(self, otherCity):
        xDistance = abs(self.X - otherCity.X)
        yDistance = abs(self.Y - otherCity.Y)
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

# Controls all aspects of the ACO
class TSP_ACO:
    def __init__(self, cityCount, populationSize):
        self.gridTSP = TSP_Grid(cityCount)
        self.cityCount = self.gridTSP.cityCount
        self.cityList = self.gridTSP.cityList
        #random.seed() # Switching to a random seed after the TSP_Grid is built
        self.cityMatrix = self.create_city_matrix()
        self.pheromoneIndex = 1
        self.populationSize = populationSize
        self.population = self.create_population()
        self.bestRoute = self.population[self.populationSize-1]
    
    # driver function of the GA
    def run_ACO(self, generations):
        generationCount = 1
        print(f"The Best Route found by generation {generationCount} is: {self.bestRoute.routeLength}\n")

        # Run a new generation of the GA generations times
        for i in range(generations-1):
            generationCount = generationCount + 1
            self.population = self.create_population()
            if (self.population[self.populationSize-1].routeLength < self.bestRoute.routeLength):
                self.bestRoute = self.population[self.populationSize-1]
            # Print the best and worst of each generation
            if generationCount%(generations/10) == 0 or generationCount == 1:
                print(f"The Best Route found by generation {generationCount} is: {self.bestRoute.routeLength}\n")

        print(f"The Best Route found in {generationCount} generations was: {self.bestRoute.route}, {self.bestRoute.routeLength}\n")

    
    # Creates a matrix of each city's distance to other cities
    # As well as the # of pheremones on that path
    def create_city_matrix(self):
        matrix = {}
        for city1 in self.cityList:
            matrix[city1] = {}
            for city2 in self.cityList:
                matrix[city1][city2] = [0, 1]
                matrix[city1][city2][0] = city1.city_distance(city2)
        self.cityMatrix = matrix
    
    # Creates the initial population for the GA
    def create_population(self):
        population = []
        for i in range(0, self.populationSize):
            ant = Ant(self.cityList)
            ant.ant_travel()
            population.append(ant)
        population.sort(key=lambda x: x.routeLength, reverse=True) # sort the population by fitness
        return population

    def add_pheromones(self):
        for ant in self.population:
            for i in range(len(ant.route)):
                try:
                    self.cityMatrix[i][i+1][self.pheromoneIndex] += 1
                except:
                    self.cityMatrix[i][0][self.pheromoneIndex] += 1

# Represents a member of the colony's population    
class Ant:
    def __init__(self, cityList):
        self.cityList = cityList
        self.cityCount = len(cityList)
        self.route = []
        self.routeLength = 0.0

    # Simulate an ant traveling to each city
    def ant_travel(self):
        for i in range(self.cityCount):
            self.travel_to_a_city()
        self.calculate_route_length()

    # Simulate traveling to a city
    def travel_to_a_city(self):
        city = self.choose_a_city()
        self.route.append(city)
    
    # Chooses a city to travel to
    def choose_a_city(self):
        city = int(random.random()*self.cityCount)
        if (city in self.route):
            return self.choose_a_city()
        return city

    # Calculate the length of a route
    def calculate_route_length(self):
        for i in range(len(self.route)):
            try:
                self.routeLength += self.city_distance(self.cityList[self.route[i]], self.cityList[self.route[i+1]])
            except:
                self.routeLength += self.city_distance(self.cityList[self.route[i]], self.cityList[self.route[0]])
    
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