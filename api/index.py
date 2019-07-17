from flask import Flask
from flask_restful import Api
from api import Meter,get_query_all_meters, get_query_each_meters
from api import Meter_Id, Customer_Id
from flask import request
import status




app = Flask(__name__)

api = Api(app)


# Route_1
api.add_resource(Meter, '/measure/meters/all')
# Route_2
api.add_resource(Meter_Id, '/measure/meters/<m_id>')
# Route_3
api.add_resource(Customer_Id, '/measure/meters/customer/<c_id>')
# Route_4   #/measure/query?From= &to=   #2018-08-16  format
api.add_resource(get_query_all_meters, '/measure/query',)
# Route_4  #/measure/query/eachM?eterID= &From= &to=   #2018-08-16
api.add_resource(get_query_each_meters, '/measure/query/eachM',)




@app.route('/measure/get_Jeson', methods=['POST']) # from postman
def get_Jeson():
    req_data = request.get_json()
    From = req_data['From']
    to = req_data['to']
    return '''
        From is {}.
        to is {}.
       '''.format(From,to)




#Form ***********

# @app.route('/measure/form', methods=['POST','GET'])
# def get_form():
#     if request.method =='POST':
#         From = request.form.get('From')
#         to = request.form.get('to')
#         return 'From : ' + From + ' to : ' + to
#
#     return '''<form method="POST">
#     Start_date <input type="text" name="start_date">
#     End_date <input type="text" name="End_date">
#     <input type ="submit">
#     </form>'''

if __name__ == "__main__":
    app.run(host='localhost', port=5001, debug=True)
