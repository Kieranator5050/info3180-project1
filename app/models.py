from . import db


class Property(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    __tablename__ = 'properties'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), unique=True)
    noBedRooms = db.Column(db.Integer)
    noBathRooms = db.Column(db.Integer)
    location = db.Column(db.String(100))
    price = db.Column(db.Float)
    type = db.Column(db.String(20))
    description = db.Column(db.String(1500))
    photoname = db.Column(db.String(500))

    def __init__(self, title, noBedRooms, noBathRooms, location, price, type, description, photoname) -> None:
        self.title = title
        self.noBedRooms = noBedRooms
        self.noBathRooms = noBathRooms
        self.location = location   
        self.price = price
        self.type = type
        self.description = description
        self.photoname = photoname

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def get_price(self,price):
        return "${:,.2f}".format(price)

    def __repr__(self):
        return '<Property %r>' % (self.title)

    def __str__(self) -> str:
        return f"{self.id} {self.title} {self.price} {self.photoname}"