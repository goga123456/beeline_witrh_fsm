from enum import Enum

token = "5875923517:AAHdupc3iddCYl-5XYQj79ZeCeU80cx28XU"
db_file = "database.vdb"


class States(Enum):
    """
    Мы используем БД Vedis, в которой хранимые значения всегда строки,
    поэтому и тут будем использовать тоже строки (str)
    """
    S_START = "0"  # Начало нового диалога
    S_ENTER_lang = "1"
    S_ENTER_first_text= "2"
    S_ENTER_second_text = "3"
    S_ENTER_number = "4"
    S_ENTER_name = "5"
    S_ENTER_surname = "6"
    S_ENTER_birthday = "7"
    S_ENTER_day = "8"
    S_ENTER_month = "9"
    S_ENTER_year = "10"
    S_ENTER_where_are_you_from = "11"
    S_ENTER_district = "12"
    S_ENTER_town_and_district = "13"
    S_ENTER_edu = "14"
    S_ENTER_uzb = "15"
    S_ENTER_ru = "16"
    S_ENTER_eng = "17"
    S_ENTER_work_experience = "18"
    S_ENTER_work_experience_yes = "19"
