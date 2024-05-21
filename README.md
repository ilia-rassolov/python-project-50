#### Hexlet tests and linter status

[![hexlet-check](https://github.com/ilia-rassolov/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/ilia-rassolov/python-project-50/actions/workflows/hexlet-check.yml)

[![my-check](https://github.com/ilia-rassolov/python-project-50/actions/workflows/my-check.yml/badge.svg)](https://github.com/ilia-rassolov/python-project-50/actions/workflows/my-check.yml)

[![Maintainability](https://api.codeclimate.com/v1/badges/a723eafeff9ce50f593f/maintainability)](https://codeclimate.com/github/ilia-rassolov/python-project-50/maintainability)

[![Test Coverage](https://api.codeclimate.com/v1/badges/a723eafeff9ce50f593f/test_coverage)](https://codeclimate.com/github/ilia-rassolov/python-project-50/test_coverage)

---

### Это мой второй учебный проект на Hexlet. Он называется **"Вычислитель отличий"**

Это приложение позволяет сравнивать данные в двух файлах, доступные форматы для сравнения **.json**, **.yaml** или **.yml**

---

#### Установка проекта, запуск проверок

Требования:
Для установки проекта требуются установленные CPython ^3.10 и Poetry ^1.2.0

##### Скачайте проект, перейдите в директорию и установите зависимости с помощью Poetry

`git clone git@github.com:ilia-rassolov/python-project-50.git`

`cd python-project-50`

`make install`

---

##### Можно запустить проверку кода линтером и тестами

`make linter`

`make test`

---

#### Приложение готово к работе

Эта команда выводит описание решаемой задачи и список опций

```gendiff -h```

##### Сравниваем данные, расположенные в двух файлах

По умолчанию используется форматтер stylish

``gendiff tests/fixtures/nest_f1.json tests/fixtures/nest_f2.json``

[![asciicast](https://asciinema.org/a/PV7Nfp9UE6FHwsQaSoYLg5CFx.svg)](https://asciinema.org/a/PV7Nfp9UE6FHwsQaSoYLg5CFx)

##### Сравнение также доступно при помощи форматтера plain
   
Он выводит результат в виде текста

`gendiff tests/fixtures/nest_f1.json tests/fixtures/nest_f2.yaml -f plain`
 
[![asciicast](https://asciinema.org/a/77V0zuNaM2FuKO8aFRwShTjgy.svg)](https://asciinema.org/a/77V0zuNaM2FuKO8aFRwShTjgy)

##### Форматтер json серилизует, то есть упаковывает результат сравнения данных в формат json

Это необходимо, например, для интеграции с другими программами

`gendiff tests/fixtures/nest_f1.yml tests/fixtures/nest_f2.yaml -f json`

[![asciicast](https://asciinema.org/a/Y47ADSZlINtlmFVYiylHd40qd.svg)](https://asciinema.org/a/Y47ADSZlINtlmFVYiylHd40qd)

---
