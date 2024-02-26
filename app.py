from website import create_app
from website import db

#print(db)
#exit(0)
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)


