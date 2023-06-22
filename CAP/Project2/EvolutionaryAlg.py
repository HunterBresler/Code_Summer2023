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
    
    # driver function of the GA
    def run_GA(self, generations):
        generationCount = 1
        for i in range(generations):
            self.create_new_generation(generationCount)
            generationCount = generationCount + 1
    
    # Creates the initial population for the GA
    def create_initial_population(self):
        population = []
        for i in range(0, self.populationSize):
            element = Element(self.gridTSP.cityCount)
            element.randomize_chromosome()
            element.calculate_fitness(self.gridTSP.cityList)
            population.append(element)
        return population

    # Creates the entirety of the next generation using reproduction
    def create_new_generation(self, generationCount):
        parents = self.get_parents(generationCount)
        newPopulation = []
        for i in range(len(parents)):
            parents = random.sample(parents, len(parents))
            for i in range(0, len(parents), 2):
                childChromosome = self.crossover(parents[i], parents[i+1])
                newChild = Element(self.gridTSP.cityCount)
                newChild.chromosome = childChromosome
                newChild.calculate_fitness(self.gridTSP.cityList)
                newPopulation.append(newChild)
        self.population = newPopulation
        self.populationSize = len(self.population)
        print(f"POP_SIZE for new gen = {self.populationSize}")

    # Selects and returns a list of parents using a modified roulette wheel
    # The top performing Element will be favored by a factor of rouletteScalar
    # For rouletteScalar = 5, the top scorer gets odds of 5/totalOdds and the worst gets odds of 1/totalOdds
    # Each Elements odds will be (currentElement-bottomElement)/(topElement-bottomeElement)*rouletteScalar
    # Minimum odds being 1
    def get_parents(self, generationCount):
        rouletteScalar = 5
        rouletteWheel = []
        sumOfWheel = 0.0
        parents = []
        odds = 1

        # Get the top and bottom fitness scores
        topFitness = -math.inf
        bottomFitness = math.inf
        for i in self.population:
            if i.fitness > topFitness:
                topFitness = i.fitness
            if i.fitness < bottomFitness:
                bottomFitness = i.fitness

        # Print the best and worst of each generation
        print(f"Generation {generationCount}'s best fitness: {topFitness}")
        print(f"Generation {generationCount}'s worst fitness: {bottomFitness}")
        print(f"POP_SIZE = {self.populationSize}")
        
        # Generate "wheel"
        for i in range(0, self.populationSize):
            try:
                odds = (self.population[i].fitness-bottomFitness)/(topFitness-bottomFitness)*rouletteScalar
            except:
                print([element.fitness for element in self.population])
            if odds < 1:
                odds = 1
            sumOfWheel = sumOfWheel + odds
            rouletteWheel.append(odds)
        
        # "Spin" the wheel
        # Multiply by 2 so there are an even amount of parents
        for i in range(int(self.populationSize/6)*2):
            spinValue = random.random()*sumOfWheel
            for count, i in enumerate(rouletteWheel):
                spinValue = spinValue + i
                if spinValue >= sumOfWheel:
                    parents.append(self.population[count])
                    break
        return parents
    
    # Creates children for the next generation
    # Takes a chunk from 1 parent and switches it out with the same chunk of the other
    # Will likely have duplicate cities. Addressed in mutate
    def crossover(self, parent1, parent2):
        spliceStart = int(random.random()*len(parent1.chromosome)/2)
        spliceEnd = int(spliceStart + random.random()*len(parent1.chromosome)/2)
        childChromosome = []
        childChromosome.extend(parent1.chromosome[0: spliceStart])
        childChromosome.extend(parent2.chromosome[spliceStart: spliceEnd])
        childChromosome.extend(parent1.chromosome[spliceEnd: len(parent1.chromosome)])
        childChromosome = self.mutate(childChromosome)
        return childChromosome
    
    # Replaces duplicate alleles with missing alleles randomly
    def mutate(self, childChromosome):
        # Creates and randomizes the order of the allele list
        alleleList = list(range(0, self.gridTSP.cityCount))
        alleleList = random.sample(alleleList, len(alleleList))

        unusedAlleles = []
        for i in alleleList:
            alleleCount = childChromosome.count(i)
            if alleleCount == 1:
                continue
            elif alleleCount == 0:
                unusedAlleles.append(i)
            elif alleleCount == 2:
                if len(unusedAlleles) == 0:
                    alleleList.append(i)
                else:
                    replacementAllele = unusedAlleles.pop(0)
                    childChromosome[childChromosome.index(i)] = replacementAllele

        return childChromosome
        
# Represents a member of the TSP_GA population    
# Chromosomes are an ordered list of cities visited
class Element:
    def __init__(self, cityCount):
        self.chromosome = list(range(cityCount))
        self.routeLength = 0.0
        self.fitness = 0.0

    '''@property
    def fitness(self):
        return self.fitness'''
    
    def check_chromosome(self, cityList):
        check = list(range(0, len(cityList)))
        for i in check:
            if self.chromosome.count(i) != 1:
                print(f"Invalid chromosome: {self.chromosome}\n{check}")
                break
    
    # Sets the chromosome to a random
    def randomize_chromosome(self):
        self.chromosome = random.sample(self.chromosome, len(self.chromosome))

    # Calculates fitness 
    # fitness = routeLength - sum of the the longest 3 trips * 5
    # Hopefully it will help the GA learn that long trips are bad quickly
    #TODO:FIX
    def calculate_fitness(self, cityList):
        self.check_chromosome(cityList)
        maxCityToCity = self.calculate_route_length(cityList)
        self.fitness = 4000 - self.routeLength - sum(maxCityToCity)/len(self.chromosome)

    # Calculates the total length of a route/chromosome
    # Also returns longest 3 cityToCity distances
    def calculate_route_length(self, cityList):
        routeLength = 0.0
        maxCityToCity = [0.0, 0.0, 0.0]
        for i in range(len(self.chromosome)):
            try:
                cityToCity = self.city_distance(cityList[self.chromosome[i]], cityList[self.chromosome[i+1]])
                if cityToCity > min(maxCityToCity):
                    maxCityToCity[maxCityToCity.index(min(maxCityToCity))] = cityToCity
                routeLength = routeLength + cityToCity
            # Loop back to the first city for the last distance calculation
            except:
                cityToCity = self.city_distance(cityList[self.chromosome[i]], cityList[self.chromosome[0]])
                if cityToCity > min(maxCityToCity):
                    maxCityToCity[maxCityToCity.index(min(maxCityToCity))] = cityToCity
                routeLength = routeLength + cityToCity
        self.routeLength = routeLength
        return maxCityToCity

    # Calculates the distance between 2 cities
    def city_distance(self, city1, city2):
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
POPULATION_SIZE = 18
NUMBER_OF_GENERATIONS = 10
salesmanProblem = TSP_GA(NUMBER_OF_CITIES, POPULATION_SIZE)
salesmanProblem.run_GA(NUMBER_OF_GENERATIONS)