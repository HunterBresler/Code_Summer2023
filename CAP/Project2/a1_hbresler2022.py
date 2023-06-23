# Project 2: Genetic Algorthim 
# Author: Hunter Bresler
# Date: 06/22/2023

import math
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
        self.bestRoute = self.population[self.populationSize-1]
    
    # driver function of the GA
    def run_GA(self, generations):
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
    
    # Creates the initial population for the GA
    def create_initial_population(self):
        population = []
        for i in range(0, self.populationSize):
            element = Element(self.gridTSP.cityCount)
            element.randomize_chromosome()
            element.calculate_fitness(self.gridTSP.cityList)
            population.append(element)
        population.sort(key=lambda x: x.fitness, reverse=True) # sort the population by fitness
        return population

    # Creates the next generation using reproduction
    # The selected parents also are in the next generation
    def create_new_generation(self):
        allParents = self.get_parents()
        newPopulation = []
        averageFitness = 0
        # create new population
        for i in range(self.populationSize-len(allParents)):
            parents = random.sample(allParents, 2)
            childChromosome = self.crossover(parents[0], parents[1])
            newChild = Element(self.gridTSP.cityCount)
            newChild.chromosome = childChromosome
            newChild.calculate_fitness(self.gridTSP.cityList)
            averageFitness = averageFitness + newChild.fitness
            newPopulation.append(newChild)
        
        test1 = len(newPopulation)
        newPopulation.extend(allParents)
        test2 = len(newPopulation)
        self.population = newPopulation
        if self.populationSize != len(self.population):
            print(f"New POP_SIZE is: {len(self.population)}")
            print(f"Number of children = {test1} Number of parents staying = {len(allParents)}")
        self.populationSize = len(self.population)
        self.population.sort(key=lambda x: x.fitness, reverse=True) # sort the population by fitness
        # Keep Track of best fitness overall
        if newPopulation[len(self.population)-1].fitness < self.bestRoute.fitness:
            self.bestRoute = newPopulation[len(self.population)-1]

        # return the average fitness of a generation
        for i in allParents:
            f = lambda x: x.fitness
            averageFitness = averageFitness + f(i)
        return averageFitness/self.populationSize

    # Selects and returns a list of parents using a modified roulette wheel
    # The top performing Element will be favored based on rank
    def get_parents(self):
        rouletteWheel = []
        sumOfWheel = 0.0
        parents = []
        
        # Generate "wheel"
        for i in range(0, self.populationSize):
            odds = i
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
        splice1 = int(random.random()*len(parent1.chromosome))
        splice2 = int(random.random()*len(parent1.chromosome))
        childChromosome = []
        if splice1 <= splice2:
            childChromosome.extend(parent1.chromosome[0: splice1])
            childChromosome.extend(parent2.chromosome[splice1: splice2])
            childChromosome.extend(parent1.chromosome[splice2: len(parent1.chromosome)])
        else:
            childChromosome.extend(parent1.chromosome[0: splice2])
            childChromosome.extend(parent2.chromosome[splice2: splice1])
            childChromosome.extend(parent1.chromosome[splice1: len(parent1.chromosome)])
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

        # Make it so that some children don't get mutations
        if 10*random.random() > 8:
            return childChromosome
        
        # Add specific, random mutations by swapping 2 alleles
        swap1 = int(random.random()*self.gridTSP.cityCount)
        swap2 = int(random.random()*self.gridTSP.cityCount)
        temp = childChromosome[swap1]
        childChromosome[swap1] = childChromosome[swap2]
        childChromosome[swap2] = temp

        return childChromosome
        
# Represents a member of the TSP_GA population    
# Chromosomes are an ordered list of cities visited
class Element:
    def __init__(self, cityCount):
        self.chromosome = list(range(cityCount))
        self.routeLength = 0.0
        self.fitness = 0.0

    '''def get_fitness(self):
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
    # fitness = routeLength - sum of the the longest 3 trips / 3
    # Hopefully it will help the GA learn that long trips are bad quickly
    def calculate_fitness(self, cityList):
        self.check_chromosome(cityList)
        maxCityToCity = self.calculate_route_length(cityList)
        self.fitness = self.routeLength + sum(maxCityToCity)/3

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

# MAIN
# NOTE: CHANGE THESE 3 VALUES
NUMBER_OF_CITIES = 25
POPULATION_SIZE = 1000
NUMBER_OF_GENERATIONS =100
salesmanProblem = TSP_GA(NUMBER_OF_CITIES, POPULATION_SIZE)
salesmanProblem.run_GA(NUMBER_OF_GENERATIONS)

# NOTE: Lower Fitness = Better Fitness
# Counterintuitive yes, but easier to implement