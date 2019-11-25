import hopper
import neat

current_generation = 0

def evaluate_genomes(genomes, config):

    # Play game and get results
    idx,genomes = zip(*genomes)
    current_generation =   1
    game = hopper.HopperGame(current_generation)
    game.create_players(genomes=genomes, config=config)
    game.play()
    results = game.results
    
    # calculate fitness for each genome and add to the genome object
    for r in results:
        score = r[0]
        genome = r[1]
        fitness = score * 3000 
        if fitness == 0:
                genome.fitness = -1 
        else:
                genome.fitness = fitness


def evolutionary_driver(generations=10):
    # Load configuration.
    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet, neat.DefaultStagnation, 'neat_config.txt')

   
    p = neat.Population(config)
    p.add_reporter(neat.StdOutReporter(False))

    # pass in our evaluation function and the number of generations
    winner = p.run(evaluate_genomes, n=generations)
    print(winner)

evolutionary_driver(generations=1000)