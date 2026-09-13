import pytest

from ecu.diagnostic import DiagnosticService


def test_default_session():
    diagnostic = DiagnosticService()

    assert diagnostic.session == 0x01


def test_change_to_extended_session():
    diagnostic = DiagnosticService()

    diagnostic.change_session(0x03)

    assert diagnostic.session == 0x03
    assert diagnostic.is_extended_session()


def test_change_to_invalid_session():
    diagnostic = DiagnosticService()

    with pytest.raises(ValueError):
        diagnostic.change_session(0x99)

def test_change_session():
    diagnostic = DiagnosticService()
    default_session = diagnostic.session
    diagnostic.change_session(0x02)
    programming_session = diagnostic.session
    diagnostic.change_session(0x03)
    extended_session = diagnostic.session

    assert default_session == 0x01
    assert programming_session == 0x02
    assert extended_session == 0x04