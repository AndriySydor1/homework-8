import mongoengine as me

def connect_to_db():
    me.connect(
        host="mongodb+srv://andriysydor91:53rKL6MJXYhePqqA@cluster0.lls6tnz.mongodb.net/myDatabase?retryWrites=true&w=majority"
    )
    