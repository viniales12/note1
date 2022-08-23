from flask import Blueprint, request, make_response

from src.notes_api.models.note import Note, db
from src.notes_api.routes.common.exceptions import NotFoundException, InvalidPayload

notes = Blueprint('notes', __name__)


@notes.route('/v1/notes', methods=['GET'])
def get_notes():
    notes = db.session.query(Note).all()
    if notes:
        notes_list = [{
            'id': note.id,
            'created_at': note.created_at,
            'title': note.title,
            'body': note.body
        } for note in notes]
        return {
            'status': 'success',
            'data': {
                'notes': notes_list
            }
        }
    else:
        return {
            'status': 'success',
            'message': "No notes in database."
        }


@notes.route('/v1/notes/<note_id>', methods=['GET'])
def get_note(note_id: int):
    try:
        note = db.session.query(Note).filter_by(id=note_id).one_or_none()
        if not note:
            raise NotFoundException(message='Note does not exist.')
        return {
            'status': 'success',
            'data': {
                'id': note.id,
                'created_at': note.created_at,
                'title': note.title,
                'body': note.body
            }
        }
    except NotFoundException:
        return {
            'status': 'success',
            'message': "No notes in database with given ID."
        }


@notes.route('/v1/notes', methods=['POST'])
def add_note():
    req = request.get_json()

    if not req:
        raise InvalidPayload()

    title = req.get('title')
    body = req.get('body')

    try:
        note = Note(title=title, body=body)
        db.session.add(note)
        db.session.commit()
        return {
                   'status': 'success',
                   'message': f"Note {title} added successfully!"
               }, 201
    # TODO: exception to broad, find what exception can be thrown in try block
    except:
        raise InvalidPayload()


@notes.route('/v1/notes/<note_id>', methods=['DELETE'])
def delete_note(note_id: int):
    note = Note.query.get_or_404(note_id)
    db.session.delete(note)
    db.session.commit()
    return make_response("", 204)


@notes.route('/v1/notes/<note_id>', methods=['PATCH'])
def patch_note(note_id: int):
    note = Note.query.get_or_404(note_id)
    note.title = request.get_json()["title"]
    note.body = request.get_json()["body"]
    db.session.commit()
    return {
            'status': 'success',
            'message': "Data has been updated"
        }

