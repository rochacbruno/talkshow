import wtforms as wtf
from flask_wtf import FlaskForm
from flask_admin.form.fields import DateTimeField as FlaskAdminDateTimeField


class ProposalForm(FlaskForm):
    """Form to register new proposals to events"""
    name = wtf.StringField(
        'name', validators=[wtf.validators.DataRequired()]
    )
    email = wtf.StringField(
        'email', validators=[wtf.validators.Email()]
    )
    title = wtf.StringField(
        'title', validators=[wtf.validators.DataRequired()]
    )
    description = wtf.TextAreaField(
        'description', validators=[wtf.validators.DataRequired()]
    )
    submit = wtf.SubmitField("Enviar")


class ProposalAdminForm(ProposalForm):
    """Extends Proposal form to use in admin interface"""
    date = FlaskAdminDateTimeField()  # this shows date picker widget
    event_id = wtf.StringField()
    approved = wtf.BooleanField()
    submit = None
