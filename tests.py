from unittest import TestCase
from app import app
from models import db, Strain

class StrainViewsTestCase(TestCase):
    """Tests"""
    
    def setUp(self):
        Strain.query.delete()
        db.session.commit()
        
        strains = [
        Strain(name="Granddaddy Purple", variety="Indica", thc_content=22.62, description="Real nice relaxed high. Tastes of gas and blueberries. Highly recommended."),
        Strain(name="Jack Herer", variety="Sativa",thc_content=20.42, description="Powerful mental effects. Tastes like a gentleman's weed; Soft sandalwood with a robust musk."),
        Strain(name="Girl Scout Cookies", variety="Hybrid", thc_content=25.23, description="Incredibly unique bouquet on this strain. The pungent nature of it is close to both fresh baked goods, as well as rotting flesh. The flavor is oddly fresh and almost mentholated. 10/10")
        ]

        db.session.add_all(strains)
        db.session.commit()
        
        self.strain_id = strain.id 
        
    def tearDown(self):
        """Clean Up"""
        
        db.session.rollback()
    
    def test_all_strains(self):
        with app.test_client() as client:
            resp = client.get("/api/strains")
            self.assertEqual(resp.status_code, 200)

    def test_single_strain(self):
        with app.test_client() as client:
            resp = client.get('/api/strains/6')
            self.assertEqual(
                resp.json,
                {"strain": {
                    "description": "test",
                    "id": 6,
                    "name": "test",
                    "thc_content": 0.0,
                    "variety": "test"
                }})
            
    def test_create_strain(self):
        with app.test_client() as client:
            resp = client.post(
                "/strains", json={
                    "name": "weed",
                    "variety": "weed",
                    "thc_content": 0.0,
                    "description": "weed"
                })
            self.assertEqual(resp.status_code, 201)
            
            self.assertIsInstance(resp.json['strain']['id'], int)
            del resp.json['strain']['id']
            
            self.assertEqual(
                resp.json,
                {"strain": {
                    "name": "weed",
                    "variety": "weed",
                    "thc_content": 0.0,
                    "description": "weed"
                }}
            )
            
            self.assertEqual(Strain.query.count(), 2)
        
        