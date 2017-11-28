def age_map(num):
    return {
        1: '<20',
        2: '20-29',
        3: '30-39',
        4: '40 or more'
    }[num]

def ethnicity_map(num):
    return {
        1: 'Hispanic of Latino',
        2: 'NON Hispanic of Lation'

    }[num]

def race_map(num):
    return {
        1: 'Native Hawaiian or Pacific Islander',
        2: 'Asian',
        3: 'Black of African American',
        4: 'American Indian/Alaskan Native',
        5: 'White',
        6: 'One or more race'

    }[num]

def education_map(num):
    return {
        1: 'Less than high school',
        2: 'High school/GED',
        3: 'Some college',
        4: 'Associate College',
        5: 'BA or BS degree',
        6: 'Masters Degree',
        7: 'Doctoral Degree',
        8: 'Professional Degree'
    }[num]

def house_income_map(num):
    return {
        1: 'Less than $10,000',
        2: '$10,000 to < $24,999',
        3: '$25,000 to $49,999',
        4: '$50,000 or more'

    }[num]

def occupation_map(num):
    return {
        1: 'Homemaker',
        2: 'Professional',
        3: None,
        4: None

    }[num]

def residence_map(num):
    return {
        1: 'Rural',
        2: 'Urban',
        3: 'Apartment/Rental',
        4: 'Owned'

    }[num]

def parity_map(num):
    return None
    '''
    return {
        1: 'none',
        2: 'none',
        3: 'none',
        4: 'none'
    }[num]
    '''

def poh_map(num):
    return None
    '''
    return {
        
        1111: 'none',
        1112: 'none',
        1121: 'none',
        1211: 'none',
        2111: 'none',
        2221: 'none',
        2212: 'none',
        1122: 'none',
        1222: 'none',
        2222: 'none',
        1221: 'none',
        2211: 'none',
        2121: 'none',
        1212: 'none',
        2112: 'none',
        2122: 'none'
    }[num]
    '''

