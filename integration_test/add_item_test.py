from src.app import app
from src.repositories.item_repo import ItemRepository
import pytest
from src.app import db
from src.util.database_utils import delete_last_inserted
from src.database.tables import ItemTable

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        client.application.app_context().push()
        yield client

@pytest.fixture
def client_with_item_teardown(client):
    yield client
    delete_last_inserted("item")

class TestAddItem:
    
    def test_add_item_to_sell(self, client_with_item_teardown):
        response = client_with_item_teardown.post('/sell', data={
        'seller_id': 'U0001',
        'name': 'Apple Watch', 
        'description': 'Apple Watch Series 5 (Cellular + GPS, 44 mm)',
        'price_reais': '6254',
        'price_cents': '10',
        'stock': '2',
        'sale': '0',
        }, follow_redirects=True)

        item = db.session.query(ItemTable).filter(ItemTable.name == 'Apple Watch').first()

        assert item
        assert item.description == 'Apple Watch Series 5 (Cellular + GPS, 44 mm)'
        assert response.status_code == 200

    def test_delete_item_by_name(self, client_with_item_teardown):
        new_item = ItemTable("item-id-1", "seller-id-1", "Item Name",
                            "description", 10, 20, 5, 1)

        db.session.add(new_item)
        db.session.commit()

        ItemRepository().delete_item_by_name('Item Name')

        item = db.session.query(ItemTable).filter(ItemTable.id == "item-id-1").first()

        assert not item