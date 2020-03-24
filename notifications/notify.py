from plugins.typesetting import plugin_settings
from events import logic as events_logic
from utils import models as utils_models


def typesetting_assignment(request, assignment, message, skip):
    kwargs = {
        'assignment': assignment,
        'request': request,
        'message': message,
        'skip': skip,
    }

    events_logic.Events.raise_event(
        plugin_settings.ON_TYPESETTING_ASSIGN_NOTIFICATION,
        task_object=assignment.round.article,
        **kwargs,
    )

    if not skip:
        assignment.notified = True
        assignment.save()


def galley_proofing_assignment(request, assignment, message, skip):
    kwargs = {
        'assignment': assignment,
        'request': request,
        'message': message,
        'skip': skip,
    }

    utils_models.LogEntry.add_entry(
        types='Proofreader Assigned',
        description='{} assigned as a proofreader by {}'.format(
            assignment.proofreader.full_name(),
            request.user,
        ),
        level='Info',
        actor=request.user,
        target=assignment.round.article,
    )

    events_logic.Events.raise_event(
        plugin_settings.ON_PROOFREADER_ASSIGN_NOTIFICATION,
        task_object=assignment.round.article,
        **kwargs,
    )


def galley_proofing_cancel(request, assignment):
    kwargs = {
        'assignment': assignment,
        'request': request,
        'event_type': 'cancelled',
    }

    utils_models.LogEntry.add_entry(
        types='Proofreading Assignment Cancelled',
        description='Proofing by {} cancelled by {}'.format(
            assignment.proofreader.full_name(),
            request.user,
        ),
        level='Info',
        actor=request.user,
        target=assignment.round.article,
    )

    events_logic.Events.raise_event(
        plugin_settings.ON_PROOFREADER_ASSIGN_CANCELLED,
        task_object=assignment.round.article,
        **kwargs,
    )


def galley_proofing_reset(request, assignment):
    kwargs = {
        'assignment': assignment,
        'request': request,
        'event_type': 'reset',
    }

    utils_models.LogEntry.add_entry(
        types='Proofreading Assignment Reset',
        description='Proofing by {} reset by {}'.format(
            assignment.proofreader.full_name(),
            request.user,
        ),
        level='Info',
        actor=request.user,
        target=assignment.round.article,
    )

    events_logic.Events.raise_event(
        plugin_settings.ON_PROOFREADER_ASSIGN_RESET,
        task_object=assignment.round.article,
        **kwargs,
    )


def galley_proofing_complete(request, assignment):
    kwargs = {
        'assignment': assignment,
        'request': request,
        'event_type': 'completed'
    }

    utils_models.LogEntry.add_entry(
        types='Proofreading Assignment Complete',
        description='Proofing by {} completed'.format(
            request.user,
        ),
        level='Info',
        actor=request.user,
        target=assignment.round.article,
    )

    events_logic.Events.raise_event(
        plugin_settings.ON_PROOFREADER_ASSIGN_COMPLETE,
        task_object=assignment.round.article,
        **kwargs,
    )
