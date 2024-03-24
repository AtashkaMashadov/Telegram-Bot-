import telebot 
import config
from telebot import types
import time
import sqlite3

bot=telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
	sti = open('static/welcome.webp', 'rb')
	bot.send_sticker(message.chat.id, sti)
	#KEYBOARD
	markup = types.ReplyKeyboardMarkup(resize_keyboard= True)
	key1 = types.KeyboardButton("About Us")
	key2 = types.KeyboardButton("Register")
	key3 = types.KeyboardButton("Academic")
	key4 = types.KeyboardButton("Student Services")
	key5 = types.KeyboardButton("Community")
	key6 = types.KeyboardButton('About @AIS-bot')


	markup.add(key1, key2, key3, key4, key5, key6)

		
	bot.send_message(message.chat.id, 'I am - <b>{1.first_name}</b>.'.format(message.from_user, bot.get_me()),parse_mode='html',reply_markup = markup)
	time.sleep(1.0)
	bot.send_message(message.chat.id, 'Ashgabat International School teaches students from 29+ countries.'.format(message.from_user, bot.get_me()),parse_mode='html',reply_markup = markup)
	time.sleep(1.0)
	bot.send_message(message.chat.id, 'The buttons show the main information about our school.'.format(message.from_user, bot.get_me()),parse_mode='html',reply_markup = markup)
	time.sleep(1.0)

	#------------------------------------------------------------------------

	conn = sqlite3.connect('users.sql')
	cur = conn.cursor()

	cur.execute('CREATE TABLE IF NOT EXISTS users (id int auto_increment primary key, name varchar(50)')
	conn.commit()
	cur.close()
	conn.close()
	user_name()

def user_name():
	conn = sqlite3.connect('users.sql')
	cur = conn.cursor()

	cur.execute('INSERT INTO users (name) VALUES ({0.first_name})')
	conn.commit()
	cur.close()
	conn.close()
