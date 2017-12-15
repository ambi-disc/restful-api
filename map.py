# Mother model mapped values
def age_map(num):
    return {
        1: '<20',
        2: '20-29',
        3: '30-39',
        4: '40 or more'
    }[num]


def ethnicity_map(num):
    return None


def race_map(num):
    return None


def education_map(num):
    return None


def house_income_map(num):
    return None


def occupation_map(num):
    return {
        1: 'Homemaker',
        2: 'Professional',
        3: None,
        4: None

    }[num]


def residence_map(num):
    return None


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


def breast_feeding_duration_map(num):
    return {
        1: "1-2 minutes",
        2: "3-4 minutes",
        3: "5-10 minutes",
        4: "11-15 minutes",
        5: "> 15 minutes"
    }[num]


def pumping_method_map(num):
    return {
        1: "Hand Pump",
        2: "Manual Pump",
        3: "Double Electric Pump",
        4: "Not applicable"
    }[num]


def infant_state_map(num):
    return {
        1: "Difficult to awake",
        2: "Drowsy",
        3: "Quiet and Alert",
        4: "Active alert",
        5: "Crying"
    }[num]


def maternal_problems_map(num):
    return {
        1: "Breast tissue is soft/no milk coming in",
        2: "Sore nipple",
        3: "Flat/inverted nipple",
        4: "Engorgement",
        5: "Mastitis",
        6: "No problem"
    }[num]


def latching_map(num):
    return{
        1: "Not at all",
        2: "Slipping of the breast",
        3: "Latch correctly",
        4: "Latch with nipple shield"
    }[num]


def side_map(num):
    return{
        1: "left",
        2: "right",
        3: "both"
    }[num]


def pumping_amount_map(num):
    return{
        0: "0 ounce",
        1: "1 ounce",
        2: "2 ounce",
        3: "3 ounce",
        4: "4 ounce",
        5: "5 ounce",
        6: "6 ounce",
        7: "7 ounce",
        8: "8 ounce",
        9: "9 ounce",
        10: "10 ounce",
        11: "> 10 ounces"
    }[num]


def suptype_map(num):
    return {
        1: "Expressed milk",
        2: "Pasteurized human milk",
        3: "Formula"
    }[num]


def supmethod_map(num):
    return{
        1: "Bottle",
        2: "Cup",
        3: "Supplemental Set",
        4: "Spoon"
     }[num]


def total_amount_map(num):
    return{
        1: "1 ounce",
        2: "2 ounce",
        3: "3 ounce",
        4: "4 ounce",
        5: "5 ounce",
        6: "6 ounce",
        7: "7 ounce",
        8: "8 ounce",
        9: "9 ounce",
        10: "10 ounce",
        11: "> 10 ounces"

    }[num]


def total_amount_today(num):
    return{
        1: "1",
        2: "2",
        3: "3",
        4: "4",
        5: "5",
        6: "> 5"
    }[num]


def urine_color_map(num):
    return{
        0: "None",
        1: "Amber Yellow",
        2: "Dark Yellow"
    }[num]


def urine_saturation_map(num):
    return{
        0: "None",
        1: "Not wet at all",
        2: "Slightly wet",
        3: "Moderately wet",
        4: "Heavily wet"
    }[num]


def stool_color_map(num):
    return{
        0: "None",
        1: "Black/tarry meconium",
        2: "Black/Green",
        3: "Yellow"
    }[num]


def stool_consistency_map(num):
    return{
        0: "None",
        1: "Loose and steady",
        2: "Formed",
        3: "Watery"
    }[num]


def number_of_diapers_map(num):
    if num is None:
        return "None"
    return{
        0:"None",
        1: "1",
        2: "2",
        3: "3",
        4: "4",
        5: "5",
        6: "6",
        7: "> 6"
    }[num]


def type_map(num):
    return {
        1: "Jaundice",
        2: "Decrease body tempature",
        3: "Decrease in blood glucose",
        4: "Difficult or troubling breathing",
        5: "Infection",
        6: "Dehydration",
        7: "Weight loss"
    }[num]


def notification_title_map(num):
    return {
        1: "Problem: Latching",
        2: "Problem: Sleepy",
        3: "Problem: Jaundice",
        4: "Problem: Engorgement",
        5: "Problem: Sore nipple",
        6: "Problem: Insufficient Breastfeeding",
        7: "Problem: Nipple Shield",
        8: "Great Job!",
        9: "Great Job!",
        10: "Great Job!"
    }[num]


def notification_description_map(num):
    return {
        1: """1.Skin-to-skin contact (remove all clothing from the baby -except diaper-,
place the baby on your bare chest. The baby will crawl to the breast and latch).
2.Pump every 3 hours if baby does not latch.
3.Contact local lactation consultant for help.""",
        2: """1. Skin-to-skin contact (remove all clothing from baby except diaper,
place the baby on your bare chest. The baby will crawl to the
breast and latch).
2. Pump after each feeding if baby did not get enough.
3. Contact the primary care provider if continues (baby should
not go for more than 5 hours without feeding for the first
5 weeks).""",
        3: """1. Contact your primary care provider.
2. Breastfeed the baby more frequently.
3. Make sure that the baby is latching correctly.
4. Report any decrease in wet and dirty diapers.""",
        4: """1.Manually express or pump enough to soften your
breast before putting your baby to the breast.
2. Breastfeed your baby more often.
3. Make sure that your baby is latching on and feeding well.
4. Apply cold packs to the breasts after feeding to help
reduce swelling, warmth, and pain.""",
        5: """1. Make sure that your baby is latched on well, so
that baby opens mouth wide.
2. Continue breast-feeding even if nipples are sore or
cracked. Try to feed the baby from the less painful
breast first.
3. Detach your baby carefully off of the breast
 when feeding is finished.
4. Breastfeed often (Every 1&frac12; to 3 hours for 8 to 12
feedings a day) to reduce engorgement.
5. Vary nursing positions, so the baby's positions on the
breast are changed.
6. Express colostrum or milk onto your nipples before and
after feedings.
7. After feeding, allow the nipples to air dry.""",
        6: """1. Ideal breastfeeding during the first month is
from 8 to 12 times per day. Feeding your baby less
than 6 times per day will decrease your milk supply.
2. Try to breastfeed your baby as much as you can and avoid
any supplementation.
3. Contact your lactation consultant if you have any question.""",
        7: """1. A nipple shield should in general be considered a short-term solution
and should be used under the guidance of a Lactation Consultant.
2. Work with you lactation consultant to solve the problem behind
using a nipple shield.
3. Make sure that your baby is getting enough milk and gaining weight.""",
        8: "Effective breastfeeding is from 8 to 12 times per day.",
        9: "Effective breastfeeding is from 8 to 12 times per day.",
        10: "Effective breastfeeding is from 8 to 12 times per day."
    }[num]
