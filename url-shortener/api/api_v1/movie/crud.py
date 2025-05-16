from schemas import Movie

MOVIES = [
    Movie(
        slug="harry",
        title="Harry Potter and the Prisoner of Azkaban",
        description="""Harry Potter's third year at Hogwarts turns out to be eventful as he gets 
tutored by Professor Lupin, a Defence Against the Dark Arts teacher, 
and tackles Sirius Black, a vengeful fugitive prisoner.""",
        year=2005,
    ),
    Movie(
        slug="sniper",
        title="American Sniper",
        description="""After serving in Iraq for years, 
Chris Kyle, a lethal US sniper, returns home to his wife and son.
However, he cannot cope with the traumatic experiences of war,
affecting his life and relationships.""",
        year=2014,
    ),
    Movie(
        slug="last",
        title="Last of Us",
        description="Last of Us is best movies in last years",
        year=2022,
    ),
]