def mhdp_map(num):
    return {
        1111111: 'none',
        1111112: 'Other',
        1111121: 'Gestational Diabetes',
        1111211: 'PROM',
        1112111: 'Lack or late prenatal care ',
        1121111: 'Toxemia of Pregnancy',
        1211111: 'Bleeding during Pregnancy',
        2111111: 'Low Maternal Weight < 50 kg',
        1111122: 'Gestational Diabetes and Other',
        1111222: 'PROM, Gestational Diabetes and Other',
        1112222: 'Lack or late prenatal care, PROM, Gestational Diabetes and Other',
        1122222: 'Toxemia of Pregnancy, Lack or late prenatal care, PROM, Gestational Diabetes and Other',
        1222222: 'Bleeding during Pregnancy, Toxemia of Pregnancy, Lack or late prenatal care, PROM, Gestational Diabetes and Other',
        2222222: 'Low maternal weight <50kg, Bleeding during Pregnancy, Toxemia of Pregnancy, Lack or late prenatal care, PROM, Gestational Diabetes and Other',
        2211111: 'Low maternal weight <50kg, Bleeding during Pregnancy',
        2221111: 'Low maternal weight <50kg, Bleeding during Pregnancy, Toxemia of Pregnancy',
        2222111: 'Low maternal weight <50kg, Bleeding during Pregnancy, Toxemia of Pregnancy, Lack or late prenatal care',
        2222211: 'Low maternal weight <50kg, Bleeding during Pregnancy, Toxemia of Pregnancy, Lack or late prenatal care, PROM',
        2222221: 'Low maternal weight <50kg, Bleeding during Pregnancy, Toxemia of Pregnancy, Lack or late prenatal care, PROM, Gestational Diabetes',
        1112211: 'Lack or late prenatal care, PROM',
        1122111: 'Toxemia of Pregnancy, Lack or late prenatal care',
        1222111: 'Bleeding during Pregnancy, Toxemia of Pregnancy, Lack or late prenatal care',
        1111221: 'PROM, Gestational Diabetes',
        1221111: 'Bleeding during Pregnancy, Toxemia of Pregnancy',
        2111112: 'Low maternal weight <50kg, and Other',
        2111122: 'Low maternal weight <50kg, Gestational Diabetes, and Other',
        2111222: 'Low maternal weight <50kg, PROM, Gestational Diabetes, and Other',
        2112222: 'Low maternal weight <50kg, Lack or late prenatal care, PROM, Gestational Diabetes, and Other',
        2122222: 'Low maternal weight <50kg, Toxemia of Pregnancy, Lack or late prenatal care, PROM, Gestational Diabetes, and Other',
        2121212: 'Low maternal weight <50kg, Toxemia of Pregancy, PROM, and Other',
        2121211: 'Low maternal weight <50kg, Toxemia of Pregancy, and PROM',
        2121111: 'Low maternal weight <50kg and Toxemia of Pregnancy',
        2121121: 'Low maternal weight <50kg, Toxemia of Pregnancy, and Gestational Diabetes',
        2122211: 'Low maternal weight <50kg, Toxemia of Pregnancy, Lack or late Prenatal care, and PROM',
        2121122: 'Low maternal weight <50kg, Toxemia of Preganacy, Gestational Diabetes',
        2112211: 'Low maternal weight <50kg, Lack or Late prenatal care, PROM',
        2221121: 'Low maternal weight <50kg, Bleeding during Pregnancy, Toxemia of Pregnancy, Gestational Diabetes',
        2222112: 'Low maternal weight <50kg, Bleeding during Pregnancy, Toxemia of Pregnancy, Lack or late prenatal care and Other',
        2111212: 'Low material weight <50kg, PROM, and Other',
        2211221: 'Low maternal weight <50kg, Bleeding During pregnancy, PROM, Gestational Diabetes',
        2212121: 'Low maternal weight <50kg, Bleeding During pregancy, Lack or prenatal care, and Gestational Diabetes',
        2221212: 'Low maternal weight <50kg, Bleeding during Pregnancy, Toxemia of Pregnancy, PROM, and Other',
        2211122: 'Low maternal weight <50kg, Bleeding during pregnancy, Gestational Diabetes, and Other',
        2221122: 'Low maternal weight <50kg, Bleeding during Pregnancy, Toxemia of Pregnancy, Gestational Diabetes, and Other',
        2112212: 'Low maternal weight <50kg, Lack of late prenatal care, PROM, and Other',
        2222122: 'Low maternal weight <50kg, Bleeding during Pregnancy, Toxemia of Pregnancy, Lack or late prenatal care, Gestational Diabetes, and Other',
        2111221: 'Low maternal weight <50kg, PROM, and Gestational Diabetes',
        2112122: 'Low maternal weight <50kg, Lack or late prenatal care, Gestational Diabetes, and Other',
        2121221: 'Low maternal weight <50kg, Toxemia of Pregnancy, PROM, Gestational Diabetes',
        2121112: 'Low maternal weight <50kg, Toxemia of Pregnancy, and Other',
        2211222: 'Low maternal weight <50kg, Bleeding during pregnancy, PROM, Gestational Diabetes, and Other',
        1211221: 'Bleeding during pregnancy, PROM, and Gestational Diabetes',
        1211121: 'Bleeding during pregnancy, Gestational Diabetes',
        1212211: 'Bleeding during pregnancy, Lack or late prenatal care, PROM',
        1212112: 'Bleeding during pregnancy, Lack or late prenatal care, and Other',
        1222211: 'Bleeding during pregnancy, Toxemia of Pregnancy, Lack or late prenatal care, and PROM',
        1122112: 'Toxemia of Pregnancy, Lack or late prenatal care, and Other',
        1121211: 'Toxemia of Pregnancy, PROM',
        1212121: 'Bleeding during pregnancy, Lack or late prenatal care, Gestational Diabetes',
        1212111: 'Bleeding during pregnancy, Lack or late prenatal care',
        1212122: 'Bleeding during pregnancy, Lack or late prenatal care, Gestational Diabetes and Other',
        1212222: 'Bleeding during pregnancy, Lack or late prenatal care, PROM, Gestational Diabetes and Other',
        1211211: 'Bleeding during pregnancy, and Gestational Diabetes and Other'

    }[num]

def method_of_delivery_map(num):
    return {
        1: 'Vaginal',
        2: 'Vaginal with Assistance',
        3: 'Breech',
        4: 'Section'

    }[num]

def pbe_map(num):
    return {
        1: "<3 months",
        2: "3-6 months",
        3: "7-12 months",
        4: "> 1 year",
        5: "No past breastfeeding experience"

    }[num]
