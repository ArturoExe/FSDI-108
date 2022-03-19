#import flask library
from flask import Flask

#create the application "server"
app= Flask("Server")

## App routes
#Root route
@app.route("/")
def home():
    return "Hello from flask"

#Me route
@app.route("/me")
def about_me():
    return "Arturo Martinez Jr"



#Run the app on debug mode 
app.run(debug=True)