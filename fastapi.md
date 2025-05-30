# FastAPI Backend Engineer Study Guide

---

## 1. **Introduction to FastAPI**

**FastAPI** is a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints. It is designed for speed, developer productivity, and easy integration with modern Python features.

- **Key Features:**
  - Asynchronous support with `async`/`await`
  - Automatic data validation using Pydantic
  - Automatic API docs (Swagger UI, Redoc)
  - Dependency Injection system
  - Based on Starlette (web parts) and Pydantic (data parts)
  - Type hints for intuitive code and editor support

---

## 2. **Project Structure and Setup**

**Typical Project Structure:**
```
myapp/
├── app/
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   ├── dependencies.py
│   └── routers/
│       ├── users.py
│       └── items.py
├── tests/
│   └── test_main.py
├── requirements.txt
└── README.md
```

**Installation:**
```sh
pip install fastapi uvicorn
```
- `uvicorn` is an ASGI server to run FastAPI apps.

---

## 3. **Core Concepts**

### 3.1. **Creating a Basic API**
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
```
- Use decorators: `@app.get`, `@app.post`, `@app.put`, `@app.delete`

### 3.2. **Path and Query Parameters**
```python
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
```
- Path parameters: `/items/{item_id}`
- Query params: `/items/1?q=search`

### 3.3. **Request Body and Data Validation**
FastAPI uses Pydantic models for validation:
```python
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None

@app.post("/items/")
def create_item(item: Item):
    return item
```

### 3.4. **Automatic Docs**
- Swagger UI: `/docs`
- Redoc: `/redoc`

---

## 4. **Advanced FastAPI Features**

### 4.1. **Asynchronous Endpoints**
```python
@app.get("/async")
async def get_async():
    await some_async_func()
    return {"msg": "done"}
```

### 4.2. **Dependency Injection**
```python
from fastapi import Depends

def common_params(q: str = None):
    return q

@app.get("/items/")
def read_items(q: str = Depends(common_params)):
    return {"q": q}
```
- Use `Depends` to inject reusable logic (DB sessions, authentication, etc).

### 4.3. **Response Models**
```python
class ItemOut(BaseModel):
    name: str
    price: float

@app.get("/items/{item_id}", response_model=ItemOut)
def read_item(item_id: int):
    ...
```
- Controls what is sent to the client (output filtering).

### 4.4. **Background Tasks**
```python
from fastapi import BackgroundTasks

def write_log(message: str):
    with open("log.txt", "a") as f:
        f.write(message)

@app.post("/send-notification/")
def send_notification(email: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(write_log, f"Notified {email}\n")
    return {"message": "Notification sent"}
```

### 4.5. **Custom Exception Handling**
```python
from fastapi import HTTPException

@app.get("/resource/{id}")
def get_resource(id: int):
    if id > 10:
        raise HTTPException(status_code=404, detail="Not found")
    return {"id": id}
```

### 4.6. **Middleware**
```python
from fastapi import Request

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Process-Time"] = "0"
    return response
```

---

## 5. **Database Integration**

### 5.1. **SQLAlchemy Example**
```python
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
```
- Use a DB session dependency with `Depends`.

### 5.2. **Dependency for DB Session**
```python
from fastapi import Depends

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/users/")
def read_users(db: Session = Depends(get_db)):
    return db.query(User).all()
```

---

## 6. **Authentication & Security**

- FastAPI has built-in support for OAuth2, JWT tokens, and API keys.
- Use `fastapi.security` for OAuth2PasswordBearer, APIKeyHeader, etc.

**Example: OAuth2 with Password (JWT)**
```python
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.get("/users/me")
def read_users_me(token: str = Depends(oauth2_scheme)):
    return {"token": token}
```

**Hashing passwords:** Use `passlib` or `bcrypt`.

---

## 7. **Testing FastAPI Applications**

Use `TestClient` from FastAPI (based on Starlette) and `pytest`.
```python
from fastapi.testclient import TestClient

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}
```

---

## 8. **Deployment Best Practices**

- Use `uvicorn` or `gunicorn` with async workers.
- Use environment variables for configuration.
- Add CORS middleware if needed.
- Use `.env` files and tools like `python-dotenv` for secrets.
- Structure your project for scalability (routers, services, db, dependencies).

---

## 9. **Frequently Asked Interview Questions**

**Basic:**
- What is FastAPI? What are its main advantages?
- How does FastAPI handle data validation?
- How are path and query parameters handled in FastAPI?
- How does FastAPI generate interactive API docs?

**Intermediate:**
- Explain the role of Pydantic in FastAPI.
- What’s the difference between `@app.get` and `@app.post`?
- How do you handle authentication in FastAPI?
- What is dependency injection? Give an example in FastAPI.
- How do you manage database sessions per request?

**Advanced:**
- How does FastAPI leverage type hints for validation and docs?
- Explain how to write and use custom middleware.
- How would you implement JWT-based authentication?
- How do you write background tasks in FastAPI?
- How would you structure a large FastAPI project?
- What is ASGI? How is it different from WSGI?
- How do you ensure thread safety in your FastAPI backend?
- How can you implement rate limiting?
- How would you test async endpoints?

**Behavioral/System Design:**
- How would you design a scalable RESTful API for an e-commerce store using FastAPI?
- How would you handle long-running tasks or background jobs?
- What are your strategies for securing a FastAPI backend?
- How do you manage environment-specific settings and secrets?
- How do you ensure your API is maintainable as it grows?

---

## 10. **Preparation & Practice Checklist**

- [ ] Build a simple CRUD FastAPI project (users/items).
- [ ] Add authentication (JWT or OAuth2).
- [ ] Integrate with a real database (PostgreSQL/MySQL/SQLite).
- [ ] Write unit and integration tests.
- [ ] Set up middleware and custom exception handlers.
- [ ] Deploy your app with `uvicorn` and Docker.
- [ ] Practice explaining core concepts and your code.

---

## 11. **Useful Links & Further Reading**

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [FastAPI Tutorials](https://fastapi.tiangolo.com/tutorial/)
- [Pydantic Docs](https://docs.pydantic.dev/)
- [SQLAlchemy Docs](https://docs.sqlalchemy.org/)
- [TestClient Docs](https://fastapi.tiangolo.com/tutorial/testing/)
- [OAuth2 & JWT Example](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/)
- [Starlette Docs](https://www.starlette.io/)

---

## 12. **Pro Tips**

- Use type hints everywhere for best FastAPI experience.
- Use routers to split your API into logical modules.
- Always validate and sanitize incoming data.
- Secure your endpoints (authentication, CORS, rate limiting).
- Write clear, maintainable, and well-documented code.
- Learn the basics of async programming in Python (`async`/`await`).

---

