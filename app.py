from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os


basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')


db = SQLAlchemy(app)
ma = Marshmallow(app)

class Entry(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(15))
    content = db.Column(db.String(144))

    def __init__(self,title, content):
        self.title = title
        self.content = content

class EntrySchema(ma.Schema):
    class Meta:
        fields = ('id','title', 'content')

entry_schema = EntrySchema()
entries_schema = EntrySchema(many = True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/entry', methods = ['POST'])
def create_entry():
    
    title = request.form['title']
    content = request.form['content']

    new_entry = Entry(title, content)

    db.session.add(new_entry)
    db.session.commit()

    return render_template('index.html')

# End point to create a new entry

@app.route('/entries', methods = ['GET'])
def get_entries():

    entries = Entry.query.all()
    result = entries_schema.dump(entries)
    
    return jsonify(result)

#  End point to get all entries

@app.route("/entry/<id>", methods=["DELETE"])
def delete_entry(id):
    entry = Entry.query.get(id)
    
    db.session.delete(entry)
    db.session.commit()

    return entry_schema.jsonify(entry)

#  End point for deleting a entry

if __name__ == '__main__':
    app.run(debug = True)


    # Push to repo