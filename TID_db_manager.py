from sqlite3 import *
from catid_generator import *
from datetime import *

fully_student = 1
just_got_in_by_tgshchcka = 2

class_id_map = {
"id1110": ["Детское", "Интелектуальное", "Английский язык"],
"id1120": ["Детское", "Интелектуальное", "Логопед"],
"id1130": ["Детское", "Интелектуальное", "Подготовка к школе"],
"id1210": ["Детское", "Спортивное", "Хореография"],
"id1310": ["Детское", "Художественное", "Развитие"],
"id2110": ["Подростковое", "Интелектуальное", "Подготовка к школе"],
"id2120": ["Подростковое", "Интелектуальное", "Ментальная алгебра"],
"id2130": ["Подростковое", "Интелектуальное", "Подготовка к ОГЭ/ЕГЭ/ВПР"],
"id2140": ["Подростковое", "Интелектуальное", "Английский язык"],
"id2150": ["Подростковое", "Интелектуальное", "Армянский язык"],
"id2160": ["Подростковое", "Интелектуальное", "Испанский язык"],
"id2210": ["Подростковое", "Спортивное", "Хореография"],
"id2220": ["Подростковое", "Спортивное", "Хип-Хоп"],
"id2230": ["Подростковое", "Спортивное", "Карате"],
"id2310": ["Подростковое", "Художественное", "Рисование"],
"id2320": ["Подростковое", "Художественное", "Актерское мастерство"],
"id2330": ["Подростковое", "Художественное", "Исскуствоведение"],
"id2340": ["Подростковое", "Художественное", "Хореография"],
"id3110": ["Взрослое", "Интелектуальное", "Английский язык"],
"id3120": ["Взрослое", "Интелектуальное", "Армянский язык"],
"id3130": ["Взрослое", "Интелектуальное", "Испанский язык"],
"id3140": ["Взрослое", "Интелектуальное", "Французский язык"],
"id3210": ["Взрослое", "Спортивное", "Йога"],
"id3220": ["Взрослое", "Спортивное", "Фитнес"],
"id3310": ["Взрослое", "Художественное", "Ораторское искуство"],
"id3320": ["Взрослое", "Художественное", "Актерское мастерство"],
"id3330": ["Взрослое", "Художественное", "Рисование"],
"id3340": ["Взрослое", "Художественное", "Хореография"]
}


def getPersonInfo(TID):
    data_from_db = getPersonInfoFromcatiddb(TID, 0)
    amount_of_returned_lists =  data_from_db["amount_of_returned_lists"]

    current_month = datetime.now().strftime("%m.%Y")
    result_messages = []

    if amount_of_returned_lists == 1:
        try:
            classID = ', '.join(class_id_map.get(data_from_db["classID"]))
        except TypeError as e:
            classID = "Вы еще не записались на полноценные занятия :/"
            print(e)
            print("Скорее всего class_id в db = None")
        print(classID)
        result_messages.append(f"""
Ваш статус на {current_month}:
    \tИмя: {data_from_db["name"]}
    \tНапрвление: {classID}
    \tОплаченных уроков: {data_from_db["paid_lessons"]}
    \tропущенных уроков: {data_from_db["missed_lessons"]}
""")
    else:
        for i in range(amount_of_returned_lists):
            data_from_db = getPersonInfoFromcatiddb(TID, i)
            try:
                classID = ', '.join(class_id_map.get(data_from_db["classID"]))
            except TypeError as e:
                classID = "Вы еще не записались на полноценные занятия :/"
                print(e)
                print("Скорее всего class_id в db = None")
            reply_message = f"""
\tИмя: {data_from_db["name"]}
\tНапрвление: {classID}
\tОплаченных уроков: {data_from_db["paid_lessons"]}
\tПропущенных уроков: {data_from_db["missed_lessons"]}
"""
            result_messages.append(reply_message)

    result_text = "📰Личный кабинет📰\n\nВаш статус на 02.2024:\n"
    result_text += result_messages[0]

    for message in result_messages[1:]:
        result_text += "\n" + message

    return result_text


