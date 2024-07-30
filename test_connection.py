from pymongo import MongoClient

# Рядок підключення
uri = "mongodb+srv://andriysydor91:53rKL6MJXYhePqqA@cluster0.lls6tnz.mongodb.net/myDatabase?retryWrites=true&w=majority"

# Підключення до сервера
client = MongoClient(uri)

# Перевірка підключення
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
