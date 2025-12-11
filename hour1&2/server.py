from flask import Flask

app = Flask(__name__)

# Ithu thaan namma "Waiter". User enga ponaalum (Route), enna tharanum nu solrom.
@app.route('/')
def home():
    return "Hello World! Naan AI help oda idhai create panniten!"

if __name__ == '__main__':
    app.run(debug=True)