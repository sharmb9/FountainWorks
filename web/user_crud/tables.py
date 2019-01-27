from flask_table import Table, Col, LinkCol
 
class Results(Table):
    fountain_id = Col('Fountain Id') #show =False
    building_name = Col('Building Name')
    floor_num = Col('Floor Number')
    status = Col('Status')
    edit = LinkCol('Edit', 'edit_view', url_kwargs=dict(id='user_id'))
    delete = LinkCol('Delete', 'delete_user', url_kwargs=dict(id='user_id'))