from flask import Flask
from sqlalchemy import create_engine, text
from flask import abort, request, escape, make_response
import pickle
import pandas as pd


app = Flask(__name__)
model = pickle.load(open('projpredictlgs.pkl', 'rb'))

#Setup of db, we use sqlite for convenience.
engine = create_engine("sqlite+pysqlite:///drug_proj.db", echo=True)
conn= engine.connect()

#https://www.askpython.com/python-modules/pandas/read-pickle-files-in-pandas
df = pd.read_pickle('drugdataset.pkl')
# print the dataframe
print(df)

df.to_sql('drug_proj', conn, if_exists='replace', index = False)

@app.route('/getusers', methods=['GET'])
def getusers():
    """
    Gets all users in the db and passes them as json
    """
    global engine
    if request.method == "GET":
        with engine.connect() as conn:
            results=conn.execute(text("select * from drug_proj"))
            return {'data': [{'reporttype': r[0], 'fulfillexpeditecriteria': r[1],
                            'patientsex': r[2], 'reactionmeddrapt': r[3],
                            'reactionoutcome': r[4], 'drugcharacterization': r[5],
                            'medicinalproduct': r[6], 'drugdosageform': r[7],
                            'drugindication': r[8], 'actiondrug': r[9],'age_group':r[10],'target':r[11]} for r in results.fetchall()]}
    else: abort(405)

# Here we post json of maniputlate it and return a resulat.
@app.route('/prediction', methods=['POST', 'GET'])
def prediction():
    if request.method == "POST":
        if request.json and 'data' in request.json:
            df_predict_live = pd.DataFrame(request.json.get("data"),columns=["reporttype", "fulfillexpeditecriteria", "patientsex", "reactionmeddrapt", "reactionoutcome", "drugcharacterization", "medicinalproduct", "drugdosageform", "drugindication", "actiondrug", "age_group"])
            print(df_predict_live)
            return {"Prediction": int(model.predict(df_predict_live)[0])}
            # return {"Prediction": int(model.predict(request.json['data']))}
        else: abort(405)
    else: abort(405)


@app.route('/insert', methods=['PUT'])
def insert():
    """
    Takes json of the form {"username": username, "id": id} and puts in db
    """
    global engine
    if request.method == "PUT":
        #print(1)
        print(request.json)
        if request.json:
            try:
                print(2)
                with engine.connect() as conn:
                    print(3)
                    print(request.json['actiondrug'])
                    conn.execute(
                    text("INSERT INTO drug_proj (reporttype, fulfillexpeditecriteria, patientsex, reactionmeddrapt, reactionoutcome,\
                        drugcharacterization, medicinalproduct, drugdosageform, drugindication, actiondrug, \
                                   age_group, target) VALUES (:reporttype, :fulfillexpeditecriteria,:patientsex,\
                                            :reactionmeddrapt,:reactionoutcome,:drugcharacterization,:medicinalproduct,:drugdosageform,:drugindication,:actiondrug,:age_group,:target)"),
                            [{"reporttype": request.json['reporttype'], "fulfillexpeditecriteria": request.json['fulfillexpeditecriteria'],"patientsex": request.json['patientsex'],\
                                "reactionmeddrapt": request.json['reactionmeddrapt'],"reactionoutcome": request.json['reactionoutcome'],"drugcharacterization": request.json['drugcharacterization'],\
                                    "medicinalproduct": request.json['medicinalproduct'],"drugdosageform": request.json['drugdosageform'],"drugindication": request.json['drugindication'],\
                                        "actiondrug": request.json['actiondrug'],"age_group": request.json['age_group'],"target": request.json['target']}]
                        )
                    return "record created"
            except:
                abort(400)
        else: 
            abort(405)
    else: abort(405)



@app.errorhandler(405)
def malformed_query(error):
    """
    Redirects 405 errors
    """
    resp = make_response("Malformed Query")
    return resp
