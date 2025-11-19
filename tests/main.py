import diamond
try:
    # Core commands
    diamond.write("write()")
    input = diamond.ask("ask()")
    diamond.write(input)
    diamond.wait(1)
    diamond.clear()
    diamond.activate("a")
    # Arrow commands
    a.line(100, "black")
    a.rect(100, 100, "red", "black")
    a.turn(360)
    # Math commands
    diamond.write(diamond.sqrt(9))
    diamond.write(diamond.sin(9))
    diamond.write(diamond.cos(9))
    diamond.write(diamond.tan(9))
    diamond.write(diamond.pi)
    diamond.write(diamond.e)
    # RNG commands
    diamond.download("rng")
    diamond.write(diamond.rng.randint(1, 10))
    diamond.write(diamond.rng.random_float())
    diamond.write(diamond.rng.chance(25))
    diamond.write(diamond.rng.increment(0, 100, 5))
    # Utilities
    diamond.help()
    diamond.wait(2)
    diamond.run()
