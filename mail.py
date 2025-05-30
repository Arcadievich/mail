import smtplib
import os
from dotenv import load_dotenv

load_dotenv()
login = os.getenv('LOGIN')
password = os.getenv('MAIL_APP_PASSWORD')

website = 'https://dvmn.org/profession-ref-program/dmitry_274/VoB3j/'
friend_name = 'Лёха'
my_name = 'Димон'

letter = ("""\
From: dimotron1999@yandex.ru
To: dimotron1999@yandex.ru
Subject: Приглашение!
Content-Type: text/plain; charset="UTF-8";

Привет, {0}! {1} приглашает тебя на сайт {2}!

{2} — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на {2}? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → {2}  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.""").format(friend_name, my_name, website)

message = letter.encode("UTF-8")
server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
server.login(login, password)
server.sendmail('dimotron1999@yandex.ru', 'dimotron1999@yandex.ru', message)
server.quit()