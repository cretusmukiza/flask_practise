from flask import Blueprint,request
from api.utils.responses import response_with
from api.models.book import BookSchema,Books
from api.utils.database import db
import api.utils.responses as resp

book_routes = Blueprint('book_routes',__name__)
def has_property(data,property):
        it_exist = data.get(property,None)
        return False if it_exist is None else True
@book_routes.route('/',methods=['POST'])
def create_book():
    try:
        data = request.get_json()
        book_schema = BookSchema()
        book = book_schema.load(data)
        result = book_schema.dump(book.create())
        return response_with(resp.SUCCESS_201,value={"book":result})
    except Exception as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422)

@book_routes.route('/',methods=['GET'])
def get_books_list():
    fetched = Books.query.all()
    book_schema = BookSchema(many=True,only=['year','title','author_id','id'])
    books = book_schema.dump(fetched)
    return resp.response_with(resp.SUCCESS_200,value={"books":books})

@book_routes.route('/<int:book_id>',methods=['GET'])
def get_book_details(book_id):
    fetched = Books.query.get(book_id)
    book_schema = BookSchema()
    book = book_schema.dump(fetched)
    return resp.response_with(resp.SUCCESS_200,value={"book":book})

@book_routes.route('/<int:book_id>',methods=['PUT'])
def update_book_details(book_id):
    data = request.get_json()
    get_book = Books.query.get(book_id)
    get_book.author_id  = data['author_id']
    get_book.title = data['title']
    get_book.year = data['year']
    db.session.add(get_book)
    db.session.commit()
    book_schema = BookSchema()
    book = book_schema.dump(get_book)
    return resp.response_with(resp.SUCCESS_200,value={"book":book})

@book_routes.route('/<int:book_id>',methods=['PATCH'])
def modify_book_details(book_id):
    data = request.get_json()
    get_book = Books.query.get(book_id)
    if has_property(data,'author_id'):
        get_book.author_id = data['author_id']
    if has_property(data,'year'):
        get_book.year = data['year']
    if has_property(data,'title'):
        get_book.title = data['title']
    db.session.add(get_book)
    db.session.commit()
    book_schema = BookSchema()
    book = book_schema.dump(get_book)
    return resp.response_with(resp.SUCCESS_200,value={"book":book})

@book_routes.route('/<int:book_id>',methods=['DELETE'])
def delete_book(book_id):
    get_book = Books.query.get(book_id)
    db.session.delete(get_book)
    db.session.commit()
    return resp.response_with(resp.SUCCESS_204)





