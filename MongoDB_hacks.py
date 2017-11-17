# How to pull fields from MongoDB

cursor = savory_recipe_db.find({})
for document in cursor:
    print(document)

def read_mongo(db, collection, query={}, host='localhost', port=27017, username=None, password=None, no_id=True):
    """ Read from Mongo and Store into DataFrame """

    # Connect to MongoDB
    db = _connect_mongo(host=host, port=port, username=username, password=password, db=db)

    # Make a query to the specific DB and Collection
    cursor = db[collection].find(query)

    # Expand the cursor and construct the DataFrame
    df =  pd.DataFrame(list(cursor))

def simple_read_mongo(coll):
    cursor = coll.find({})
    df = pd.DataFrame(list(cursor))
    return df

if __name__ == '__main__':
    df = simple_read_mongo(savory_recipe_db)
