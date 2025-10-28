from flask import Flask,request, jsonify,render_template 
import os 
from flask_cors import CORS,cross_origin 
from src.cnnClassifier.pipeline.predict import PredictionPipeline
from src.cnnClassifier.utils.common import decodeImage 

os.putenv('LANGUAGE','en_US.UTF-8')
os.putenv('LC_ALL','en_US.UTF-8')

app = Flask(__name__) 
CORS(app) 

class ClientApp:
    def __init__(self): 
        self.filename = "input_image.jpg" 
        self.classifier = PredictionPipeline(self.filename)

@app.route('/',methods=['GET'])
@cross_origin()
def homePage(): 
    return render_template("index.html") 

@app.route('/train',methods=['GET','POST']) 
@cross_origin()
def trainRoute():
    os.system("python main.py") 
    return "Training Completed!" 

@app.route('/predict',methods=['POST'])
@cross_origin()
def predictRoute():
    image = request.json['image']
    decodeImage(image,client_app.filename) 
    result = client_app.classifier.predict()
    return jsonify(result) 

if __name__=="__main__":
    client_app = ClientApp()
    #local server : 5000 
    # Azure server : 80 
    app.run(host="0.0.0.0",port=80,debug=True)