import pytest

from s478 import Note, Notes


def test_note_name():
    note = Note("до", 1)
    assert note._name == "до"


def test_note_ton():
    note = Note("ре", -1)
    assert note._ton == -1


def test_note_invalid_name():
    with pytest.raises(ValueError):
        note = Note("фа#", 0)


def test_note_invalid_ton():
    with pytest.raises(ValueError):
        note = Note("си", 2)


def test_note_name_setter():
    note = Note("ми", 0)
    note._name = "соль"
    assert note._name == "соль"


def test_note_ton_setter():
    note = Note("ля", 1)
    note._ton = 0
    assert note._ton == 0


def test_notes_singleton():
    notes1 = Notes()
    notes2 = Notes()
    assert notes1 is notes2


def test_notes_getitem_by_index():
    notes = Notes()
    assert notes[0]._name == "до"


def test_notes_getitem_invalid_type():
    notes = Notes()
    with pytest.raises(TypeError):
        notes[1.0]


def test_notes_getitem_invalid_index():
    notes = Notes()
    with pytest.raises(IndexError):
        notes[-1]


def test_notes_getitem_invalid_name():
    notes = Notes()
    with pytest.raises(TypeError):
        notes["фа#"]


def test_notes_get_by_note_number():
    notes = Notes()
    assert notes._get_by_note_number(0)._name == "до"


def test_notes_get_by_note_number_invalid_index():
    notes = Notes()
    with pytest.raises(IndexError):
        notes._get_by_note_number(9)


def test_notes_get_by_note_number_invalid_type():
    notes = Notes()
    with pytest.raises(TypeError):
        notes._get_by_note_number(1.0)
