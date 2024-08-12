def send_email(message, recipient,*, sender = "university.help@gmail.com" ):
    end = ".com", ".ru", ".net"
    for i in recipient:
        if i == "@":
            result1 = True
            break
        else:
            result1 = False
            continue
    if  recipient.endswith(end):
        result2 = True
    else:
        result2 = False

    for j in sender:
        if j == "@":
            result3 = True
            break
        else:
            result3 = False
            continue
    if  sender.endswith(end):
        result4 = True
    else:
        result4 = False
    if result1 != True or result2 != True or result3 !=  True or result4 != True:
        print("Невозможно отправить письмо с адреса ", sender, "на адрес " , recipient)
    elif sender == recipient:
        print('Нельзя отправить письмо самому себе!')
    elif sender == "university.help@gmail.com":
          print('"Письмо успешно отправлено с адреса', sender, 'на адрес ',recipient)
    else:
        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо  отправлено с адреса', sender, 'на адрес ', recipient)

send_email("Это сообщение для проверки связи",'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender = 'urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')

