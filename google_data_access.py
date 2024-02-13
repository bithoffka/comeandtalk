import gspread

# TECHNICAL HUETA START
admin = gspread.service_account(filename="/Users/alex/vsc/credentials.json")
wsh = admin.open("sussy").sheet1
# TECHNICAL HUETA END

def sign_in_user(data_dictionary):
    user_class_id = None
    
#    if data_dictionary["age_group"] == "👶Дети (4-7 лет)":
#        if data_dictionary["direction"] == "🎓Интеллектуальная":
#            if data_dictionary["class_type"] == "🇬🇧Английский язык":
#                user_class_id = id1110
#            elif data_dictionary["class_type"] == "🔠Логопед":
#                user_class_id = id1120
#            elif data_dictionary["class_type"] == "📚Подготовка к школе":
#                user_class_id = id1130
#        elif data_dictionary["direction"] == "🥋Спортивная":
#            if data_dictionary["class_type"] == "💃Хореография":
#                user_class_id = id1210
#        elif data_dictionary["direction"] == "🎨Творческая":
#            if data_dictionary["class_type"] == "🧐Развитие":
#                user_class_id = id1310
#    if data_dictionary["age_group"] == "👱Подростки (7-18 лет)":
#        if data_dictionary["direction"] == "🎓Интеллектуальная":
#            if data_dictionary["class_type"] == "📚Подготовка к школе":
#                user_class_id = id2110
#            elif data_dictionary["class_type"] == "🔢Ментальная алгебра":
#                user_class_id = id2120
#            elif data_dictionary["class_type"] == "📖Подготовка к ОГЭ/ЕГЭ/ВПР":
#                user_class_id = id2130
#            elif data_dictionary["class_type"] == "🇬🇧Английский язык":
#                user_class_id = id2140
#            elif data_dictionary["class_type"] == "🇦🇲Армянский язык":
#                user_class_id = id2150
#            elif data_dictionary["class_type"] == "🇪🇸Испанский язык":
#                user_class_id = id2160
#        if data_dictionary["direction"] == "🥋Спортивная":
#            if data_dictionary["class_type"] == "💃Хореография":
#                user_class_id = id2210
#            elif data_dictionary["class_type"] == "🔊Хип-Хоп":
#                user_class_id = id2220
#            elif data_dictionary["class_type"] == "🥋Карате":
#                user_class_id = id2230
#        if data_dictionary["direction"] == "🎨Творческая":
#            if data_dictionary["class_type"] == "🎨Рисование":
#                user_class_id = id2310
#            elif data_dictionary["class_type"] == "🎭Актерское мастерство":
#                user_class_id = id2320
#            elif data_dictionary["class_type"] == "🖼Исскуствоведение":
#                user_class_id = id2330
#            elif data_dictionary["class_type"] == "💃Хореография":
#                user_class_id = id2340
#    if data_dictionary["age_group"] == "🧔‍♂️Взрослые (18-81 лет)":
#        if data_dictionary["direction"] == "🎓Интеллектуальная":
#            if data_dictionary["class_type"] == "🇬🇧Английский язык":
#                user_class_id = id3110
#            elif data_dictionary["class_type"] == "🇦🇲Армянский язык":
#                user_class_id = id3120
#            elif data_dictionary["class_type"] == "🇪🇸Испанский язык":
#                user_class_id = id3130
#            elif data_dictionary["class_type"] == "🇫🇷Французский язык":
#                user_class_id = id3140
#        if data_dictionary["direction"] == "🥋Спортивная":
#            if data_dictionary["class_type"] == "🧘Йога":
#                user_class_id = id3210
#            elif data_dictionary["class_type"] == "💪Фитнес":
#                user_class_id = id3220
#        if data_dictionary["direction"] == "🎨Творческая":
#            if data_dictionary["class_type"] == "🎤Ораторское искуство":
#                user_class_id = id3310
#            elif data_dictionary["class_type"] == "🎭Актерское мастерство":
#                user_class_id = id3320
#            elif data_dictionary["class_type"] == "🖼Рисование":
#                user_class_id = id3330
#            elif data_dictionary["class_type"] == "💃Хореография":
#                user_class_id = id3340

