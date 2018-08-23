import datetime
import wtforms as wtf
from flask_wtf import FlaskForm
from flask import Blueprint, request, render_template, abort
from flask import current_app as app

from flask import flash  # suporte a mensagens de alerta
from talkshow.ext.admin import ModelView  # base Admin model view
from flask_admin.actions import action  # suporte a actions

bp = Blueprint("webui", __name__)


@bp.route('/')
def index():
    """View to list all registered events"""
    events = app.db['events'].find()
    return render_template('index.html', events=events)


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


@bp.route('/<event_id>/', methods=['GET', 'POST'])
def event(event_id):
    """A form to submit a talk to the selected event"""
    event = app.db['events'].find_one({'_id': event_id})
    if not event:
        abort(404, 'Evento não encontrado')

    form = ProposalForm(request.form)

    if form.validate_on_submit():
        # Se estamos no meio de um submit válido preparamos os dados
        proposal = form.data.copy()
        proposal['event_id'] = event_id
        proposal['date'] = datetime.datetime.today().date().isoformat()
        proposal['approved'] = False
        # e gravamos no banco de dados
        app.db['proposal'].insert_one(proposal)

        return render_template('thanks.html', proposal=proposal, event=event)

    # exibimos o formulário limpo
    return render_template('event.html', form=form, event=event)


# Flask Admin models
class ProposalAdminForm(ProposalForm):
    """Extends Proposal form to use in admin interface"""
    event_id = wtf.StringField()
    approved = wtf.BooleanField()
    submit = None


def format_event(self, request, obj, fieldname, *args, **kwargs):
    """Returns the name for the event (see also get_list)"""
    return app.db['events'].find_one({'_id': obj['event_id']})['name']


class AdminProposal(ModelView):
    """The proposal admin item"""
    can_create = False
    column_list = ('event_id', 'name', 'title', 'approved')
    form = ProposalAdminForm
    column_formatters = {'event_id': format_event}

    @action(
        'toggle_approval',
        'Approve/Disapprove',
        'Approve/Disapprove?'
    )
    def action_toggle_publish(self, ids):
        for _id in ids:
            model = self.coll.find_one({'_id': _id})
            model['approved'] = not model['approved']
            self.coll.update({'_id': _id}, model)

        flash(f'{len(ids)} items published/Unpublished.', 'success')


def configure(app):
    """Register the Blueprint to the app"""
    app.register_blueprint(bp)
    app.admin.add_view(AdminProposal(app.db['proposal'], 'Proposals'))
