from pymongo import MongoClient


def get_db():
    mongo_client = MongoClient("10.45.3.132", 27017)
    conn = mongo_client.connection
    db = conn['makalu']
    conn.authenticate(name='makalu', password='makalu-wzkzlu-LI5')
    return db


if __name__ == "__main__":
    client = MongoClient("localhost", 27017)
    with client.start_session() as s:
        s.start_transaction()
        s.client.db_name.foo.insert_one({'abc': 1}, session=s)
        s.client.db_name.bar.insert_one({'xyz': 2}, session=s)
        s.commit_transaction()
