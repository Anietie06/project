from mongo import connect_to_mongo
import gridfs


# Establish connection
client = connect_to_mongo()

# Access database and collection
db = client['project']
collection = db['models']
fs= gridfs.GridFS(db)


def add_videos():
    with open("Hair video.mp4", "rb") as f:
        data= f.read()
        
    created_file = fs.put(data, filename = "test")
    print("upload complete")
    print(created_file)


if __name__ == "__main__":
    add_videos()