@bot.message_handler(content_types=['text'])
def replying(message):
	if message.chat.type == 'private':
		if message.text == 'About Us':
			


			markup = types.InlineKeyboardMarkup(row_width = 2)
			item1 = types.InlineKeyboardButton('Welcome', url='https://ashgabat.qsi.org/about-us/welcome')
			item2 = types.InlineKeyboardButton('Accreditation', url='https://ashgabat.qsi.org/about-us/accreditation')
			item3 = types.InlineKeyboardButton('Facilities', url='https://ashgabat.qsi.org/about-us/facilities')
			item4 = types.InlineKeyboardButton('Faculty and Staff', url='https://ashgabat.qsi.org/about-us/faculty-and-staff')
			item5 = types.InlineKeyboardButton('History', url='https://ashgabat.qsi.org/about-us/history')
			item6 = types.InlineKeyboardButton('School Calendar', url='https://ashgabat.qsi.org/about-us/school-calendar')
			item7 = types.InlineKeyboardButton('Success Orientations', url='https://ashgabat.qsi.org/about-us/success-orientation')
			item8 = types.InlineKeyboardButton('Country Information', url='https://ashgabat.qsi.org/about-us/country-info')
			item9 = types.InlineKeyboardButton('Mastery Learning', url='https://ashgabat.qsi.org/about-us/mastery-learning')
			item10 = types.InlineKeyboardButton('Stats in Numbers', url='https://ashgabat.qsi.org/about-us/stats-in-numbers')
			item11 = types.InlineKeyboardButton('🎬Introduction Video🎬', url='https://player.vimeo.com/video/343801526?byline=0&api=1&h=3412c438e1')
			markup.add(item1,item2,item3,item4,item5,item6,item7,item8,item9,item10,item11)
			prg1='<b>QSI-AIS</b>\nQSI International School of Ashgabat, a member of Quality Schools International (QSI), is a private, non-profit, coeducational, college-preparatory institution.\n<b>PHILOSOPHY</b>\nQSI International School of Ashgabat believes in a personalized approach to instruction leading to mastery within a positive and enjoyable learning environment.\n<b>Enrollment</b>\nThe school encompasses Pre-K through Secondary IV with a current enrollment of 200.\n<b>Grading System:</b>\nTeachers evaluate mastery of each essential unit with an A or B.'
			bot.send_message(message.chat.id, prg1.format(message.from_user, bot.get_me()),parse_mode='html')
			bot.send_photo(message.chat.id, photo=open('static/AIS.jpg', 'rb'), reply_markup = markup)
			
		elif message.text == 'Register':
			markup = types.InlineKeyboardMarkup(row_width = 2)
			item1 = types.InlineKeyboardButton('Book Meeting/Tour', url='https://ashgabat.qsi.org/admissions/schedule-a-tour')
			item2 = types.InlineKeyboardButton('Admissions By Numbers', url='https://ashgabat.qsi.org/admissions/admissions-by-numbers')
			item3 = types.InlineKeyboardButton('Find Us', url='https://ashgabat.qsi.org/admissions/contact-us')
			item4 = types.InlineKeyboardButton('Registration Form', url='https://ashgabat.qsi.org/fs/resource-manager/view/6f1d91f6-5fd0-4dc8-bc8b-7988975fc67f')
			item5 = types.InlineKeyboardButton('Information Packet (English)', url='https://ashgabat.qsi.org/fs/resource-manager/view/bf10fec5-c90f-494b-889a-6c516eb34ad8')
			item6 = types.InlineKeyboardButton('Information Packet (Russian)', url='https://ashgabat.qsi.org/fs/resource-manager/view/7e8d5bb2-79b9-465d-b463-208cda7da561')
			item7 = types.InlineKeyboardButton('AIS Preschool Program Parent Handbook', url='https://ashgabat.qsi.org/fs/resource-manager/view/8cc61a40-71c4-481d-876b-bca568808617')
			item8 = types.InlineKeyboardButton('Student and Family Handbook', url='https://ashgabat.qsi.org/fs/resource-manager/view/74408a3f-8fc6-4df7-873f-946a0c60d3e9')
			item9 = types.InlineKeyboardButton('Admission Procedure Handbook', url='https://ashgabat.qsi.org/fs/resource-manager/view/0cc160fa-f6c0-4f5b-8dee-c132ca0fa6d4')
			markup.add(item1,item2,item3,item4,item5,item6,item7,item8,item9)
			prg2 = '<b>Welcome to our school community</b>.\nYou will find all of the forms, documentation, and information needed for our admissions process. Registration and admissions process may take up to 1 week to complete once all of your school records are processed. At any time, if you have any questions or concerns, please feel free to reach out to Yelena Kuvadova (yelena-kuvadova@qsi.org) our admissions specialist.'
			prg3 = 'After you have decided to attend AIS we will ask for a Registration Form along with:\n1️⃣ Photographs x2\n2️⃣ AIS medical form\n3️⃣ Parents passports copies\n4️⃣ Student passports copies\n5️⃣ Previous school records\n6️⃣ <b>$300 non-refundable fee</b>.\nAt this point we will schedule a date to assess language and math proficiency, which takes approximately 2 hours.\n<i>*To book a meeting, please fill in the form on "Book Meeting/Tour" under "In This Section" menu*</i>'
			bot.send_message(message.chat.id, prg2.format(message.from_user, bot.get_me()),parse_mode='html')
			time.sleep(1.0)
			bot.send_message(message.chat.id, prg3.format(message.from_user, bot.get_me()),parse_mode='html')
			bot.send_message(message.chat.id, '✉️Email: ashgabat@qsi.org\n☎️Phone: +99312- 48-90-27 / 28'.format(message.from_user, bot.get_me()),parse_mode='html', reply_markup = markup)
		elif message.text == 'Academic':
			markup = types.InlineKeyboardMarkup()
			item1 = types.InlineKeyboardButton('⚠️More about Academics⚠️', url ='https://ashgabat.qsi.org/academics')
			markup.add(item1)
			prg4 = '<b>Academic Rigor and Success</b>\nAshgabat International School follows the Mastery Learning model of education. Students learn at a pace which allows them to develop a high level of proficiency (knowledge, skills, and competencies) in the curriculum that they are studying. This approach promotes academic rigor and academic success' 
			prg5 = 'Academic programs at Ashgabat International School focus on the development of 21st Century Learning skills such as:\n- Critical thinking\n- Problem solving\n- Leadership\n- Collaboration\n- Cultural awareness\n- Digital literacy.'
			bot.send_message(message.chat.id, prg4.format(message.from_user, bot.get_me()),parse_mode='html')
			time.sleep(1.0)
			bot.send_message(message.chat.id, prg5,parse_mode='html', reply_markup = markup)
		elif message.text == 'Student Services':
			markup = types.InlineKeyboardMarkup(row_width = 2)
			item1 = types.InlineKeyboardButton('SAT/TOEFL IBT', url = 'https://ashgabat.qsi.org/student-services/sat-toefl-ibt-test-in-turkmenistan')
			item2 = types.InlineKeyboardButton('Library', url = 'https://ashgabat.qsi.org/student-services/library')
			item3 = types.InlineKeyboardButton('Child Protection', url = 'https://ashgabat.qsi.org/student-services/child-protection')
			item4 = types.InlineKeyboardButton('Health and Safety', url = 'https://ashgabat.qsi.org/student-services/health-and-safety')
			markup.add(item1, item2, item3, item4)
			markup2 = types.InlineKeyboardMarkup(row_width = 2)
			item11 = types.InlineKeyboardButton('Support in the Classroom', callback_data = 'site1')
			item22 = types.InlineKeyboardButton('Support Students With Academic Сhallenges', callback_data = 'site2')
			item33 = types.InlineKeyboardButton('Social and Emotional Needs', callback_data = 'site3')
			item44 = types.InlineKeyboardButton('Intensive English Department', callback_data = 'site4')
			markup2.add(item11, item22, item33, item44)
			prg6 = '<b>Support, Resources, and Safety</b>\nQSI Ashgabat International School ensures that the education of each child is supported with the appropriate and right learning approach, resources to enhance learning, and the utmost consideration for student health, safety, and well-being.'
			bot.send_message(message.chat.id, prg6, parse_mode = 'html')
			bot.send_message(message.chat.id, 'To learn more about Student Services, check the buttons bellow', parse_mode = 'html', reply_markup = markup)
			bot.send_message(message.chat.id, '<b>At AIS we believe in meeting the academic, social and emotional needs of our students</b>.\nWe offer many programs and student services.', parse_mode = 'html', reply_markup = markup2)
		elif message.text == 'Community':
			markup = types.InlineKeyboardMarkup(row_width = 2)
			item1 = types.InlineKeyboardButton('Academic Calendar', url = 'https://ashgabat.qsi.org/community/event-calendar')
			item2 = types.InlineKeyboardButton('Parent Support Group', url = 'https://ashgabat.qsi.org/community/pto')
			item3 = types.InlineKeyboardButton('Events and Activities', url = 'https://ashgabat.qsi.org/community/events-and-activities')
			markup.add(item1, item2, item3)
			prg8 = '<b>The Ashgabat International School Community</b>\nAshgabat is a unique place to live, and we understand the school typically becomes the center of community life for most of our students and families. We offer many events and activities for all ages during the school day, in the evenings and on the weekends. The school also offers many amenities for the parents and the community to utilize throughout the day.'
			prg9 = 'The gym, library, coffee shop or any other facility of AIS are all at the disposal of our community.'
			prg10 = 'One of the yearly biggest traditions AIS holds is a Food Festival. This year about 2000 people participated in the festival. Food from around the world, as well as dancing and sports shows were enjoyed by the locals and international community.\n<i>To learn more click the buttons bellow</i>'
			bot.send_message(message.chat.id, prg8, parse_mode = 'html')
			time.sleep(1.0)
			bot.send_photo(message.chat.id, photo=open('static/gym.jpg', 'rb'))
			bot.send_message(message.chat.id, prg9, parse_mode = 'html')
			bot.send_photo(message.chat.id, photo=open('static/coffe.jpg', 'rb'))
			time.sleep(1.0)
			bot.send_message(message.chat.id, prg10, parse_mode = 'html')
			bot.send_photo(message.chat.id, photo=open('static/food.jpg', 'rb'), reply_markup = markup)


		else:
			bot.send_message(message.chat.id, 'While this is a bot, it doesnt understand your messages :(')
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'site1':
                bot.send_message(call.message.chat.id, '<b>Support in the Classroom</b>\nWe have a group of teachers who meet together on a weekly basis to address, assist and develop plans for students who might need support in the classroom.', parse_mode = 'html')
            elif call.data == 'site2':
                bot.send_message(call.message.chat.id, '<b>Support Students With Academic Сhallenges</b>\nWe do not have a student support services teacher, who can target specific academic needs and support students with academic challenges.', parse_mode = 'html')
            elif call.data == 'site3':
                bot.send_message(call.message.chat.id, '<b>Social and Emotional Needs</b>\nWe have a virtual  school counselor who can assist students with social and emotional needs. In addition, we have a virtual college counselor who can assist secondary students with college applications.', parse_mode = 'html')
            elif call.data == 'site4':
                bot.send_message(call.message.chat.id, '<b>Intensive English Department</b>\nWe also have an Intensive English Department to assist students who are learning the English language.', parse_mode = 'html')
 
    except Exception as e:
        print(repr(e))


bot.polling(none_stop=True)
