# ReformatPDF
A program that allows you to convert large PDF tables to JSON for further work.
<p align="center">
  <img src="https://user-images.githubusercontent.com/64792903/111350987-bd596900-8693-11eb-891a-8bc76de59b70.png">
<br><br>
  <img src="https://user-images.githubusercontent.com/64792903/111351582-5d16f700-8694-11eb-85b6-fc4505cf64fc.png">
</p>
</details>

<details>
  <summary>Spoiler func reformat</summary>
  
```text
def reformat(self) -> dict:
        
  В зависимости от полученного списка словарей форматирует данные по нужному шаблону.

  [{'top': 241.32117, 'left': 114.458305, 'width': 148.84747314453125, 'height': 23.783233642578125,
   'text': 'Шулаева Евгения Юрьевна\r(Бакалавриат)'},
  {'top': 241.32117, 'left': 263.3058, 'width': 58.32025146484375, 'height': 23.783233642578125, 'text': ''},
  {'top': 241.32117, 'left': 321.62604, 'width': 53.400787353515625, 'height': 23.783233642578125, 'text': ''},
  {'top': 241.32117, 'left': 375.02682, 'width': 95.03976440429688, 'height': 23.783233642578125, 'text': 'Копия'},
  {'top': 241.32117, 'left': 470.0666, 'width': 94.81597900390625, 'height': 23.783233642578125, 'text': 'V'},
  {'top': 0.0, 'left': 0.0, 'width': 0.0, 'height': 0.0, 'text': ''}]
  Вернет : 
  {'name': 'Шулаева Евгения Юрьевна', 'form_of_education': 'Бакалавриат', 'document_type': 'Копия', 'consent': True}


  [{'top': 264.92746, 'left': 64.614006, 'width': 49.84033966064453, 'height': 12.490386962890625, 'text': '48.03.01'},
  {'top': 264.92746, 'left': 114.454346, 'width': 148.8521728515625, 'height': 12.490386962890625, 'text': 'Теология'},
  {'top': 264.92746, 'left': 263.30652, 'width': 58.32073974609375, 'height': 12.490386962890625, 'text': '9'},
  {'top': 264.92746, 'left': 321.62726, 'width': 53.399078369140625, 'height': 12.490386962890625, 'text': '32'},
  {'top': 264.92746, 'left': 375.02634, 'width': 95.03768920898438, 'height': 12.490386962890625, 'text': ''},
  {'top': 264.92746, 'left': 470.06403, 'width': 94.8138427734375, 'height': 12.490386962890625, 'text': '9'}]
  Вернет:
  {'code': '48.03.01', 'name': 'Теология', 'number_of_seats': '9', 'applications': '32', 'consent': '9'}


```
