from app.main import app
from app.utils.db import connect_db
if __name__ == "__main__":
        print('Flask app is running 🌶')
        db=connect_db()
        app.run(debug=False)
         