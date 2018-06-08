from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, Base, Item, User

engine = create_engine('sqlite:///electronics.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create dummy user
User1 = User(name="Robo Barista", email="tinnyTim@udacity.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')  # noqa
session.add(User1)
session.commit()

#  Televisions
category1 = Category(user_id=1, name="Televisions")

session.add(category1)
session.commit()

Item2 = Item(user_id=1,
             name="Sony 900F",
             description="4K HDR TV with full array local dimming",
             price="$1200.00",
             category=category1)

session.add(Item2)
session.commit()


Item1 = Item(user_id=1,
             name="LG B8",
             description="4K HDR OLED TV with Dolby Vision",
             price="$2000.99",
             category=category1)

session.add(Item1)
session.commit()

Item2 = Item(user_id=1,
             name="Samsung Q9",
             description="4K HDR TV with nearly 2000 nits of brightness",
             price="$3000.50",
             category=category1)

session.add(Item2)
session.commit()

Item3 = Item(user_id=1,
             name="Panasonic EZ1000",
             description="""4K HDR OLED TV with best in class
                            video processing""",
             price="$7000.99",
             category=category1)

session.add(Item3)
session.commit()


#  Blu-Ray Players
category2 = Category(user_id=1, name="Blu-Ray Players")

session.add(category2)
session.commit()


Item1 = Item(user_id=1,
             name="Oppo-203",
             description="The blu-ray player for audio/videophiles",
             price="$500.00",
             category=category2)

session.add(Item1)
session.commit()

Item2 = Item(user_id=1,
             name="Oppo-205",
             description=" The step up model from the Oppo-203",
             price="$700.00",
             category=category2)

session.add(Item2)
session.commit()

Item3 = Item(user_id=1,
             name="Samsung M9500",
             description="""Produces bright and colorful HDR image,
                            and includes many streaming apps """,
             price="$300.00",
             category=category2)

session.add(Item3)
session.commit()

Item4 = Item(user_id=1,
             name="Sony X800 ",
             description="""Will support the new low-latency
                            Dolby Vision profile """,
             price="$200.00",
             category=category2)

session.add(Item4)
session.commit()


#  Laptops
category1 = Category(user_id=1, name="Laptops")

session.add(category1)
session.commit()


Item1 = Item(user_id=1,
             name="Dell Inspiron",
             description="""15 inch screen, Intel Core
                            i7-7700HQ/128GB SSD/1TB HDD/
                            16GB RAM/Win 10""",
             price="$1,299.99",
             category=category1)

session.add(Item1)
session.commit()

Item2 = Item(user_id=1,
             name="ASUS ROG Strix",
             description="""17 inch screen, Intel Core
                            i7-7700HQ/1TB HDD/128GB
                            SSD/16GB RAM/Win 10""",
             price="$1,499.99",
             category=category1)

session.add(Item2)
session.commit()

Item3 = Item(user_id=1,
             name="Acer Predator Helios",
             description="""17 inch screen, i7-7700HQ/1TB
                            HDD/128GB SSD/12GB RAM/Win10""",
             price="$1,599.99",
             category=category1)

session.add(Item3)
session.commit()


#  Cell Phones
category1 = Category(user_id=1, name="Phones ")

session.add(category1)
session.commit()


Item1 = Item(user_id=1,
             name="Apple iPhone 8",
             description="64GB - Gold",
             price="$299.99",
             category=category1)

session.add(Item1)
session.commit()

Item2 = Item(user_id=1,
             name="LG G7",
             description="ThinQ - Platinum Grey",
             price="$399.99",
             category=category1)

session.add(Item2)
session.commit()

Item3 = Item(user_id=1,
             name="Samsung Galaxy S9",
             description="""edge-to-edge Quad HD+
                            Super AMOLED touchscreen Infinity Display
                            with a resolution of 1440 x 2960""",
             price="$99.99",
             category=category1)

session.add(Item3)
session.commit()

#  Gaming consoles
category1 = Category(user_id=1, name="Gaming Consoles")

session.add(category1)
session.commit()

Item2 = Item(user_id=1,
             name="Xbox One X",
             description="""The world's most powerful console.
                            Supports true 4K native gaming and HDR.
                            Supports 4K Ultra HD Blu-Ray playback.""",
             price="$599.99",
             category=category1)

session.add(Item2)
session.commit()

Item1 = Item(user_id=1,
             name="Playstation Pro",
             description="Supports 4K gaming and HDR",
             price="$499.99",
             category=category1)

session.add(Item1)
session.commit()

print "added  items!"
