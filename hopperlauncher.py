import hopper
import neat

def eval_genomes(genomes, config):

    # Play game and get results
    idx,genomes = zip(*genomes)

    game = hopper.HopperGame()
    game.create_players(genomes=genomes, config=config)
    game.play()
    results = game.results
    
    # Calculate fitness and top score
    top_score = 0
    for r in results:
        score = r[0]
        genome = r[1]
        fitness = score * 3000 
        genome.fitness = -1 if fitness == 0 else fitness
        if top_score < score:
            top_score = score

    #print score
    print('The top score was:', top_score)

def evolutionary_driver(n=10):
    # Load configuration.
    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         'neat_config.txt')

    # Create the population, which is the top-level object for a NEAT run.
    p = neat.Population(config)

    # Add a stdout reporter to show progress in the terminal.
    p.add_reporter(neat.StdOutReporter(False))

    # Run until we achive n.
    winner = p.run(eval_genomes, n=n)

    # dump
    print(winner)

evolutionary_driver(n=10)