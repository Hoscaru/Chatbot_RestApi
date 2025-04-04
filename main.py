from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from schemas.schema import User, UserForm, Prompt
from core.modelo import model
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

# instance of fastapi
app = FastAPI(title="FastAPI with Langchain",)


# user object list
users = [{"id": 1, "name": "John Doe", "age": 25},
         {"id": 2, "name": "Jane Doe", "age": 30},
         {"id": 3, "name": "Alice", "age": 35},
         {"id": 4, "name": "Bob", "age": 40}]

@app.get("/users")
def get_all_users()-> dict:
    return {
        "messages": "Successfully retrieved all users",
        "data": users
    }


@app.get("/users/{user_id}/")

def get_user_by_id(user_id: int)-> dict:
    for user in users:
        if user["id"] == user_id:
            return {
                "messages": "Successfully retrieved user by id",
                "data": user
            }
    raise HTTPException(status_code=404, detail="User not found")

@app.post(
    "/users"
    )

def create_user(user: User)-> dict:
    user_data = user.model_dump()
    return {
        "messages": "Successfully created user",
        "data": user_data
    }

# Create post to ask for user data


@app.post("/form")

def create_user_form(user: UserForm)-> dict:
    user_data = user.model_dump()
    return {
        "messages": "Successfully fetched all user",
        "data": f"user {user.name}."
        
    }

# Create bot with langchain




messages = [
    SystemMessage(content="Te llamas roberto"),
    ]


@app.post("/bot", tags=["bot"], summary="Chat with the bot")
def chat_with_bot(prompt: Prompt)-> dict:
    messages.append(HumanMessage(content=prompt.prompt))
    response = model.invoke(messages)
    messages.append(response)
    return {
        # return the last message
        "messages": "Successfully retrieved bot response",
        "data": messages[-1].content
        
    }