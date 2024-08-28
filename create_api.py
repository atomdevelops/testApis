
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

# Configure CORS
origins = [
    "http://localhost:8000",
    "http://localhost:4200",
    "http://localhost:4201",
    "http://localhost:4202",
    "http://0.0.0.0:4200",
    "http://0.0.0.0:4201",
    "http://0.0.0.0:4202",
    "http://0.0.0.0:8000",
    # Add more origins if needed, e.g., "https://example.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class User(BaseModel):
    id: int
    name: str
    email: str

class Item(BaseModel):
    id: int
    name: str
    price: float

class Customer(BaseModel):
    customerId: int
    name: str
    emailId: str
    mobileNo: str
    address: str

# create Customer List
customers = [
    Customer(customerId=1, name="Jone Dane", emailId="jone.dane@gmail.com", mobileNo="8372636", address="Ontario, Canada"),
    Customer(customerId=2, name="Smith Gotham", emailId="gotham.smith@gmail.com", mobileNo="5544345", address="Paris, France")
]

# Create a list to store the data
users = [
    User(id=1, name="John Doe", email="john@example.com"),
    User(id=2, name="Jane Doe", email="jane@example.com")
]

items = [
    Item(id=1, name="Item 1", price=10.99),
    Item(id=2, name="Item 2", price=5.99)
]

# Define the API endpoints for the Customer
@app.get("/customers/")
async def read_customers():
    return customers

@app.get("/customers/{customer_ID}")
async def read_customer(customer_ID: int):
    for customer in customers:
        if customer.customerId == customer_ID:
            return customer
    return "Customer not found!"

@app.post("/customers/")
async def create_customer(customer: Customer):
    maxid = getMaxId()
    customer.customerId = maxid
    customers.append(customer)
    return customers

@app.put("/customers/{cust_id}")
async def update_customer(cust_id: int, customer: Customer):
    for i ,existing_customer in enumerate(customers):
        if(existing_customer.customerId == cust_id):
            customers[i] = customer
            return customer
    return "error: Customer Not found!"

@app.delete("/customers/{cust_id}")
async def delete_customer(cust_id: int):
    for i ,existing_customer in enumerate(customers):
        if(existing_customer.customerId == cust_id):
            del customers[i]
            return "messge: Customer deleted!"
    return "error: Customer Not found!"

def getMaxId():
    if customers:
        return max(customer.customerId for customer in customers) + 1
    else:
        return 1




# Define the API endpoints
@app.get("/users/")
async def read_users(customer: Customer):
    customers.append(customer)
    return customer

@app.get("/users/{user_id}")
async def read_user(user_id: int):
    for user in users:
        if user.id == user_id:
            return user
    return {"error": "User not found"}

@app.post("/users/")
async def create_user(user: User):
    users.append(user)
    return user

@app.put("/users/{user_id}")
async def update_user(user_id: int, user: User):
    for i, existing_user in enumerate(users):
        if existing_user.id == user_id:
            users[i] = user
            return user
    return {"error": "User not found"}


@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    for i, user in enumerate(users):
        if user.id == user_id:
            del users[i]
            return {"message": "User deleted"}
    return {"error": "User not found"}

@app.get("/items/")
async def read_items():
    return items

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    for item in items:
        if item.id == item_id:
            return item
    return {"error": "Item not found"}

@app.post("/items/")
async def create_item(item: Item):
    items.append(item)
    return item

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    for i, existing_item in enumerate(items):
        if existing_item.id == item_id:
            items[i] = item
            return item
    return {"error": "Item not found"}

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    for i, item in enumerate(items):
        if item.id == item_id:
            del items[i]
            return {"message": "Item deleted"}
    return {"error": "Item not found"}



# 1. create the Virtual enviroment
# > python -m venv myenv

# 2. First Activate the Virtual enviroment with below command.
# > source venv/bin/activate

# go to the createApi folder which have the create_api.py file

# 3. Install the fastApi and uvicorn
# > pip install fastapi uvicorn

# 4. to the the fastApi we user the uvicorn use below bommand
# > uvicorn create_api:app --host 0.0.0.0 --port 8000

# 5 command to the new user with the terminal
# > curl -X POST -H "Content-Type: application/json" -d '{"id": 3, "name": "New User", "email": "newuser@example.com"}' http://localhost:8000/users/
