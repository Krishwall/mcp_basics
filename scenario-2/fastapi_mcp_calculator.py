#HTTP

from fastapi import FastAPI
from fastapi_mcp import FastApiMCP

#1 Let's create a FastAPI app
app = FastAPI(title="MCP Calculator API", version="1.0.0")

@app.post("/multiply")
def multiply(a: float, b: float) -> float:
    """Multiplies two numbers.
    
    args:
        a (float): The first number.
        b (float): The second number.
    returns:
        float: The product of the two numbers."""
    return a * b

@app.post("/divide")
def divide(a: float, b: float) -> float:
    """Divides one number by another.
    
    args:
        a (float): The numerator.
        b (float): The denominator.
    returns:
        float: The quotient of the two numbers."""
    if b == 0:
        raise ValueError("Denominator cannot be zero.")
    return a / b

@app.post("/add")
def add(a: float, b: float) -> float:
    """Adds two numbers.
    
    args:
        a (float): The first number.
        b (float): The second number.
    returns:
        float: The sum of the two numbers."""
    return a + b
@app.post("/subtract")
def subtract(a: float, b: float) -> float:
    """Subtracts one number from another.
    
    args:
        a (float): The number to be subtracted from.
        b (float): The number to subtract.
    returns:
        float: The difference of the two numbers."""
    return a - b
#2 . converting it to mcp
mcp=FastApiMCP(app, name="CalculatorAPI")
mcp.mount_http()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost",port=8002)