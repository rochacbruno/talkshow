import datetime

from flask import current_app as app, render_template, abort, request

from talkshow.blueprints.webui.forms import ProposalForm
from talkshow.blueprints.webui.webui import bp_webui


@bp_webui.route('/')
def index():
    """View to list all registered events"""
    events = app.db['events'].find()
    return render_template('index.html', events=events)


@bp_webui.route('/<event_id>/', methods=['GET', 'POST'])
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
