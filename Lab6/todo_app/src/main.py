from fastapi import FastAPI, Body

app = FastAPI()


@app.get("/api")
def first_api():
    return {"msg": "Hello World"}


@app.get("/books/{path_param}")
def first_apiV2(path_param: str):
    return {"msg": path_param}


@app.get("/books/")
def first_apiV3(title: str):
    return {"msg": title}


@app.post("/books/create_book")
def first_apiV4(new_book=Body()):
    print(new_book)
    return {"msg": new_book}


@app.put("/books/{book_id}")
def update_book(book_id: str, updated_book: dict = Body(...)):
    return {"book_id": book_id, "updated_book": updated_book}


@app.delete("/books/{book_id}")
def delete_book(book_id: str):
    return {"book_id": book_id}
