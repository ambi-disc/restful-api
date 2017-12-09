from flask import Flask, jsonify, request
import mysql.connector
from flask import abort

from map import age_map, ethnicity_map, race_map, education_map, house_income_map, occupation_map, residence_map, \
    parity_map, poh_map, mhdp_map, method_of_delivery_map, pbe_map, breast_feeding_duration_map, pumping_method_map, \
    infant_state_map, maternal_problems_map, latching_map, pumping_amount_map, side_map, suptype_map, supmethod_map, \
    number_of_diapers_map, total_amount_map, total_amount_today, urine_color_map, urine_saturation_map, stool_color_map, \
    stool_consistency_map

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
        try:
            mother = {
                'name': Name,
                'motherId': mid,
                'address': Address,
                'age': age_map(Age),
                'ethnicity': ethnicity_map(Ethnicity),
                'race': race_map(Race),
                'education': education_map(Education),
                'houseIncome': house_income_map(HouseIncome),
                'occupation': occupation_map(Occupation),
                'residence': residence_map(Residence),
                'parity': parity_map(Parity),
                'poh': poh_map(POH),
                'mhdp': mhdp_map(MHDP),
                'methodOfDelivery': method_of_delivery_map(MethodOfDelivery),
                'pbe': pbe_map(PBE),
                'phone': Phone
            }
            mothers.append(mother)
        except KeyError:
            print("Mother with id %s has a null value, and will not be returned as a result." % mid)
    return jsonify(
        mothers=mothers
    )
'''
@app.route('/scientists')
def get_scientists_info():
    query=('SELECT * FROM Scientists')
    db = mysql.connector.connect(user='EPICS', password='EPICS2017', database='lactor', host='166.62.75.128', port=3306)
    authToken = request.args.get('authToken')

    # TODO actual user verification
    if authToken != 'AXNTHAUONTUOAENHTOEUA':
        abort(403)

    cursor = cnx.cursor()
    cursor.execute(query)

    scientists = []

    for(sid, email, password, loginstep, admin, hospital_id, name) in cursor:
        try:
            scientists = {
                'scientistid'= sid,
                'email' = email,
                'password' = password,
                'loginstep' = loginstep,
                'admin' = admin,
                'hospitalid'= hospital_id,
                'name' = name
            
                    
            }
            print(scientists)
            r
'''

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
        suffix_to_query+= " AND EntryDate > STR_TO_DATE(%s, %d,%m,%Y)"
        sqlParams += (startDate,)
    if endDate is not None:
        suffix_to_query+= " AND EntryDate < STR_TO_DATE(%s, %d,%m,%Y)"
        sqlParams += (endDate,)


    # Queries for breastfeeding entries, supplement entries, output entries, and morbidity entries
    breastfeeding_query = """
        SELECT BreastfeedingDuration,
               PumpingMethod,
               InfantState,
               MaternalProblems,
               Latching,
               Side,
               PumpingAmount,
               DATE_FORMAT(EntryDate, '%b %e, %Y') as EntryDate
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
               NumberTimes,
               DATE_FORMAT(EntryDate, '%b %e, %Y') as EntryDate
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
               NumberDiapers,
               DATE_FORMAT(EntryDate, '%b %e, %Y') as EntryDate
        FROM OutputEntry
        INNER JOIN Diary
        ON Diary.EntryId = OutputEntry.EntryId
        WHERE mid = %s
    """

    morbidity_query = """
        SELECT Type,
               DATE_FORMAT(EntryDate, '%b %e, %Y') as EntryDate
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

    for(BreastfeedingDuration, PumpingMethod, InfantState, MaternalProblems, Latching, Side, PumpingAmount, EntryDate) in cursor:
        print("Hi 1")
        if(BreastfeedingDuration == None or PumpingAmount == None or InfantState == None or MaternalProblems == None or Latching == None or Side == None or PumpingAmount == None):
            continue
        print("Hi 2")
        breastfeeding_diary.append({
            'breastfeedingduration': breast_feeding_duration_map(BreastfeedingDuration),
            'pumpingmethod': pumping_method_map(PumpingMethod),
            'infantstate': infant_state_map(InfantState),
            'maternalproblems': maternal_problems_map(MaternalProblems),
            'latching': latching_map(Latching),
            'side': side_map(Side),
            'pumpingamount': pumping_amount_map(PumpingAmount),
            'entryDate': EntryDate
        })

    cursor.close()
    cursor = db.cursor()
    cursor.execute(supplement_query, sqlParams)

    for(SupType, SupMethod, NumberDiapers, TotalAmount, NumberTimes, EntryDate) in cursor:
        if(SupType == None or SupMethod == None or NumberDiapers == None or TotalAmount == None or NumberTimes == None):
            continue
        supplement_diary.append({
            'suptype': suptype_map(SupType),
            'supmethod': supmethod_map(SupMethod),
            'numberofdiapers': number_of_diapers_map(NumberDiapers),
            'totalamount': total_amount_map(TotalAmount),
            'numbertimes': total_amount_today(NumberTimes),
            'entryDate': EntryDate
        })

    cursor.close()
    cursor = db.cursor()
    cursor.execute(output_query, sqlParams)

    for(UrineColor, UrineSaturation, StoolColor, StoolConsistency, NumberDiapers, EntryDate) in cursor:
        if(UrineColor == None or UrineSaturation == None or StoolColor == None or StoolConsistency == None or NumberDiapers == None):
            continue
        output_entries.append({
            'urinecolor': urine_color_map(UrineColor),
            'urinesaturation': urine_saturation_map(UrineSaturation),
            'stoolcolor': stool_color_map(StoolColor),
            'stoolconsistency': stool_consistency_map(StoolConsistency),
            'numberdiapers': number_of_diapers_map(NumberDiapers),
            'entryDate': EntryDate
        })

    cursor.close()
    cursor = db.cursor()
    cursor.execute(morbidity_query, sqlParams)

    for(Type, EntryDate) in cursor:
        if(Type == None or EntryDate == None):
            continue
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
