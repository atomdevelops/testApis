
## 1. create the Virtual enviroment
## > python -m venv myenv

## 2. First Activate the Virtual enviroment with below command.
### > source venv/bin/activate

## go to the createApi folder which have the create_api.py file

## 3. Install the fastApi and uvicorn
### > pip install fastapi uvicorn

## 4. to the the fastApi we user the uvicorn use below bommand
### > uvicorn create_api:app --host 0.0.0.0 --port 8000

## 5 command to the new user with the terminal
### > curl -X POST -H "Content-Type: application/json" -d '{"id": 3, "name": "New User", "email": "newuser@example.com"}' http://localhost:8000/users/
