# bulletin-board
## Итоговое задание "Доска объявлений"
### В рамках итогового задания D16 реализовано следующее:
- Регистрация на сайте с подтверждением email
- Функционал по восстановлению пароля
- Возможность публикации объявлений после подтверждения почты
- В объявление можно добавлять картинки и видео, а также прилагать файлы
- Пользователи имеют доступ только к своему загруженному медиаконтенту
- Редактирование и удаление только своих объявлений
- Личный кабинет с доступом к откликам на свои объявления и фильтрацией откликов по объявлению
- Авторизованные пользователи могут добавлять отклики на объявления
- Отправка письма автору объявления после появления отклика
- Удаление и подтверждение откликов на свои объявления
- После подтверждения отклика, отправка письма автору отклика
- Ежесуточная рассылка новых объявлений

cd ~
source venv/bin/activate
cd /mnt/c/Users/romab/OneDrive/Documents/GitHub/Bulletin-Board-Tutorial
celery -A Board worker -l INFO -B