from flask import Flask, jsonify, request
import mysql.connector
from flask import abort

from map import age_map, ethnicity_map, race_map, education_map, house_income_map, occupation_map, residence_map, \
    parity_map, poh_map, mhdp_map, method_of_delivery_map, pbe_map, breast_feeding_duration_map, pumping_method_map, \
    infant_state_map, maternal_problems_map, latching_map, pumping_amount_map, side_map, suptype_map, supmethod_map, \
    number_of_diapers_map, total_amount_map, total_amount_today, urine_color_map, urine_saturation_map, stool_color_map, \
    stool_consistency_map, type_map, notification_title_map, notification_description_map

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
        ORDER BY Diary.EntryDate DESC
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
        ORDER BY Diary.EntryDate DESC
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
        ORDER BY Diary.EntryDate DESC
    """

    morbidity_query = """
        SELECT Type,
               DATE_FORMAT(EntryDate, '%b %e, %Y') as EntryDate
        FROM MorbidityEntry
        INNER JOIN Diary
        ON Diary.EntryId = MorbidityEntry.EntryId
        WHERE mid = %s
        ORDER BY Diary.EntryDate DESC
    """

    breastfeeding_diary=[]
    supplement_diary = []
    output_entries = []
    morbidity_entries = []

    cursor = db.cursor()
    cursor.execute(breastfeeding_query, sqlParams)

    for(BreastfeedingDuration, PumpingMethod, InfantState, MaternalProblems, Latching, Side, PumpingAmount, EntryDate) in cursor:
        if(BreastfeedingDuration == None or PumpingAmount == None or InfantState == None or MaternalProblems == None or Latching == None or Side == None or PumpingAmount == None):
            continue
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
        if(SupType == None or SupMethod == None or TotalAmount == None or NumberTimes == None):
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
        print("Hi 1")
        if(UrineColor == None or UrineSaturation == None or StoolColor == None or StoolConsistency == None or NumberDiapers == None):
            continue
        print("Hi 2")
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
            'type': type_map(Type),
            'entryDate': EntryDate
        })

    cursor.close()
    db.close()

    return jsonify({
        'breastfeedEntries': breastfeeding_diary,
        'supplementEntries': supplement_diary,
        'outputEntries': output_entries,
        'morbidityEntries': morbidity_entries
    })


@app.route('/notifications')
def get_notifications():
    db = mysql.connector.connect(user='EPICS', password='EPICS2017', database= 'lactor', host= '166.62.75.128', port=3306)

    # Url Params
    authToken = request.args.get('authToken')
    motherId = request.args.get('motherId')

    # TODO actual user verification
    if authToken != 'AXNTHAUONTUOAENHTOEUA':
        abort(403)

    query = """
        SELECT status,
               ntype,
               DATE_FORMAT(NotificationIssued, '%b %e, %Y') as date
        FROM Notifications
        WHERE mid = %s
        ORDER BY NotificationIssued DESC
    """

    cursor = db.cursor()
    cursor.execute(query, (motherId,))

    notifications_list = []

    for (status, ntype, date) in cursor:
        notifications_list.append({
            'date': date,
            'seenByMother': status == 2,
            'title': notification_title_map(ntype),
            'description': notification_description_map(ntype)
        })

    cursor.close()
    db.close()

    return jsonify({
        "notifications": notifications_list
    })


@app.route('/inbox', methods=['GET'])
def get_inbox():
    db = mysql.connector.connect(user='EPICS', password='EPICS2017', database= 'lactor', host= '166.62.75.128', port=3306)

    authToken = request.args.get('authToken')
    # TODO actual user verification
    if authToken != 'AXNTHAUONTUOAENHTOEUA':
        abort(403)
    reciever_id = 71  # FIXME

    cursor = db.cursor()
    cursor.execute("""
        SELECT message, DATE_FORMAT(messageDate, '%b %e, %Y') as date, senderId, name
        FROM Inbox
        INNER JOIN MotherInfo ON MotherInfo.mid = Inbox.senderId
        WHERE recipientId = %s
    """, (reciever_id,))

    received = []
    for message, date, senderId, name in cursor:
        received.append({
            'message': message,
            'messageDate': date,
            'senderId': senderId,
            'senderName': name
        })

    cursor.close()
    cursor = db.cursor()
    cursor.execute("""
            SELECT message, DATE_FORMAT(messageDate, '%b %e, %Y') as date, recipientId, name
            FROM Inbox
            INNER JOIN MotherInfo ON MotherInfo.mid = Inbox.recipientId
            WHERE senderId = %s
        """, (reciever_id,))

    sent = []
    for message, date, recipientId, name in cursor:
        sent.append({
            'message': message,
            'messageDate': date,
            'receiverId': recipientId,
            'receiverName': name
        })

    cursor.close()
    db.close()

    return jsonify({
        "received": received,
        "sent": sent
    })


@app.route('/inbox', methods=['POST'])
def post_inbox():
    db = mysql.connector.connect(user='epicsadm', password='EPICS2017', database= 'lactor', host= '166.62.75.128', port=3306)

    print("Hi1")
    sender_id = 71 # FIXME
    print("Hi2")
    print(request.data)
    reciever_id = request.json['recieverId']
    print("Hi3")
    message = request.json['message']
    print("Hi4")

    cursor = db.cursor()
    cursor.execute("""
        INSERT INTO Inbox(message, messageDate, senderId, recipientId, metadata)
        VALUES(%s, NOW(), %s, %s, 25)
    """, (message, sender_id, reciever_id))

    cursor.close()
    db.close()

    return jsonify({
        'ok': True
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
