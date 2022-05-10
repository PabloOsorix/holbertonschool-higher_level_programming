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

    new_state = State(name="Louisiana")
    session.add(new_state)

    query = session.query(State).filter_by(name="Louisiana").first()
    if query is not None:
        print(str(query.id))
    session.commit()
    session.close()
