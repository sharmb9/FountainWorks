import pymysql
from app import app
from tables import Results
from db_config import mysql
from flask import flash, render_template, request, redirect


# users add new stuff(update databse) in new_user(change it to show building to store fountain info)
@app.route('/new_user')
def add_user_view():
	return render_template('add.html')
		
@app.route('/add', methods=['POST'])
def add_user():
	try:		
		_builName = request.form['inputBuilding'] #_name
		_floorNum = request.form['inputFloorNum'] #_email
		_status = request.form['inputStatus'] #_password
		_fountID = request.form['inputID']
		# validate the received values
		if _builName and _floorNum and _status and _fountID and request.method == 'POST':
			sql = "INSERT INTO fountainInfo(building_name, floor_num, status, fountain_id) VALUES(%s, %d, %s, %s)"
			data = (_builName, _floorNum, _status, _fountID)
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute(sql, data)
			conn.commit()
			flash('User added successfully!')
			return redirect('/')
		else:
			return 'Error while adding info'
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
		
@app.route('/')
def users():
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM fountainInfo")
		rows = cursor.fetchall()
		table = Results(rows)
		table.border = True
		return render_template('users.html', table=table)
		#cursor.close() 
		#conn.close()
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()


@app.route('/edit/<int:id>')
def edit_view(id): #change param to fountain id?
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM fountainInfo WHERE id=%s", id)
		row = cursor.fetchone()
		if row:
			return render_template('edit.html', row=row)
		else:
			return 'Error loading #{id}'.format(id=id)
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()

# updating database by changing the status by user
@app.route('/update', methods=['POST'])
def update_user():
	try:		
		_builName = request.form['inputBuilding'] #_name
		_floorNum = request.form['inputFloorNum'] #_email
		_status = request.form['inputStatus'] #_password
		_fountID = request.form['inputID']
		# validate the received values
		if _builName and _floorNum and _status and _fountID and request.method == 'POST':
			#do not save password as a plain text
			# save edits
			sql = "UPDATE fountainInfo SET building_name=%s, floor_num=%d, status=%s, fountain_id=%s WHERE fountain_id=%s"
			data = (_builName, _floorNum, _status, _fountID)
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute(sql, data)
			conn.commit()
			flash('User updated successfully!')
			return redirect('/')
		else:
			return 'Error while updating user'
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

#delete info		
@app.route('/delete/<int:id>')
def delete_user(id):
	try:
		conn = mysql.connect()
		cursor = conn.cursor()
		cursor.execute("DELETE FROM fountainInfo WHERE fountain_id=%s", (id,))
		conn.commit()
		flash('User deleted successfully!')
		return redirect('/')
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
		
if __name__ == "__main__":
    app.run()