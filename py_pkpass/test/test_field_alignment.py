# -*- coding: utf-8 -*-
from py_pkpass.models import Alignment, EventTicket


def test_field_alignment_defaults_to_left():
    event_info = EventTicket()
    event_info.addHeaderField('date', 'June 15, 2026', 'Date')

    field = event_info.headerFields[0].json_dict()
    assert field['textAlignment'] == Alignment.LEFT


def test_field_alignment_can_be_set_on_add_methods():
    event_info = EventTicket()
    event_info.addHeaderField(
        'header',
        'June 15, 2026',
        '7:00 PM → 10:00 PM',
        align=Alignment.CENTER,
    )
    event_info.addSecondaryField(
        'performance',
        '7:00 PM',
        'Performance',
        align=Alignment.RIGHT,
    )
    event_info.addAuxiliaryField(
        'location',
        'Main Hall',
        'Location',
        align=Alignment.JUSTIFIED,
    )

    pass_json = event_info.json_dict()

    assert pass_json['headerFields'][0]['textAlignment'] == Alignment.CENTER
    assert pass_json['secondaryFields'][0]['textAlignment'] == Alignment.RIGHT
    assert pass_json['auxiliaryFields'][0]['textAlignment'] == Alignment.JUSTIFIED
