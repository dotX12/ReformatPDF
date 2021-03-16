import re
from typing import Union, List


class FormatDict:

    @staticmethod
    def faculty_with_students_format(code, group_name, number_of_seats, applications, consent, students) -> dict:
        return {
            "code": code,
            "name": group_name,
            "number_of_seats": number_of_seats,
            "applications": applications,
            "consent": consent,
            "students": students
        }

    @staticmethod
    def faculty_without_students_format(code, group_name, number_of_seats, applications, consent):
        return {
            "code": code,
            "name": group_name,
            "number_of_seats": number_of_seats,
            "applications": applications,
            "consent": consent
        }

    @staticmethod
    def student_format(full_name, form_of_education, document_type, consent):
        return {'name': full_name,
                'form_of_education': form_of_education,
                'document_type': document_type,
                'consent': consent}


class ReformatData(FormatDict):
    regex_carriage_return = re.compile(r'[\n\r\t]')  # Поиск кореток переноса и т.д.
    regex_split_name_form_education = re.compile(r'\s\((.*?)\)')  # Поиск (Аспирантура) / (Бакалавриат)
    max_len_code_symbols = 50

    def __init__(self, data_dict: Union[List[dict]]):
        self.data = data_dict

    def reformat(self) -> dict:
        if len(self.data) == 1 or len(self.data[0]['text']) > self.max_len_code_symbols:
            pass
        else:
            if self.data[2]['text']:
                return self.normalize_faculty_info()
            if self.data[0]['text']:
                if self.data[1]['text']:
                    return self.normalize_user_info_1()
                if self.data[3]['text']:
                    return self.normalize_user_info_0()
            if not self.data[0]['text'] and not self.data[3]['text']:
                return self.normalize_user_info_1()
            else:
                self.normalize_user_info_0()

    def normalize_faculty_info(self) -> dict:
        if '\r' not in self.data[0]['text']:
            self.data[1]['text'] = self.regex_carriage_return.sub(" ", self.data[1]['text'])
            code = self.data[0]['text']
            name = self.data[1]['text']
            number_of_seats = self.data[2]['text']
            applications = self.data[3]['text']
            consent = self.data[5]['text']
            return self.faculty_without_students_format(code, name, number_of_seats, applications, consent)
        else:
            self.data[2]['text'] = self.regex_carriage_return.sub(" ", self.data[2]['text'])
            code = self.data[1]['text']
            name = self.data[2]['text']
            number_of_seats = self.data[3]['text']
            applications = self.data[4]['text']
            consent = self.data[5]['text']
            return self.faculty_without_students_format(code, name, number_of_seats, applications, consent)

    def normalize_user_info_1(self) -> dict:
        self.data[1]['text'] = self.regex_carriage_return.sub(" ", self.data[1]['text'])
        full_name, form_of_education = re.split(self.regex_split_name_form_education, self.data[1]['text'])[:2]
        document_type = self.data[4]['text']
        consent = True if self.data[5]['text'] != '' else False
        return self.student_format(full_name, form_of_education, document_type, consent)

    def normalize_user_info_0(self) -> dict:
        self.data[0]['text'] = self.regex_carriage_return.sub(" ", self.data[0]['text'])
        full_name, form_of_education = re.split(self.regex_split_name_form_education, self.data[0]['text'])[:2]
        document_type = self.data[3]['text']
        consent = True if self.data[4]['text'] != '' else False
        return self.student_format(full_name, form_of_education, document_type, consent)
