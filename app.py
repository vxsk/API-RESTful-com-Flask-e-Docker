from flask import Flask, jsonify, request

app = Flask(__name__)

# Lista de tarefas 
tasks = []

#Endpoint para obter todas as tarefas

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

#Endpoint para adicionar uma nova tarefa

@app.route('/tasks', methods=['POST'])
def add_task():
    task = request.json
    tasks.append(task)
    return jsonify(task), 201

#Endpoint para atualizar uma tarefa existente

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = next((t for t in tasks if t['id'] == task_id), None)
    if task is None:
        return jsonify({'error': 'Task not found'}), 404
    updated_task = request.json
    task.update(updated_task)
    return jsonify(task)

#Endpoint para deletar uma tarefa

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_taks(task_id):
    global tasks
    tasks = [t for t in tasks if t['id'] != task_id]
    return jsonify({'result': 'Task deleted.'})

if __name__ == '__main__':
    app.run(debug=True)
