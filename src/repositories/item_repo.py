from src.database.tables import ItemTable
from src.models.item import Item
from src.repositories.user_repo import UserRepository
from src.app import db

class ItemRepository:
    
    def get_all_items(self):
        items = db.session.query(ItemTable).all()
        item_list = []
        for item in items:
            user = UserRepository().get_user_by_id(item.seller_id)
            item_list.append(Item(item.id, user, item.name, 
                                item.description, (item.price_reais, item.price_cents), 
                                item.stock, item.sale))
        return item_list