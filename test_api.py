from fastapi import FastAPI

from pythonProject1.api import app


@app.get("/tests/solved_tests")
def get_solved_tests():
    pass

@app.get("/tests/statistics")
def get_statistics():
    pass

@app.post("/tests")
def add_test():
    pass

@app.delete("/tests/{test_id}")
def delete_test(test_id: int):
    pass

@app.get("/tests/{test_id}")
def get_test(test_id: int):
    pass

@app.put("/tests/{test_id}")
def update_test(test_id: int):
    pass