# app/admin/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
# from wtforms.ext.sqlalchemy.fields import QuerySelectField

from ..models import Department, Role

class DepartmentForm(FlaskForm):
    """
    Form for admin to add or edit a department
    """
    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit')


class RoleForm(FlaskForm):
    """
    Form for admin to add or edit a role
    """
    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit')

class EmployeeAssignForm(FlaskForm):
    """
    Form for admin to assign departments and roles to employees
    """
    #department = QuerySelectField(query_factory=lambda: Department.query.all(),
                                  #get_label="name")
    # role = QuerySelectField(query_factory=lambda: Role.query.all(),
                            # get_label="name")
    submit = SubmitField('Submit')
    

class EmployeeForm(FlaskForm):
    """
    Form for admin to add or edit a employee
    """
    email = StringField('email', validators=[DataRequired()])
    username= StringField('username', validators=[DataRequired()])
    first_name = StringField('first_name', validators=[DataRequired()])
    last_name = StringField('last_name', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])
    submit = SubmitField('Submit')
                            