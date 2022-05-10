#!/usr/bin/python3
"""
Script that prints the State object id
of a given name in the terminal (prompt)
"""

from model_state import Base, State
from sys import argv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2],
                                   argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State).filter(State.name == argv[4]).first()

    if query is not None:
        print(str(query.id))
    else:
        print("Not found")
    session.close()
