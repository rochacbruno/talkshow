from flask import current_app as app, flash
from flask_admin.actions import action
from flask_admin.contrib.pymongo import ModelView

from talkshow.blueprints.webui.forms import ProposalAdminForm


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
