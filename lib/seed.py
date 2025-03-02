#!/usr/bin/env python3

from faker import Faker
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Game

fake = Faker()

if __name__ == '__main__':
    
    engine = create_engine('sqlite:///seed_db.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(Game).delete()
    session.commit()

    #Generate 50 random games
    games = [Game(
        title = fake.name(),
        genre = fake.word(),
        platform = fake.word(),
        price = random.randint(0, 60)
    )
    for _ in range(50)
    ]



    # games = [
    # Game(title="Breath of the Wild", platform="Switch", genre="Adventure", price=60),
    # Game(title="Final Fantasy VII", platform="Playstation", genre="RPG", price=30),
    # Game(title="Mario Kart 8", platform="Switch", genre="Racing", price=50),
    # ]

    session.bulk_save_objects(games)
    session.commit()

    print("Database seeded with 50 random games!")

