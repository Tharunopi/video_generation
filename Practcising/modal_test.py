import modal

app = modal.App("eg_app")

@app.function()
def greet(name:str):
    return f"Hi! {name}"

@app.local_entrypoint()
def main():
    print(greet.remote("Tharun"))