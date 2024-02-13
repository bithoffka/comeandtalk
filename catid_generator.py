from sqlite3 import *
from threading import *
from gspread import *
from datetime import *

# TECHNICAL HUETA START
# admin = service_account(filename="/Users/alex/vsc/credentials.json")
# worksh = admin.open("main_db").sheet1
# TECHNICAL HUETA END

id1110 = ["Детское", "Интелектуальное", "Английский язык"]
id1120 = ["Детское", "Интелектуальное", "Логопед"]
id1130 = ["Детское", "Интелектуальное", "Подготовка к школе"]
id1210 = ["Детское", "Спортивное", "Хореография"]
id1310 = ["Детское", "Художественное", "Развитие"]
id2110 = ["Подростковое", "Интелектуальное", "Подготовка к школе"]
id2120 = ["Подростковое", "Интелектуальное", "Ментальная алгебра"]
id2130 = ["Подростковое", "Интелектуальное", "Подготовка к ОГЭ/ЕГЭ/ВПР"]
id2140 = ["Подростковое", "Интелектуальное", "Английский язык"]
id2150 = ["Подростковое", "Интелектуальное", "Армянский язык"]
id2160 = ["Подростковое", "Интелектуальное", "Испанский язык"]
id2210 = ["Подростковое", "Спортивное", "Хореография"]
id2220 = ["Подростковое", "Спортивное", "Хип-Хоп"]
id2230 = ["Подростковое", "Спортивное", "Карате"]
id2310 = ["Подростковое", "Художественное", "Рисование"]
id2320 = ["Подростковое", "Художественное", "Актерское мастерство"]
id2330 = ["Подростковое", "Художественное", "Исскуствоведение"]
id2340 = ["Подростковое", "Художественное", "Хореография"]
id3110 = ["Взрослое", "Интелектуальное", "Английский язык"]
id3120 = ["Взрослое", "Интелектуальное", "Армянский язык"]
id3130 = ["Взрослое", "Интелектуальное", "Испанский язык"]
id3140 = ["Взрослое", "Интелектуальное", "Французский язык"]
id3210 = ["Взрослое", "Спортивное", "Йога"]
id3220 = ["Взрослое", "Спортивное", "Фитнес"]
id3310 = ["Взрослое", "Художественное", "Ораторское искуство"]
id3320 = ["Взрослое", "Художественное", "Актерское мастерство"]
id3330 = ["Взрослое", "Художественное", "Рисование"]
id3340 = ["Взрослое", "Художественное", "Хореография"]

def Generate_class_id(data_dictionary):
    class_type = data_dictionary["class_type"]
    age_group = data_dictionary["age_group"]
    direction = data_dictionary["direction"]

    catid = None
    
    if age_group == "👶Дети (4-7 лет)":
        if direction == "🎓Интеллектуальная":
            if class_type == "🇬🇧Английский язык":
                catid = {"id": "id1110", "full_id": id1110}
            elif class_type == "🔠Логопед":
                catid = {"id": "id1120", "full_id": id1120}
            elif class_type == "📚Подготовка к школе":
                catid = {"id": "id1130", "full_id": id1130}
        elif direction == "🥋Спортивная":
            if class_type == "💃Хореография":
                catid = {"id": "id1210", "full_id": id1210}
        elif direction == "🎨Творческая":
            if class_type == "🧐Развитие":
                catid = {"id": "id1310", "full_id": id1310}
    if age_group == "👱Подростки (7-18 лет)":
        if direction == "🎓Интеллектуальная":
            if class_type == "📚Подготовка к школе":
                catid = {"id": "id2110", "full_id": id2110}
            elif class_type == "🔢Ментальная алгебра":
                catid = {"id": "id2120", "full_id": id2120}
            elif class_type == "📖Подготовка к ОГЭ/ЕГЭ/ВПР":
                catid = {"id": "id2130", "full_id": id2130}
            elif class_type == "🇬🇧Английский язык":
                catid = {"id": "id2140", "full_id": id2140}
            elif class_type == "🇦🇲Армянский язык":
                catid = {"id": "id2150", "full_id": id2150}
            elif class_type == "🇪🇸Испанский язык":
                catid = {"id": "id2160", "full_id": id2160}
        if direction == "🥋Спортивная":
            if class_type == "💃Хореография":
                catid = {"id": "id2210", "full_id": id2210}
            elif class_type == "🔊Хип-Хоп":
                catid = {"id": "id2220", "full_id": id2220}
            elif class_type == "🥋Карате":
                catid = {"id": "id2230", "full_id": id2230}
        if direction == "🎨Творческая":
            if class_type == "🎨Рисование":
                catid = {"id": "id2310", "full_id": id2310}
            elif class_type == "🎭Актерское мастерство":
                catid = {"id": "id2320", "full_id": id2320}
            elif class_type == "🖼Исскуствоведение":
                catid = {"id": "id2330", "full_id": id2330}
            elif class_type == "💃Хореография":
                catid = {"id": "id2340", "full_id": id2340}
    if age_group == "🧔‍♂️Взрослые (18-81 лет)":
        if direction == "🎓Интеллектуальная":
            if class_type == "🇬🇧Английский язык":
                catid = {"id": "id3110", "full_id": id3110}
            elif class_type == "🇦🇲Армянский язык":
                catid = {"id": "id3120", "full_id": id3120}
            elif class_type == "🇪🇸Испанский язык":
                catid = {"id": "id3130", "full_id": id3130}
            elif class_type == "🇫🇷Французский язык":
                catid = {"id": "id3140", "full_id": id3140}
        if direction == "🥋Спортивная":
            if class_type == "🧘Йога":
                catid = {"id": "id3210", "full_id": id3210}
            elif class_type == "💪Фитнес":
                catid = {"id": "id3220", "full_id": id3220}
        if direction == "🎨Творческая":
            if class_type == "🎤Ораторское искуство":
                catid = {"id": "id3310", "full_id": id3310}
            elif class_type == "🎭Актерское мастерство":
                catid = {"id": "id3320", "full_id": id3320}
            elif class_type == "🖼Рисование":
                catid = {"id": "id3330", "full_id": id3330}
            elif class_type == "💃Хореография":
                catid = {"id": "id3340", "full_id": id3340}

    return catid


