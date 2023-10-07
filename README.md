# Predator-Prey-Genetic-SA-
Animal Ordering Problem Solver

Animal Ordering Problem Solver
Introduction
This project addresses the Animal Ordering Problem, where a set of animals in a predator-prey relationship within a wildlife ecosystem needs to be ordered in such a way that no predator precedes its prey. We aim to find the best possible order for these animals using genetic algorithms and simulated annealing.

The input to the problem is represented as a directed graph, where each node corresponds to an animal, and each directed edge from node A to node B indicates that animal A preys on animal B.

Algorithms Used
Genetic Algorithm
In the genetic algorithm approach, we work with a population of chromosomes, each representing a potential solution to the problem. Each chromosome is assigned a fitness value based on a defined objective function. The goal is to find a solution that maximizes this objective function. The main steps of the genetic algorithm include:

Initializing the population of chromosomes.
Selecting parents for reproduction.
Generating offspring through crossover and mutation.
Eliminating less fit individuals.
Continuing the process until a stopping condition is met.
Simulated Annealing (SA)
Simulated Annealing is a metaheuristic optimization algorithm inspired by the annealing process in metallurgy. It starts with an initial solution and iteratively explores nearby solutions. The algorithm accepts solutions that improve the objective function and occasionally accepts worse solutions with a decreasing probability as the "temperature" parameter decreases. The main steps of the SA algorithm include:

Initializing the temperature and initial solution.
Iteratively generating neighbor solutions.
Evaluating the objective function for each neighbor.
Accepting or rejecting neighbor solutions based on the temperature and objective function values.
Reducing the temperature until convergence.
Usage
To use this Animal Ordering Problem solver, follow these steps:

Clone this repository to your local machine.
Prepare the input graph in the form of a text file (e.g., input.txt) where the first line specifies the number of nodes, followed by pairs of nodes representing predator-prey relationships.
Modify the configuration and parameters in the code as needed.
Run the code to find the best order for the animals.
The program will output the optimal order along with additional information about the optimization process.
Example
Here's an example of how to set up and run the solver:

# Load the input graph from a file
input_graph = load_input_graph("input.txt")

# Initialize and run the genetic algorithm
ga_solver = GeneticAlgorithmSolver(input_graph)
best_order_ga = ga_solver.solve()

# Initialize and run the simulated annealing algorithm
sa_solver = SimulatedAnnealingSolver(input_graph)
best_order_sa = sa_solver.solve()
Objective Function Explanation
The objective function evaluates the quality of a given animal ordering solution. It operates on a two-dimensional list, listV1, which represents a list of nodes and their connections in the graph.

First, we check whether the first element of the list corresponds to the first predator. If not, we decrement the score by one. This step ensures that the first element in the ordering is indeed the first predator.

In the next condition, we verify if the subsequent nodes in the list are indeed prey animals. If they are, we check if the predator for each prey exists before it in the list. If not, we decrement the score by one. This condition ensures that each predator appears before its prey in the ordering.

Finally, the function returns the computed score as the result.

This objective function assesses the validity of the animal ordering by penalizing deviations from the required predator-prey relationship. A higher score indicates a more acceptable and biologically meaningful ordering.
