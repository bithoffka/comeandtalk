import logging
from aiogram import types, Bot, Dispatcher, executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from markups import *
from catid_generator import *

token = "6509194424:AAGnHAw_eNFre4Y8KlRvIOs_PGOJbNaPg3w"
#Test token - 6100825136:AAHwtNxu-kaHE2K2aGuslJEclVSZPtyRtm8
#Cat bot token - 6509194424:AAGnHAw_eNFre4Y8KlRvIOs_PGOJbNaPg3w

bot = Bot(token)
dp = Dispatcher(bot, storage=MemoryStorage())

logging.basicConfig(level=logging.INFO)

manager_list = ["1440788864", "1184685120"]

class ApplicationStatesGroup(StatesGroup):
	age_group = State()
	direction = State()
	class_type = State()
	phone_number = State()

def LogMessage(message):
	logging.info(f"Message from {message.from_user.first_name}, user ID: {message.from_user.id}: {message.text}")

def ChatTypePrivate(message): return message.chat.type == "private"

@dp.message_handler(commands="start")
async def start(message: types.Message):
	if ChatTypePrivate(message):
		LogMessage(message)

		markup_privacy = InlineKeyboardMarkup()
		markup_privacy.add(InlineKeyboardButton(text="Политика Конфиденциальности", url="https://jazzy-dasik-1615a8.netlify.app/"))

		await message.reply(f"Привет, {message.from_user.first_name}!\n🇬🇧Это бот Come & Talk🇪🇸\n\nЭтот бот поможет вам:\n🔰 Назначить урок\n🔰 Связаться с менеджером\n🔰 Узнать график работы\n🔰 Быть в курсе последних новостей\n🔰 Подписаться на наши социальные сети\n\nИ многое другое✅️\n\nℹ️Для списка команд выберите \"Помощь\" в меню\n\nℹ️Пользуясь ботом, вы соглашаетесь с Политикой Конфиденциальности, прочитать которую можно по кнопке ниже.", reply_markup=MainMarkup())
		await message.answer("↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓", reply_markup=markup_privacy)
	else:
		await message.reply("Бот не работает в группах, перейдите в приватный чат")

@dp.message_handler(commands="sched")
async def sched(message: types.Message):
	if ChatTypePrivate(message):
		LogMessage(message)

		await message.reply("⏰Часы работы всех наших центров развития⏰:\n\n📍 г.Михайловск, ул.Ленина, 111\n\n⏱ пн - 09:00–19:00\n⏱ вт - 09:00–19:00\n⏱ ср - 09:00–19:00\n⏱ чт - 09:00–19:00\n⏱ пт - 09:00–19:00\n⏱ сб - 09:00–19:00\n⏱ вс - 09:00–15:00\n\n📍 г.Михайловск, ул.Георгиевская,107\n\n⏱ пн - 09:00–19:00\n⏱ вт - 09:00–19:00\n⏱ ср - 09:00–19:00\n⏱ чт - 09:00–19:00\n⏱ пт - 09:00–19:00\n⏱ сб - 09:00–19:00\n⏱ вс - 09:00–15:00\n\n☎️ Номер телефона: 61-09-90, +7-(962)-451-09-90")
	else:
		await message.reply("Бот не работает в группах, перейдите в приватный чат")

@dp.message_handler(commands="info")
async def info(message: types.Message):
	if ChatTypePrivate(message):	
		LogMessage(message)

		await message.reply("ℹ️Информация\n\n📱Наш ВК: https://vk.com/comeandtalkk\n\n☎️ Номер телефона: 61-09-90, +7-(962)-451-09-90\n✉️ Почта: comeandtalk@yandex.ru\n🕸 Наш сайт: comeandtalk.ru")
		await message.answer("ИП: Асирян Сатинэ Сергеевна\nИНН: 262303681451\nОГРН: 311265124400025\nВиды деятельности: 85.11, 85.12, 85.13, 85.14, 85.21, 85.22, 85.41, 85.42")
	else:
		await message.reply("Бот не работает в группах, перейдите в приватный чат")

@dp.message_handler(commands="help")
async def help(message: types.Message):
	if ChatTypePrivate(message):	
		LogMessage(message)

		await message.reply("🛠Помощь🛠\n\n/start - Перезапустить бота\n/signup - Записаться на занятие в нашем центре\n/sched - Раписание работы наших центров\n/info - Информация о нашей организации\n/help - Помощь")
	else:
		await message.reply("Бот не работает в группах, перейдите в приватный чат")

@dp.message_handler(commands="signup")
async def signup(message: types.Message):
	if ChatTypePrivate(message):	
		LogMessage(message)

		markup = InlineKeyboardMarkup()
		markup.add(InlineKeyboardButton("Наш веб-сайт", url="https://comeandtalk.ru"))
		await message.reply("📑Перед тем, как записаться, ознакомьтесь с программами обучения по кнопке снизу", reply_markup=markup)

		await message.answer("🔰Выберите возраст🔰", reply_markup=AgeGroupMarkup())
		await ApplicationStatesGroup.age_group.set()
	else:
		await message.reply("Бот не работает в группах, перейдите в приватный чат")

@dp.message_handler(commands="account")
async def account(message: types.Message):
	await message.answer("Тут должен быть личный кабинет")

#FSM HANDLERS START

