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

    def get_item_by_id(self, id: str):
        item = db.session.query(ItemTable).filter(ItemTable.id == id).first()
        user = UserRepository().get_user_by_id(item.seller_id)
        return Item(item.id, user, item.name, item.description, (item.price_reais, item.price_cents), item.stock, item.sale)

    def get_item_by_name(self, name: str):
        item = db.session.query(ItemTable).filter(ItemTable.name == name).first()
        if not item: return item
        user = UserRepository().get_user_by_id(item.seller_id)
        return Item(item.id, user, item.name, item.description, (item.price_reais, item.price_cents), item.stock, item.sale)
    
    def add_item(self, item: Item):
        seller_id = UserRepository().get_user_id_by_username(item.seller.username)
        new_item = ItemTable(item.id, seller_id, item.name, 
                            item.description, item.price[0], 
                            item.price[1], item.stock, item.sale)
        db.session.add(new_item)
        db.session.commit()
    
    def delete_item_by_name(self, name: str):
        item = db.session.query(ItemTable).filter_by(name=name).first()
        if item:
            db.session.delete(item)
            db.session.commit()