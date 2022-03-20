#import flask library
from tkinter.messagebox import ABORT
from flask import Flask,abort
from mock_data import catalog
import json


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


################################################################################
################################# API ENDPOINTS ################################
################################# RETURN JSON ################################
################################################################################

#Retrive the catalog 
@app.route("/api/products",methods=['GET'])
def get_catalog():    
    return json.dumps(catalog)

#Post method test
@app.route("/api/products",methods=['POST'])
def save_catalog():
    return "POST METHOD WORKING"

#Count every product in the catalog
@app.route("/api/products/count",methods=['GET'])
def count_products():
    
    return json.dumps(len(catalog))

#Get the sum of all products
@app.route("/api/products/total",methods=['GET'])
def total_products():

    total=0
    for x in catalog:
        total=x['price']+total  

    return json.dumps(total)

#Get the product by ID <Sending the ID>
@app.route("/api/products/<id>",methods=['GET'])
def id_products(id):
    for x in catalog:
        if x['_id'] == id:
            return json.dumps(x)

    return abort(404,"There is no product with such ID")
    

   




#Run the app on debug mode 
app.run(debug=True)
