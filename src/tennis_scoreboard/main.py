from sqlalchemy import MetaData, Table, create_engine, URL, text
from sqlalchemy.orm import sessionmaker, Session

url_object = URL.create(
    drivername='mysql+pymysql',
    username='root',
    password='asdf',
    host='localhost',
    port='3306',
    database='testdb',
)

engine = create_engine(url_object, echo=True)

metadata = MetaData()

my_table = Table('users', metadata, autoload_with=engine)

Session = sessionmaker(bind=engine)
session = Session()
results = session.query(my_table).all()

for row in results:
    print(row)

# with engine.connect() as connection:
#     result = connection.execute(text("SELECT * FROM users"))
#     for row in result:
#         print(row)
