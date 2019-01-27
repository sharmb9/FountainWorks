from flask_table import Table, Col, LinkCol
 
class Results(Table):
    fountain_id = Col('fountain_id') #show =False
    building_name = Col('building_name')
    floor_num = Col('floor_num')
    status = Col('status')
    # edit = LinkCol('Edit', 'edit_view', url_kwargs=dict(id='user_id'))
    # delete = LinkCol('Delete', 'delete_user', url_kwargs=dict(id='user_id'))