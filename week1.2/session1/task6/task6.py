# Week 1.2, Session 1: Task 6

from pprint import pprint

# Create music database, as a dictionary of strings mapped to lists
# (keys are artist names, values are lists of album names)
music = {
    "The Beatles": ["Abbey Road", "Let It Be", "Sgt. Pepper's Lonely Hearts Club Band"],
    "Pink Floyd": ["The Dark Side of the Moon", "Wish You Were Here", "Animals"],
    "Led Zeppelin": ["Led Zeppelin IV", "Physical Graffiti", "Houses of the Holy"]
}
# Pretty-print the data structure
pprint(music)

# Display details of one album recorded by a specific artist

print(music.get("The Beatles"))
