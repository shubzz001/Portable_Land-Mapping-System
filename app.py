from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime 

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] ="sqlite:///avishkar_data.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)


# class Avishkar_DB(db.Model):
#     pass

#     def __repr__(self) -> str:
#         return f"data"
    
list1=[123,4645]
@app.route('/')
def index(data=list1):
    return render_template('index.html',data=data)
    # return 'hello'


if __name__ == '__main__':
    app.run(debug=True)

