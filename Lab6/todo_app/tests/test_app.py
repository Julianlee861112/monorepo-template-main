from src.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_read_api():
    response = client.get("/api")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}


def test_read_book_by_path_param():
    response = client.get("/books/book1")
    assert response.status_code == 200
    assert response.json() == {"msg": "book1"}


def test_read_books_by_title():
    response = client.get("/books/", params={"title": "A Book"})
    assert response.status_code == 200
    assert response.json() == {"msg": "A Book"}


def test_create_book():
    response = client.post("/books/create_book",
                           json={"title": "Book", "author": "Author1"})
    assert response.status_code == 200
    assert response.json() == {
        "msg": {"title": "Book", "author": "Author1"}}


def test_update_book():
    response = client.put(
        "/books/1", json={"title": "Updated Book", "author": "Updated Author"})
    assert response.status_code == 200
    assert response.json() == {"book_id": "1", "updated_book": {
        "title": "Updated Book", "author": "Updated Author"}}


def test_delete_book():
    response = client.delete("/books/1")
    assert response.status_code == 200
    assert response.json() == {"book_id": "1"}
