#!/usr/bin/python3

"""script that prints the first State object from the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(user, passwd, db), pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).first()
    if state:
        print('{}: {}'.format(state.id, state.name))
    else:
        print('Nothing')

    session.close()
