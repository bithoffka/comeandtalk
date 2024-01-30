from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def MainMarkup():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    start_button = KeyboardButton("🔄Перезапустить бота🔄")
    signup_button = KeyboardButton("📑Записаться на занятие📑")
    sched_button = KeyboardButton("🕰️График работы🕰️")
    info_button = KeyboardButton("ℹ️Информацияℹ️")
    help_button = KeyboardButton("🛠Помощь🛠")

    markup.add(start_button)
    markup.add(signup_button)
    markup.add(sched_button)
    markup.add(info_button, help_button)

    return markup

# AGE GROUP START

def AgeGroupMarkup():
    markup = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)

    kids_button = KeyboardButton("👶Дети (4-7 лет)")
    teens_button = KeyboardButton("👱Подростки (7-18 лет)")
    adults_button = KeyboardButton("🧔‍♂️Взрослые (18-81 лет)")
    cancel_button = KeyboardButton("🚫Отмена заявки🚫")

    markup.add(kids_button, teens_button, adults_button, cancel_button)

    return markup

# AGE GROUP END

# DIRECTION START

def DirectionMarkup():
    markup = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)

    intel_button = KeyboardButton("🎓Интеллектуальная")
    sport_button = KeyboardButton("🥋Спортивная")
    art_button = KeyboardButton("🎨Творческая")
    cancel_button = KeyboardButton("🚫Отмена заявки🚫")

    markup.add(intel_button, sport_button, art_button, cancel_button)

    return markup

# DIRECTION END

# KIDS START

def KidsIntel():
    markup = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    
    eng_button = KeyboardButton("🇬🇧Английский язык")
    speech_therapist_button = KeyboardButton("🔠Логопед")
    preparation_button = KeyboardButton("📚Подготовка к школе")
    cancel_button = KeyboardButton("🚫Отмена заявки🚫")

    markup.add(eng_button, speech_therapist_button, preparation_button, cancel_button)
    
    return markup

def KidsSport():
    markup = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)

    dance_button = KeyboardButton("💃Хореография")
    cancel_button = KeyboardButton("🚫Отмена заявки🚫")

    markup.add(dance_button, cancel_button)

    return markup

def KidsArt():
    markup = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)

    development_button = KeyboardButton("🧐Развитие")
    cancel_button = KeyboardButton("🚫Отмена заявки🚫")

    markup.add(development_button, cancel_button)

    return markup

# KIDS END

# TEENS START
    
def TeensIntel():
    markup = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)

    preparation_button = KeyboardButton("📚Подготовка к школе")
    meth_button = KeyboardButton("🔢Ментальная алгебра")
    exams_button = KeyboardButton("📖Подготовка к ОГЭ/ЕГЭ/ВПР")
    eng_button = KeyboardButton("🇬🇧Английский язык")
    arm_button = KeyboardButton("🇦🇲Армянский язык")
    esp_button = KeyboardButton("🇪🇸Испанский язык")
    cancel_button = KeyboardButton("🚫Отмена заявки🚫")

    markup.add(preparation_button, meth_button, exams_button, eng_button, arm_button, esp_button, cancel_button)

    return markup

def TeensSport():
    markup = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    
    dance_button = KeyboardButton("💃Хореография")
    hip_hop_button = KeyboardButton("🔊Хип-Хоп")
    karate = KeyboardButton("🥋Карате")
    cancel_button = KeyboardButton("🚫Отмена заявки🚫")

    markup.add(dance_button, hip_hop_button, karate, cancel_button)

    return markup

def TeensArt():
    markup = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)

    art_button = KeyboardButton("🎨Рисование")
    acting_button = KeyboardButton("🎭Актерское мастерство")
    art_education_button = KeyboardButton("🖼Исскуствоведение")
    dance_button = KeyboardButton("💃Хореография")
    cancel_button = KeyboardButton("🚫Отмена заявки🚫")

    markup.add(art_button, acting_button, art_education_button, dance_button, cancel_button)

    return markup

# TEENS END

# ADULTS START
    
def AdultsIntel():
    markup = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)

    eng_button = KeyboardButton("🇬🇧Английский язык")
    arm_button = KeyboardButton("🇦🇲Армянский язык")
    esp_button = KeyboardButton("🇪🇸Испанский язык")
    frc_button = KeyboardButton("🇫🇷Французский язык")
    cancel_button = KeyboardButton("🚫Отмена заявки🚫")

    markup.add(frc_button, eng_button, arm_button, esp_button, cancel_button)

    return markup

def AdultsArt():
    markup = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)

    oratory_button = KeyboardButton("🎤Ораторское искуство")
    acting_button = KeyboardButton("🎭Актерское мастерство")
    art_education_button = KeyboardButton("🖼Рисование")
    dance_button = KeyboardButton("💃Хореография")
    cancel_button = KeyboardButton("🚫Отмена заявки🚫")

    markup.add(oratory_button, acting_button, art_education_button, dance_button, cancel_button)

    return markup

def AdultsSport():
    markup = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)

    yoga_button = KeyboardButton("🧘Йога")
    fitness_button = KeyboardButton("💪Фитнес")
    cancel_button = KeyboardButton("🚫Отмена заявки🚫")

    markup.add(yoga_button, fitness_button, cancel_button)

    return markup

# ADULTS END

# REQUEST CONTACT START

def RequestContact():
    markup = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)

    request_contact_button = KeyboardButton("📱Поделиться контактом", request_contact=True)

    markup.add(request_contact_button)

    return markup

# REQUEST CONTACT END
