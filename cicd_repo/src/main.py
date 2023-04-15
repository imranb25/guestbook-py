from fastapi import FastAPI, HTTPException
app = FastAPI()

@app.get("/")
async def read_main():
    return {"msg": "Hello, world!"}

@app.get("/one-to-ten/{number}")
async def read_number(number):
    try:
        number = int(number)
    except ValueError as err:
        raise HTTPException(status_code=400, detail="invalid input!") from err
    if number < 1 or number > 10:
        raise HTTPException(
                    status_code=422, detail="Only numbers 1-10 are accepted!")
    return {"number": {"binary": bin(number), "hexadecimal": hex(number), "octal": oct(number)}}

