import json
import string
from random import choices
from typing import Union, List
import os
import tabula

from .formatter import ReformatData
from .compressor import FixRepetitionsGroups
from .utils import delete_file, is_file


class ReformatPDF:
    def __init__(self):
        self.list_groups_students: Union[List[dict]] = []

    def create_faculty_and_students_from_tabula_json(self, temp_json_name) -> None:
        with open(temp_json_name) as file:
            json_data = json.load(file)
            for ind_i, _ in enumerate(json_data):
                for _, j in enumerate(json_data[ind_i]['data']):
                    temp_re = ReformatData(j)
                    temp_formatted = temp_re.reformat()
                    self.list_groups_students.append(temp_formatted)
        #  print(self.list_groups_students)

    def compose_students_to_group(self) -> list:
        new_faculties = []
        temp_faculty = {}

        for _, i_value in enumerate(self.list_groups_students[3:]):
            if i_value is not None:
                if 'code' in i_value.keys():
                    temp_faculty = i_value
                    temp_faculty['students'] = []
                    new_faculties.append(temp_faculty)
                else:
                    temp_faculty['students'].append(i_value)
        return new_faculties

    def translate(self, pdf_name: str, new_json_name: str = 'reformatted_pdf.json', delete_temp: bool = True) -> None:
        if is_file(pdf_name):
            new_pdf_path = f"TEMP/{os.path.basename(pdf_name)}"
            temp_json_name = f"{new_pdf_path}_{''.join(choices(string.ascii_uppercase + string.digits, k=16))}.json"
            tabula.convert_into(pdf_name, temp_json_name, output_format="json", pages='all')
            self.create_faculty_and_students_from_tabula_json(temp_json_name)
            composed = self.compose_students_to_group()
            new_format_composed = FixRepetitionsGroups(composed).wrap()
            with open(new_json_name, 'w', encoding='utf-8') as f:
                json.dump(new_format_composed, f, indent=4, ensure_ascii=False)
            if delete_temp:
                delete_file(temp_json_name)
