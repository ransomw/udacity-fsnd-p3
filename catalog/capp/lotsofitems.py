from sqlalchemy.orm import sessionmaker

from models import engine
from models import Base
from models import User
from models import Category
from models import Item

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

categorySoccer = Category(name="Soccer")
categoryBasketball = Category(name="Basketball")
categoryBaseball = Category(name="Baseball")
categoryFrisbee = Category(name="Frisbee")
categorySnowboarding = Category(name="Snowboarding")
categoryRockClimbing = Category(name="Rock Climbing")
categoryFoosball = Category(name="Foosball")
categorySkating = Category(name="Skating")
categoryHockey = Category(name="Hockey")

session.add(categorySoccer)
session.commit()
session.add(categoryBasketball)
session.commit()
session.add(categoryBaseball)
session.commit()
session.add(categoryFrisbee)
session.commit()
session.add(categorySnowboarding)
session.commit()
session.add(categoryRockClimbing)
session.commit()
session.add(categoryFoosball)
session.commit()
session.add(categorySkating)
session.commit()
session.add(categoryHockey)
session.commit()

item = Item(
    title="Stick",
    description="A hockey stick",
    category=categoryHockey)
session.add(item)
session.commit()

item = Item(
    title="Goggles",
    description="Keep the snow out of your eyes",
    category=categorySnowboarding)
session.add(item)
session.commit()

item = Item(
    title="Snowboard",
    description="Type-A vintage",
    category=categorySnowboarding)
session.add(item)
session.commit()

item = Item(
    title="Two shinguards",
    description="Prevent injuries resulting from kicks to the shin",
    category=categorySoccer)
session.add(item)
session.commit()

item = Item(
    title="Shinguards",
    description="Prevent injuries resulting from kicks to the shin",
    category=categorySoccer)
session.add(item)
session.commit()

item = Item(
    title="Frisbee",
    description="A flying disc",
    category=categoryFrisbee)
session.add(item)
session.commit()

item = Item(
    title="Bat",
    description="Louisville slugger",
    category=categoryBaseball)
session.add(item)
session.commit()

item = Item(
    title="Jersey",
    description="World Cup 2014 commemorative jersy",
    category=categorySoccer)
session.add(item)
session.commit()

item = Item(
    title="Soccer Cleats",
    description="Nike cleats",
    category=categorySoccer)
session.add(item)
session.commit()

print "populated database with sample data"