def SetPaidLessonsAmount(cat_id, paid_lessons):
    with connect("MAIN_db.db") as con:
        cur = con.cursor()
#       cur.execute(''' CREATE TABLE IF NOT EXISTS "catid_db" (
#	    "cat_id"	INTEGER NOT NULL,
#	    "class_id"	TEXT,
#	    "paid_lessons"	INTEGER,
#	    "TID"	INTEGER,
#	    PRIMARY KEY("cat_id")
#        );''')
        cur.execute(f'''UPDATE catid_db 
        SET paid_lessons = {paid_lessons}
        WHERE cat_id = {cat_id}
        ''')
        
        data1 = cur.execute("SELECT * FROM catid_db").fetchall()
        print(data1)


def EstablishNewPupil(data_dictionary):
    with connect("MAIN_db.db") as con:
        cur = con.cursor()
        try:
            catID = Generate_class_id(data_dictionary) 
            cur.execute(f'''INSERT INTO catid_db_for_{datetime.now().strftime("%m%Y")} (name, TID, class_id, status)
                           VALUES (?, ?, ?, 2)''',
                        (data_dictionary["TNAME"], data_dictionary["TID"], catID["id"]))
        except OperationalError or ProgrammingError as e:
            print("An error occurred:", e)


def getPersonInfoFromcatiddb(TID, index):
    with connect("MAIN_db.db") as con:
        cur = con.cursor()

        catID_list = []
        classID_list = []
        missed_lessons_list = []
        paid_lessons_list = []
        name_list = []

        cur.execute("""SELECT cat_id, class_id, missed_lessons, paid_lessons, name 
        FROM catid_db
        WHERE TID = ?
        """, (str(TID),))

        rows = cur.fetchall()

    for row in rows:
        catID_list.append(row[0])
        classID_list.append(row[1])
        missed_lessons_list.append(row[2])
        paid_lessons_list.append(row[3])
        name_list.append(row[4])

    len_of_lists = len(catID_list)

    try:
        return {"catID": catID_list[index], "classID": classID_list[index], "missed_lessons": missed_lessons_list[index], "paid_lessons": paid_lessons_list[index] ,"name": name_list[index], "amount_of_returned_lists": len_of_lists}
    except IndexError:
        return "Index out of range for the given TID."


#print(getPersonInfoFromcatiddb(1440788864, 0))

#def getPersonInfoFromcatiddb(TID, index):
#    with connect("MAIN_db.db") as con:
#        cur = con.cursor()
#        catID_list = []
#        classID_list = []
#        catID = cur.execute("""SELECT cat_id 
#            FROM catid_db
#            WHERE TID = ?
#            """, (str(TID),))
#        for i in range(0, len(catID)):
#            catID = cur.execute("""SELECT cat_id 
#            FROM catid_db
#            WHERE TID = ?
#            """, (str(TID),))
#            catID = cur.fetchall()
#            catID = catID[i]
#            catID_list.append(catID)
#
#            classID = cur.execute("""SELECT class_id 
#            FROM catid_db
#            WHERE TID = ?
#            """, (str(TID),))
#            classID = cur.fetchall()
#            classID = classID[i]
#            classID_list.append(classID)
#        try:
#            return {"catID": catID_list[index], "classID": classID_list[index]}
#        except:
#            pass



#def CopyTableIntoGoogle():
#    with connect("MAIN_db.db") as con:
#        cur = con.cursor()
#        row_count = 1
#        col_count = 1
#        my_num_inlist = cur.execute(f'''SELECT {col_count} from catid_db 
#                            WHERE rowid = "{str(row_count)}" ''')
#        while True:
#            if my_num_inlist != None:
#                worksh.update_cell(row_count, col_count, 1)
#                col_count =+ 1
#            else:
#                row_count =+ 1
#                col_count = 1
#
#CopyTableIntoGoogle()

    
        


#cur.execute(''' CREATE TABLE "catid_db" (
#	"cat_id"	INTEGER NOT NULL,
#	"class_id"	TEXT,
#	"paid_lessons"	INTEGER,
#	"TID"	INTEGER,
#	PRIMARY KEY("cat_id")
#);''')
#con.commit()
#
#cur.execute('''INSERT INTO catid_db (class_id, paid_lessons)
#VALUES ('id111', 1)
#''')
#cur.execute("""UPDATE catid_db
#SET class_id = 'id212', paid_lessons = '5', cat_id = 2
#WHERE cat_id = 1;                 
#""")


#def getMissedClassesAmount():
#    for i in range(2, 20):
#        CATIDdt = worksh.cell(i, 2).value
#        NAMEval = worksh.cell(i, 1).value
#        if CATIDdt:
#            try:
#                with connect("MAIN_db.db") as con:
#                    cur = con.cursor()
#                    cur.execute(f'''INSERT INTO catid_db (cat_id, name) 
#                                 VALUES (?, ?);''', (int(CATIDdt), NAMEval))
#            except IntegrityError:
#                i += 1
#
#getMissedClassesAmount()