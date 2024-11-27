from django.conf import settings
from django.core.mail import send_mail


def send_register_email(email):
    ''' Отправка письма после регистрации '''
    send_mail(
        subject='Поздравляю с регистрацией',
        message='Вы успешно зарегистрировались! Добро пожаловать!',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email]
    )


def send_new_password(email, new_password):
    ''' Отправка письма после изменения пароля '''
    send_mail(
        subject='Вы успешно изменили пароль',
        message=f'Ваш новый пароль: {new_password}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email]
    )
