### Hexlet tests and linter status:

[![hexlet-check](https://github.com/ilia-rassolov/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/ilia-rassolov/python-project-50/actions/workflows/hexlet-check.yml)

[![my-check](https://github.com/ilia-rassolov/python-project-50/actions/workflows/my-check.yml/badge.svg)](https://github.com/ilia-rassolov/python-project-50/actions/workflows/my-check.yml)

[![Maintainability](https://api.codeclimate.com/v1/badges/a723eafeff9ce50f593f/maintainability)](https://codeclimate.com/github/ilia-rassolov/python-project-50/maintainability)

[![Test Coverage](https://api.codeclimate.com/v1/badges/a723eafeff9ce50f593f/test_coverage)](https://codeclimate.com/github/ilia-rassolov/python-project-50/test_coverage)


Это мой второй учебный проект на Hexlet. Он называется **Вычислитель отличий**

1. Команда **gendiff -h** выводит описание решаемой задачи и список опций

2. **gendiff gendiff/json_files/file1.json gendiff/json_files/file2.json** 

   сравнивает данные в файлах формата .json, расположенные в аргументах (пути 2-х файлов)


[![asciicast](https://asciinema.org/a/OHyPacXfjy2BaJmTb3GngHDX9.svg)](https://asciinema.org/a/OHyPacXfjy2BaJmTb3GngHDX9)

3. **gendiff gendiff/yaml_files/file1.yaml gendiff/yaml_files/file.yml** 

   сравнивает данные в файлах формата .yaml .yml, но только если данные простые - без вложенности


[![asciicast](https://asciinema.org/a/4gPnydJ1xEsY6mBPO4adSVsSx.svg)](https://asciinema.org/a/4gPnydJ1xEsY6mBPO4adSVsSx)

4. **gendiff tests/fixtures/nest_f1.yaml tests/fixtures/nest_f2.yaml -f stylish** 

   сравнивает данные с вложенностью, используется форматтер stylish, он используется по умолчанию


[![asciicast](https://asciinema.org/a/rgxkBHia0fNGSpttZ1qiYtMan.svg)](https://asciinema.org/a/rgxkBHia0fNGSpttZ1qiYtMan)

5. **gendiff tests/fixtures/nest_f1.yaml tests/fixtures/nest_f2.yaml -f plain** 

   форматтер plain выводит сравнение данных в виде текста


[![asciicast](https://asciinema.org/a/TVdbwB2Al7Tb5yk29XjSAm515.svg)](https://asciinema.org/a/TVdbwB2Al7Tb5yk29XjSAm515)

6. **gendiff tests/fixtures/nest_f1.yaml tests/fixtures/nest_f2.yaml -f json** 

   форматтер json серилизует (упаковывает) сравнение данных в формат json
   это необходимо, например, для интеграции с другими программами


[![asciicast](https://asciinema.org/a/TVdbwB2Al7Tb5yk29XjSAm515.svg)](https://asciinema.org/a/TVdbwB2Al7Tb5yk29XjSAm515)


