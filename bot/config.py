from enum import Enum

token = "6013008737:AAFsTNqzddmw8a8QT8Hj65fpRRgeSmcYrNw"
db_file = "database.vdb"


class States(Enum):
    """
    Мы используем БД Vedis, в которой хранимые значения всегда строки,
    поэтому и тут будем использовать тоже строки (str)
    """
    S_START = "0"  # Начало нового диалога
    S_ENTER_first_text= "1"
    S_ENTER_second_text = "2"
    S_ENTER_number = "3"
    S_ENTER_name = "4"
    S_ENTER_surname = "5"
    S_ENTER_birthday = "6"
    S_ENTER_day = "7"
    S_ENTER_month = "8"
    S_ENTER_year = "9"
    S_ENTER_where_are_you_from = "10"
    S_ENTER_district = "11"
    S_ENTER_town_and_district = "12"
    S_ENTER_edu = "13"
    S_ENTER_uzb = "14"
    S_ENTER_ru = "15"
    S_ENTER_eng = "16"
    S_ENTER_work_experience = "17"
    S_ENTER_work_experience_yes = "18"
