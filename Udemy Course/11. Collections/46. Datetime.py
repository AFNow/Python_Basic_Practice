# Модуль datetime представляет собой функционал подсчета в формате [year[, month[, day[, hour[, minute[, second[, microsecond[, tzinfo]]]]]]]]
# Класс datetime.date(year, month, day) - стандартная дата. Атрибуты: year, month, day. Неизменяемый объект.
# Класс datetime.time(hour=0, minute=0, second=0, microsecond=0, tzinfo=None) - стандартное время, не зависит от даты. Атрибуты: hour, minute, second, microsecond, tzinfo.
# Класс datetime.timedelta - разница между двумя моментами времени, с точностью до микросекунд.
# Класс datetime.tzinfo - абстрактный базовый класс для информации о временной зоне (например, для учета часового пояса и / или летнего времени).
# Класс datetime.datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None) - комбинация даты и времени.

# Методы класса datetime:
# datetime.today() - объект datetime из текущей даты и времени. Работает также, как и datetime.now() со значением tz=None.
# datetime.fromtimestamp(timestamp) - дата из стандартного представления времени.
# datetime.fromordinal(ordinal) - дата из числа, представляющего собой количество дней, прошедших с 01.01.1970.
# datetime.now(tz=None) - объект datetime из текущей даты и времени.
# datetime.combine(date, time) - объект datetime из комбинации объектов date и time.
# datetime.strptime(date_string, format) - преобразует строку в datetime (так же, как и функция strptime из модуля time).
# datetime.strftime(format) - см. функцию strftime из модуля time.
# datetime.date() - объект даты (с отсечением времени).
# datetime.time() - объект времени (с отсечением даты).
# datetime.replace([year[, month[, day[, hour[, minute[, second[, microsecond[, tzinfo]]]]]]]]) - возвращает новый объект datetime с изменёнными атрибутами.
# datetime.timetuple() - возвращает struct_time из datetime.
# datetime.toordinal() - количество дней, прошедших с 01.01.1970.
# datetime.timestamp() - возвращает время в секундах с начала эпохи.
# datetime.weekday() - день недели в виде числа, понедельник - 0, воскресенье - 6.
# datetime.isoweekday() - день недели в виде числа, понедельник - 1, воскресенье - 7.
# datetime.isocalendar() - кортеж (год в формате ISO, ISO номер недели, ISO день недели).
# datetime.isoformat(sep='T') - красивая строка вида "YYYY-MM-DDTHH:MM:SS.mmmmmm" или, если microsecond == 0, "YYYY-MM-DDTHH:MM:SS"
# datetime.ctime() - см. ctime() из модуля time.
import datetime
today = datetime.date.today()
b_day = datetime.date(today.year, 9, 30)
christmass = datetime.date(today.year, 12, 25)
till_b_day = b_day - today
till_christmass = christmass - today
print(f"Количество дней до Дня рождения: {till_b_day.days}")
print(f"Количество дней до Рождества: {till_christmass.days}")