def CreteMonthlyTable():
    with connect("MAIN_db.db") as con:
        cur = con.cursor()

        cur.execute(f"""
        CREATE TABLE IF NOT EXISTS "catid_db_for_{datetime.now().strftime("%m%Y")}" (
	        "cat_id"	INTEGER NOT NULL UNIQUE,
	        "class_id"	TEXT,
            "TID"	INTEGER,                
	        "name"	TEXT,
	        "paid_lessons"	INTEGER DEFAULT 0,
	        "missed_lessons"	INTEGER DEFAULT 0,
	        "status"	INTEGER,
	        PRIMARY KEY("cat_id")
        )""")

        cur.execute(f"""SELECT * FROM catid_db_for_{(datetime.now().replace(day=1) - timedelta(days=1)).strftime("%m%Y")}
                    WHERE status = {int(fully_student)}
        """)
        data = cur.fetchall()
        cur.execute(f"""INSERT INTO catid_db_for_{datetime.now().strftime("%m%Y")} (cat_id, class_id, TID, name, paid_lessons, missed_lessons, status)
                    SELECT cat_id, class_id, TID, name, paid_lessons, missed_lessons, status 
                    FROM catid_db_for_{(datetime.now().replace(day=1) - timedelta(days=1)).strftime("%m%Y")}
                    WHERE status = {int(fully_student)}
        """)

#    con.execute("""CREATE TABLE IF NOT EXISTS tid_db (
#                tid INTEGER,
#                phone_number INTEGER,
#                full_name TEXT
#                cat_id TEXT,
#                cat_id1 TEXT,
#                cat_id2 TEXT,
#                cat_id3 TEXT,
#                cat_id4 TEXT,
#                cat_id5 TEXT,
#                cat_id6 TEXT,
#                cat_id7 TEXT,
#                cat_id8 TEXT,
#                cat_id9 TEXT,
#                cat_id10 TEXT,
#                cat_id11 TEXT,
#                cat_id12 TEXT,
#                cat_id13 TEXT,
#                cat_id14 TEXT,
#                cat_id15 TEXT,
#                cat_id16 TEXT,
#                cat_id17 TEXT,
#                cat_id18 TEXT,
#                cat_id19 TEXT,
#                cat_id20 TEXT,
#                cat_id21 TEXT,
#                cat_id22 TEXT,
#                cat_id23 TEXT,
#                cat_id24 TEXT,
#                cat_id25 TEXT,
#                cat_id26 TEXT,
#                cat_id27 TEXT,
#                cat_id28 TEXT,
#                cat_id29 TEXT,
#                cat_id30 TEXT,
#                cat_id31 TEXT,
#                cat_id32 TEXT,
#                cat_id33 TEXT,
#                cat_id34 TEXT,
#                cat_id35 TEXT,
#                cat_id36 TEXT,
#                cat_id37 TEXT,
#                cat_id38 TEXT,
#                cat_id39 TEXT,
#                cat_id40 TEXT,
#                cat_id41 TEXT,
#                cat_id42 TEXT,
#                cat_id43 TEXT,
#                cat_id44 TEXT,
#                cat_id45 TEXT,
#                cat_id46 TEXT,
#                cat_id47 TEXT,
#                cat_id48 TEXT,
#                cat_id49 TEXT,
#                cat_id50 TEXT,
#                cat_id51 TEXT,
#                cat_id52 TEXT,
#                cat_id53 TEXT,
#                cat_id54 TEXT,
#                cat_id55 TEXT,
#                cat_id56 TEXT,
#                cat_id57 TEXT,
#                cat_id58 TEXT,
#                cat_id59 TEXT,
#                cat_id60 TEXT,
#                cat_id61 TEXT,
#                cat_id62 TEXT,
#                cat_id63 TEXT,
#                cat_id64 TEXT
#                )""")