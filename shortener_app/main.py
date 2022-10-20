from fastapi import FastAPI

app=FastAPI()


# path operation decorator to associate root path with
# read_root() ...now FastAPI will listens to root path n
# will delegate all incoming GET REQ to 
# this function 
@app.get("/")
def read_root():
    return "Heyyyy! WELcome to URL shortner API :P "


# python -m uvicorn shortener_app.main:app --reload 
# The --reload flag makes sure that your server will
#  reload automatically when you save your application’s code. 