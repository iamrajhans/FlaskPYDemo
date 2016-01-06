from flask import *
from flask.ext.httpauth import HTTPBasicAuth
app=Flask(__name__)
auth=HTTPBasicAuth()
@auth.get_password
def get_password(username):
    if username=='raj': 
        return 'python'
@auth.error_handler
def unauthorized():
    return abort(401)
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
@auth.login_required
def get_task():
    return jsonify({'tasks':tasks})

@app.route('/todo/tasks/<int:task_id>',methods=['GET'])
def get_tasks(task_id):
    task=[task for task in tasks if task['id']==task_id]
    if len(task)==0:
        abort(404)
    return jsonify({'task':task[0]})

@app.route('/todo/tasks',methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json :
            abort(400)
    task={
        'id':tasks[-1]['id']+1,
        'title':request.json['title'],
        'desc':request.json.get('desc','')
            
            }
    tasks.append(task)
    return jsonify({'task':task}),201
if __name__ == '__main__':
    app.run(debug=True)
