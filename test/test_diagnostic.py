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