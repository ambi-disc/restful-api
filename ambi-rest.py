from flask import Flask, jsonify, request
import mysql.connector
from flask import abort

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/account/create', methods=['POST'])
def create_account_endpoint():
    return jsonify(
        success=True,
        authToken="aTHN45nthuoe43+?",
        timeoutTimestamp="1635094775"
    )


@app.route('/account/login', methods=['POST'])
def login_endpoint():
    return jsonify(
        success=True,
        authToken="aTHN45nthuoe43+?",
        timeoutTimestamp="1635094775"
    )


@app.route('/account/verify_token')
def verify_token_endpoint():
    return jsonify(
        valid=True
    )

@app.route('/mothers')
def get_mother_info():
    query = ('SELECT * FROM MotherInfo')
    cnx = mysql.connector.connect(user='EPICS', password='EPICS2017', database= 'lactor', host= '166.62.75.128', port=3306)

    authToken = request.args.get('authToken')

    # TODO actual user verification
    if authToken != 'AXNTHAUONTUOAENHTOEUA':
        abort(403)

    cursor = cnx.cursor()
    cursor.execute(query)

    mothers = []

    for( mid, Name, Address, Age, Ethnicity, Race, Education, HouseIncome, Occupation, Residence, Parity, POH, MHDP, MethodOfDelivery, PBE, Phone) in cursor:
        mother = {
            'name': mid,
            'motherId': Address,
            'address': Ethnicity,
            'age': Age,
            'ethnicity': Ethnicity,
            'race': Race,
            'education': Education,
            'houseIncome': HouseIncome,
            'occupation': Occupation,
            'residence': Residence,
            'parity': Parity,
            'poh': POH,
            'mhdp': MHDP,
            'methodOfDelivery': MethodOfDelivery,
            'pbe': PBE,
            'phone': Phone
        }
        print(mother)
        mothers.append(mother)
    print(mothers)
    return jsonify(
        mothers=mothers
    )

@app.route('/diary')
def get_diary_info():

    db = mysql.connector.connect(user='EPICS', password='EPICS2017', database= 'lactor', host= '166.62.75.128', port=3306)

    # Url Params
    authToken = request.args.get('authToken')
    motherId = request.args.get('motherId')
    startDate = request.args.get('startDate')
    endDate = request.args.get('endDate')

    # TODO actual user verification
    if authToken != 'AXNTHAUONTUOAENHTOEUA':
        abort(403)

    sqlParams = (motherId,)
    suffix_to_query = ''
    if startDate is not None:
        suffix_to_query+= " AND EntryDate > %s"
        sqlParams += (startDate,)
    if endDate is not None:
        suffix_to_query+= " AND EntryDate < %s"
        sqlParams += (endDate,)

    # Queries for breastfeeding entries, supplement entries, output entries, and morbidity entries
    breastfeeding_query = """
        SELECT BreastfeedingDuration,
               PumpingMethod,
               InfantState,
               MaternalProblems,
               Latching,
               Side,
               PumpingAmount
        FROM BreastfeedEntry 
        INNER JOIN Diary
        ON Diary.EntryId = BreastfeedEntry.EntryId
        WHERE mid = %s
    """

    supplement_query="""
        SELECT SupType,
               SupMethod,
               NumberDiapers,
               TotalAmount,
               NumberTimes
        FROM SupplementEntry
        INNER JOIN Diary
        ON Diary.EntryId = SupplementEntry.EntryId
        WHERE mid = %s
    """

    output_query = """
        SELECT UrineColor,
               UrineSaturation,
               StoolColor,
               StoolConsistency,
               NumberDiapers
        FROM OutputEntry
        INNER JOIN Diary
        ON Diary.EntryId = OutputEntry.EntryId
        WHERE mid = %s
    """

    morbidity_query = """
        SELECT Type,
               EntryDate
        FROM MorbidityEntry
        INNER JOIN Diary
        ON Diary.EntryId = MorbidityEntry.EntryId
        WHERE mid = %s
    """

    breastfeeding_diary=[]
    supplement_diary = []
    output_entries = []
    morbidity_entries = []

    cursor = db.cursor()
    cursor.execute(breastfeeding_query, sqlParams)

    for(BreastfeedingDuration, PumpingMethod, InfantState, MaternalProblems, Latching, Side, PumpingAmount) in cursor:
        breastfeeding_diary.append({
            'breastfeedingduration': BreastfeedingDuration,
            'pumpingmethod': PumpingMethod,
            'infantstate': InfantState,
            'maternalproblems': MaternalProblems,
            'latching': Latching,
            'side': Side,
            'pumpingamount': PumpingAmount
        })

    cursor.close()
    cursor = db.cursor()
    cursor.execute(supplement_query, sqlParams)

    for(SupType, SupMethod, NumberDiapers, TotalAmount, NumberTimes) in cursor:
        supplement_diary.append({
            'suptype': SupType,
            'supmethod': SupMethod,
            'numberofdiapers': NumberDiapers,
            'totalamount': TotalAmount,
            'numbertimes': NumberTimes
        })

    cursor.close()
    cursor = db.cursor()
    cursor.execute(output_query, sqlParams)

    for(UrineColor, UrineSaturation, StoolColor, StoolConsistency, NumberDiapers) in cursor:
        output_entries.append({
            'urinecolor': UrineColor,
            'urinesaturation': UrineSaturation,
            'stoolcolor': StoolColor,
            'stoolconsistency': StoolConsistency,
            'numberdiapers': NumberDiapers
        })

    cursor.close()
    cursor = db.cursor()
    cursor.execute(morbidity_query, sqlParams)

    for(Type, EntryDate) in cursor:
        morbidity_entries.append({
            'type': Type,
            'entryDate': EntryDate
        })

    cursor.close()
    db.close()

    return jsonify({
        'breastfeedEntries': breastfeeding_diary,
        'supplementEntries': output_entries,
        'outputEntries': supplement_diary,
        'morbidityEntries': morbidity_entries
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
