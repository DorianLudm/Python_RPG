from sqlalchemy import create_engine, text

engine = create_engine('sqlite:///Code/Data/rpg.db', echo=True) # set echo to False after testing

with engine.connect() as connection:
    rs = connection.execute(text('select "Hello World"' ))
    print(rs.all())