from .formatter import FormatDict


class FixRepetitionsGroups(FormatDict):
    def __init__(self, data_json):
        self.data_json = data_json

    def get_repetitions(self):
        full_groups = []
        all_faculties_names = []
        faculties_names_repetitions = []

        for group in self.data_json:
            if group['name'] not in all_faculties_names:
                all_faculties_names.append(group['name'])
                full_groups.append(group)

            else:
                if group['name'] not in faculties_names_repetitions:
                    faculties_names_repetitions.append(group['name'])
        return faculties_names_repetitions

    def collection_and_unique(self):
        faculties_names_repetitions = self.get_repetitions()

        collection = {}
        all_groups_without_repetitions = []

        for group in self.data_json:
            if group['name'] in faculties_names_repetitions:
                if group['name'] not in collection.keys():
                    collection[group['name']] = self.faculty_with_students_format(
                        group['code'], group['name'],
                        group['number_of_seats'],
                        group['applications'],
                        group['consent'],
                        [])

                for student in group['students']:
                    collection[group['name']]['students'].append(student)
            else:
                all_groups_without_repetitions.append(group)
        list_collection_without_keys = list(collection.values())

        return list_collection_without_keys, all_groups_without_repetitions

    def wrap(self):
        collection, unique = self.collection_and_unique()
        new_json = [*unique, *collection]
        return new_json
