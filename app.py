from flask import *

app=Flask(__name__)


tasks=[
        {
          'id':1,
          'title':u'This is a test',
          'desc':u'flask is awesome'    
        }   
     ]
@app.route('/')

def index():
    return "hello world"

@app.route('/todo/tasks',methods=['GET'])
def get_task():
    return jsonify({'tasks':tasks})

if __name__ == '__main__':
    app.run(debug=True)
