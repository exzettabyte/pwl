from flask_sqlalchemy import SQLAlchemy
from flask import jsonify, request
from models.modelTables import Task, db

#db = SQLAlchemy()

def index():
	tasks = Task.query.all()
	response = []
	for task in tasks: response.append(task.to_dict())
	return jsonify(response), 200
	
def store():
	request_form = request.form.to_dict()
	new_task = Task(
			title = request_form['title'],
			description = request_form['description'],
			done = bool(request_form['done'])
		)
	db.session.add(new_task)
	db.session.commit()
	response = Task.query.get(new_task.task_id).to_dict()
	return jsonify(response), 201

def show(task_id):
	response = Task.query.get(task_id)
	if(response):
		response = Task.query.get(task_id).to_dict()
		return jsonify(response), 200
	else:
		return jsonify({"message":"Data Not Found"}), 404
	
def update(task_id):
	data = Task.query.get(task_id)
	if(data):
		request_form = request.form.to_dict()
		data.title = request_form['title']
		data.description = request_form['description']
		db.session.commit()
		return jsonify({"message": "data berhasil diupdate"}), 200
	else:
		return jsonify({"message": "data tidak ditemukan"}), 404
	
def delete(task_id):
	check = Task.query.get(task_id)
	if(check):
		Task.query.filter_by(task_id=task_id).delete()
		db.session.commit()
		return jsonify({"message": "Data Berhasil dihapus"}), 200
	else:
		return jsonify({"message": "Data Tidak Ditemukan"}), 404