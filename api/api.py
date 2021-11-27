from flask import Flask

app = Flask(__name__)

@app.route('/api',methods=['GET','POST'])
def get_forecast():

    #return {'time': time.time()}
    return {'foo': 'bar'}

# error handling
@app.errorhandler(Exception)
def resource_not_found(e):
    return {'Error': str(e)}