@dp.message_handler(state=ApplicationStatesGroup.age_group)
async def fsm_age_group_handler(message: types.Message, state: FSMContext):
	LogMessage(message)

	async with state.proxy() as data:
		if message.text == "👶Дети (4-7 лет)" or message.text == "👱Подростки (7-18 лет)" or message.text == "🧔‍♂️Взрослые (18-81 лет)":
			data["age_group"] = message.text

			await message.reply("🔰Выберите программу🔰", reply_markup=DirectionMarkup())
			await ApplicationStatesGroup.next()
		elif message.text == "🚫Отмена заявки🚫":
			await message.reply("❌Заявка отменена успешно!", reply_markup=MainMarkup())
			await state.finish()
		else:
			await message.reply("Воспользуйтесь кнопками ниже, чтобы установить возрастную категорию!")

@dp.message_handler(state=ApplicationStatesGroup.direction)
async def fsm_direction_handler(message: types.Message, state: FSMContext):
	LogMessage(message)

	async with state.proxy() as data:
		if message.text == "🎓Интеллектуальная" or message.text == "🥋Спортивная" or message.text == "🎨Творческая":
			data["direction"] = message.text

			age_group = data["age_group"]
			direction = data["direction"]

			next_markup = None

			if age_group == "👶Дети (4-7 лет)":
				if direction == "🎓Интеллектуальная":
					next_markup = KidsIntel()
				elif direction == "🥋Спортивная":
					next_markup = KidsSport()
				elif direction == "🎨Творческая":
					next_markup = KidsArt()
			elif age_group == "👱Подростки (7-18 лет)":
				if direction == "🎓Интеллектуальная":
					next_markup = TeensIntel()
				elif direction == "🥋Спортивная":
					next_markup = TeensSport()
				elif direction == "🎨Творческая":
					next_markup = TeensArt()
			elif age_group == "🧔‍♂️Взрослые (18-81 лет)":
				if direction == "🎓Интеллектуальная":
					next_markup = AdultsIntel()
				elif direction == "🥋Спортивная":
					next_markup = AdultsSport()
				elif direction == "🎨Творческая":
					next_markup = AdultsArt()

			await message.reply("🔰Выберите тип занятия🔰", reply_markup=next_markup)
			await ApplicationStatesGroup.next()
		elif message.text == "🚫Отмена заявки🚫":
			await message.reply("❌Заявка отменена успешно!", reply_markup=MainMarkup())
			await state.finish()
		else:
			await message.reply("Воспользуйтесь кнопками ниже, чтобы выбрать программу!")

@dp.message_handler(state=ApplicationStatesGroup.class_type)
async def fsm_class_type_handler(message: types.Message, state: FSMContext):
	LogMessage(message)

	async with state.proxy() as data:
		if message.text == "🇬🇧Английский язык" or message.text == "🔠Логопед" or message.text == "📚Подготовка к школе" or message.text == "💃Хореография" or message.text == "🧐Развитие" or message.text == "🔢Ментальная алгебра" or message.text == "📖Подготовка к ОГЭ/ЕГЭ/ВПР" or message.text == "🇦🇲Армянский язык" or message.text == "🇪🇸Испанский язык" or message.text == "🔊Хип-Хоп" or message.text == "🥋Карате" or message.text == "🎨Рисование" or message.text == "🎭Актерское мастерство" or message.text == "🖼Исскуствоведение" or message.text == "🇫🇷Французский язык" or message.text == "🎤Ораторское искуство" or message.text == "🖼Рисование" or message.text == "🧘Йога" or message.text == "💪Фитнес":
			data["class_type"] = message.text

			await message.reply("🔰Поделитесь контактом🔰", reply_markup=RequestContact())
			await ApplicationStatesGroup.next()
		elif message.text == "🚫Отмена заявки🚫":
			await message.reply("❌Заявка отменена успешно!", reply_markup=MainMarkup())
			await state.finish()
		else:
			await message.reply("Воспользуйтесь кнопками ниже, чтобы выбрать тип занятия!")

@dp.message_handler(content_types=types.ContentType.CONTACT, state=ApplicationStatesGroup.phone_number)
async def fsm_phone_number_handler(message: types.Message, state: FSMContext):
	LogMessage(message)
	
	async with state.proxy() as data:
		data["phone_number"] = message.contact.phone_number

		for i in manager_list:
			await bot.send_message(i, f'Заявка на регистрацию!\nID: {message.chat.id}\nUsername: {message.from_user.first_name}\nВозрастная категория: {data["age_group"]}\nПрограмма: {data["direction"]}\nТип занятий: {data["class_type"]}\nКонтакт: {data["phone_number"]}')
		
		data_dictionary = {
				"TID": message.chat.id,
			    "TNAME": message.from_user.first_name,
				"age_group": data["age_group"],
				"direction": data["direction"],
				"class_type": data["class_type"],
				"phone_number": message.contact.phone_number
			}
		
	await message.reply("✅Готово, ваша заявка отправлена менеджеру, мы свяжемся с вами в ближайшее время!", reply_markup=MainMarkup())
	await state.finish()

#FSM HANDLERS END

@dp.message_handler()
async def handler(message: types.Message):
	if ChatTypePrivate(message):
		text = message.text.strip()

		if text == "🕰️График работы🕰️":
			await sched(message)
		elif text == "🔄Перезапустить бота🔄":
			await start(message)
		elif text == "📑Записаться на занятие📑":
			await signup(message)
		elif text == "ℹ️Информацияℹ️":
			await info(message)
		elif text == "🛠Помощь🛠":
			await help(message)
		elif text == "📰Личный кабинет📰":
			await account(message)
		else:
			LogMessage(message)
			await message.answer("Ваша команда не распознана, напишите /help для помощи, или нажмите кнопку \"Помощь\" внизу!")
	else:
		await message.reply("Бот не работает в группах, перейдите в приватный чат")

if __name__ == "__main__":
	executor.start_polling(dp, skip_updates=True)
