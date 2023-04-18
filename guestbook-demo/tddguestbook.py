def test_new_note():
    notes = []
    add_note_command = 'new This is my note'
    command_parts = add_note_command.split(' ')
    assert len(command_parts) >= 2
    if command_parts[0] == 'new':
        note = ' '.join(command_parts[1:])
        notes.append(note)
        assert len(notes) == 1
        assert notes[0] == 'This is my note'

def test_list_notes():
    notes = ['Note 1', 'Note 2', 'Note 3']
    list_command = 'list'
    command_parts = list_command.split(' ')
    assert len(command_parts) >= 1
    if command_parts[0] == 'list':
        if len(notes) == 0:
            assert 'No entries found.' in str(excinfo.value)
        else:
            expected_output = ''
            for index, note in enumerate(notes):
                expected_output += f"{index+1}) {note}\n"
            assert expected_output.strip() == '1) Note 1\n2) Note 2\n3) Note 3'

def test_edit_note():
    notes = ['Note 1', 'Note 2', 'Note 3']
    edit_command = 'edit 2 Edited note'
    command_parts = edit_command.split(' ')
    assert len(command_parts) >= 3
    if command_parts[0] == 'edit':
        index = int(command_parts[1])
        if index > 0 and index <= len(notes):
            new_note = ' '.join(command_parts[2:])
            notes[index-1] = new_note
            assert len(notes) == 3
            assert notes == ['Note 1', 'Edited note', 'Note 3']

def test_delete_note():
    notes = ['Note 1', 'Note 2', 'Note 3']
    delete_command = 'delete 1'
    command_parts = delete_command.split(' ')
    assert len(command_parts) >= 2
    if command_parts[0] == 'delete':
        index = int(command_parts[1])
        if index > 0 and index <= len(notes):
            deleted_note = notes.pop(index-1)
            assert len(notes) == 2
            assert deleted_note == 'Note 1'
            assert notes == ['Note 2', 'Note 3']
