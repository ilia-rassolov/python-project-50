---

### Hexlet tests and linter status:

[![hexlet-check](https://github.com/ilia-rassolov/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/ilia-rassolov/python-project-50/actions/workflows/hexlet-check.yml) [![my-check](https://github.com/ilia-rassolov/python-project-50/actions/workflows/my-check.yml/badge.svg)](https://github.com/ilia-rassolov/python-project-50/actions/workflows/my-check.yml)

[![Maintainability](https://api.codeclimate.com/v1/badges/a723eafeff9ce50f593f/maintainability)](https://codeclimate.com/github/ilia-rassolov/python-project-50/maintainability) [![Test Coverage](https://api.codeclimate.com/v1/badges/a723eafeff9ce50f593f/test_coverage)](https://codeclimate.com/github/ilia-rassolov/python-project-50/test_coverage)

---
<table>
    <tr>
        <th>Hexlet tests and linter status</th>
    </tr>
    <tr>
        <td>[![hexlet-check](https://github.com/ilia-rassolov/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/ilia-rassolov/python-project-50/actions/workflows/hexlet-check.yml)</td>
        <td>[![my-check](https://github.com/ilia-rassolov/python-project-50/actions/workflows/my-check.yml/badge.svg)](https://github.com/ilia-rassolov/python-project-50/actions/workflows/my-check.yml)</td>
    </tr>
    <tr>
        <td>[![Maintainability](https://api.codeclimate.com/v1/badges/a723eafeff9ce50f593f/maintainability)](https://codeclimate.com/github/ilia-rassolov/python-project-50/maintainability)</td>
        <td>[![Test Coverage](https://api.codeclimate.com/v1/badges/a723eafeff9ce50f593f/test_coverage)](https://codeclimate.com/github/ilia-rassolov/python-project-50/test_coverage)</td>
    </tr>
</table>


---


### Это мой второй учебный проект на Hexlet. Он называется **"Вычислитель отличий"**

Это приложение позволяет сравнивать данные в двух файлах, доступные форматы **.json**, **.yaml** или **.yml**

---

## Эта команда выводит описание решаемой задачи и список опций

`gendiff -h`

## Сравниваем данные, расположенные в аргументах (пути 2-х файлов)

По умолчанию используется форматтер stylish

`gendiff tests/fixtures/nest_f1.json tests/fixtures/nest_f2.yaml`

[![asciicast](https://asciinema.org/a/OHyPacXfjy2BaJmTb3GngHDX9.svg)](https://asciinema.org/a/OHyPacXfjy2BaJmTb3GngHDX9)

## Сравнение также доступно при помощи форматтера plain
   
Он выводит результат в виде текста

`gendiff tests/fixtures/nest_f1.yaml tests/fixtures/nest_f2.yaml -f plain`
 
[![asciicast](https://asciinema.org/a/d5VJcbxy90y1l4ZJ9L3CMnPox.svg)](https://asciinema.org/a/d5VJcbxy90y1l4ZJ9L3CMnPox)

## Форматтер json серилизует (упаковывает) сравнение данных в формат json

Это необходимо, например, для интеграции с другими программами

`gendiff tests/fixtures/nest_f1.yaml tests/fixtures/nest_f2.yaml -f json`

[![asciicast](https://asciinema.org/a/TdDDKWXcEkETXczQESVoODOoY.svg)](https://asciinema.org/a/TdDDKWXcEkETXczQESVoODOoY)

---
