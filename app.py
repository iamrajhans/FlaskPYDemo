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

@app.route('/todo/tasks/<int:task_id>',methods=['GET'])
def get_tasks(task_id):
    task=[task for task in tasks if task['id']==task_id]
    if len(task)==0:
        abort(404)
    return jsonify({'task':task[0]})

if __name__ == '__main__':
    app.run(debug=True)
