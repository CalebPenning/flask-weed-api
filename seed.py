from models import db, connect_db, Strain
from app import app

db.drop_all()
db.create_all()

strains = [
    Strain(name="Granddaddy Purple", variety="Indica", thc_content=22.62, description="Real nice relaxed high. Tastes of gas and blueberries. Highly recommended."),
    Strain(name="Jack Herer", variety="Sativa",thc_content=20.42, description="Powerful mental effects. Tastes like a gentleman's weed; Soft sandalwood with a robust musk."),
    Strain(name="Girl Scout Cookies", variety="Hybrid", thc_content=25.23, description="Incredibly unique bouquet on this strain. The pungent nature of it is close to both fresh baked goods, as well as rotting flesh. The flavor is oddly fresh and almost mentholated. 10/10")
]

db.session.add_all(strains)
db.session.commit()