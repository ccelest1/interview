# [FastAPI - Using GraphQL](https://www.geeksforgeeks.org/python/fastapi-using-graphql/)

- FastAPI and GraphQl = big players in API development
    * GQL -> prioritizes efficiency, flexibility in data retrieval
        * Empowers clients to dictate shape, data depth required leading to more efficient data retrieval processes
        * selective data retrieval

- FastAPI: Speed, simplicity, async support
    * Automatic validation with Python type-hints

## Integration
1. `python -m venv venv` (Create virtual env)
2. activate bin or `venv\Scripts\activate`
3. `pip install fastapi strawberry-graphql uvicorn` (install libraries)
4. `main.py`
```py
from fastapi import FastAPI
from ariadne import QueryType, gql, make_executable_schema
from ariadne.asgi import GraphQL

# define graphql query type
query = QueryType()

# resolver defined for book query
@query.field('book')
def resolve_book(*_):
    return {
        'title':"GraphQL Tutorial",
        'author':'GFG'
    }

def resolve_books(*_):
    return [
        {"title": "Book 1", "author": "Author 1"},
        {"title": "Book 2", "author": "Author 2"},
        {"title": "Book 3", "author": "Author 3"},
    ]
# define graphql schema using GQL function
type_defs = gql("""

    type Book{
        title: String
        author: String
    }

    type Query{
        book: Book
        books:[Book]
    }

""")

schema = make_executable_schema(
    type_defs,
    query
)

app = FastAPI()
graphql_app =  GraphQL(
    schema,
    debug=True
)
app.mount(
    '/graphql',
    graphql_app
)
if __name__ == "__main__"L
    import uvicorn
    uvicorn.run(
        app,
        host = '127.0.0.1",
        port = 8000
    )
```
3. Run server -> `uvicorn main:app --reload` or using python command
    * `http://127.0.0.1:8000/graphql`
