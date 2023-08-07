async def read_mail(email, password):
    import imaplib
    
    # Создание экземпляра класса работы с почтой
    mail = imaplib.IMAP4_SSL("imap.mail.ru")

    # Вход в почту
    
    mail.login(email, password)

    # Выбор папки из который читаем письма
    mail.select("Название папки")

    # Поиск писем
    status, email_ids = mail.search(None, "ALL")
    email_id_list = email_ids[0].split()

    # Получаем письма
    for email_id in email_id_list:
        status, email_data = mail.fetch(email_id,"(RFC822)") # 1- ид письма 2- его форматирования(в каком виде мы его получим)
        raw_email = email_data[0][1] # условно
        print(raw_email)

    mail.logout()
