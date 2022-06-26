from src.app import app
from src.repositories.item_repo import ItemRepository
import pytest

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

class TestAddItem:
    
    def test_add_item_to_sell(self, client):
        response = client.post('/sell', data={
        'seller_id': 'U0001',
        'name': 'Apple Watch', 
        'description': 'Apple Watch Series 5 (Cellular + GPS, 44 mm)',
        'price_reais': '6254',
        'price_cents': '10',
        'stock': '2',
        'sale': '0',
        }, follow_redirects=True)


        item = ItemRepository().get_item_by_name('Apple Watch')

        assert item
        assert item.description == 'Apple Watch Series 5 (Cellular + GPS, 44 mm)'
        assert response.status_code == 200

        ItemRepository().delete_item_by_name('Apple Watch')
        item = ItemRepository().get_item_by_name('Apple Watch')

        assert not item