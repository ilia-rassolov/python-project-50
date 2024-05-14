---

### Hexlet tests and linter status

[![hexlet-check](https://github.com/ilia-rassolov/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/ilia-rassolov/python-project-50/actions/workflows/hexlet-check.yml)
[![my-check](https://github.com/ilia-rassolov/python-project-50/actions/workflows/my-check.yml/badge.svg)](https://github.com/ilia-rassolov/python-project-50/actions/workflows/my-check.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/a723eafeff9ce50f593f/maintainability)](https://codeclimate.com/github/ilia-rassolov/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/a723eafeff9ce50f593f/test_coverage)](https://codeclimate.com/github/ilia-rassolov/python-project-50/test_coverage)

---

### Это мой второй учебный проект на Hexlet. Он называется **"Вычислитель отличий"**

Это приложение позволяет сравнивать данные в двух файлах, доступные форматы для сравнения **.json**, **.yaml** или **.yml**

---

## Установка проекта, запуск проверок

Требования:
Для установки проекта требуются установленные CPython не ниже 3.10 и poetry не ниже 1.2.0

# Клонируем пакет:

`git clone git@github.com:ilia-rassolov/python-project-50.git`

# Из новой директории python-project-50 установить пакет командой

`poetry install`

# Можно запустить проверку кода линтером и тестами

`make linter`
`make test`

---

## Приложение готово к работе.

Эта команда выводит описание решаемой задачи и список опций

```gendiff -h```

## Сравниваем данные, расположенные в 2-х файлах

По умолчанию используется форматтер stylish

``gendiff tests/fixtures/nest_f1.json tests/fixtures/nest_f2.yaml``

[![asciicast](https://asciinema.org/a/9PXyXjCfNhSfwkhR0EewupDAr.svg)](https://asciinema.org/a/9PXyXjCfNhSfwkhR0EewupDAr)

## Сравнение также доступно при помощи форматтера plain
   
Он выводит результат в виде текста

`gendiff tests/fixtures/nest_f1.yaml tests/fixtures/nest_f2.yaml -f plain`
 
[![asciicast](https://asciinema.org/a/FBGvehv5sugAveyKEuXzz0Ssd.svg)](https://asciinema.org/a/FBGvehv5sugAveyKEuXzz0Ssd)

## Форматтер json серилизует, то есть упаковывает результат сравнения данных в формат json

Это необходимо, например, для интеграции с другими программами

`gendiff tests/fixtures/nest_f1.yaml tests/fixtures/nest_f2.yaml -f json`

[![asciicast](https://asciinema.org/a/2peFrQevgvdhmFVzzZDWG8zsk.svg)](https://asciinema.org/a/2peFrQevgvdhmFVzzZDWG8zsk)

---
