from flask import Flask
from datetime import datetime
app = Flask(__name__)

data = {
    "software": [
        {
            "name": "Dooby", 
            "price": "$50",
            "date": datetime.now()
            },
            {
            "name": "Tantan", 
            "price": "$30",
            "date": datetime.now()
            }
    ]
} 

@app.route("/")
def index():
        return "Quick CD Test."

@app.route('/software')
def get_software():
    return data


if __name__ == "__main__":
    app.debug = True
    app.run()