# Массовая загрузка набора данных Open Images Dataset V6

![PyPI](https://img.shields.io/pypi/v/oidv6)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/oidv6)
![PyPI - Implementation](https://img.shields.io/pypi/implementation/oidv6)
![PyPI - Status](https://img.shields.io/pypi/status/oidv6)
![PyPI - License](https://img.shields.io/pypi/l/oidv6)

| [История релизов](https://github.com/DmitryRyumin/OIDv6/blob/master/NOTES_RU.md) | [Документация на английском](https://github.com/DmitryRyumin/OIDv6/blob/master/README.md) |
| --- | --- |

## Установка

```shell script
pip install oidv6
```

## Обновление

```shell script
pip install --upgrade oidv6
```

## Зависимости

| Пакеты | Минимальная версия | Текущая версия |
| ------ | ------------------ | -------------- |
`requests` | `2.23.0` | ![PyPI](https://img.shields.io/pypi/v/requests) |
`numpy` | `1.18.4` | ![PyPI](https://img.shields.io/pypi/v/numpy) |
`pandas` | `1.0.4` | ![PyPI](https://img.shields.io/pypi/v/pandas) |
`progressbar2` | `3.51.3` | ![PyPI](https://img.shields.io/pypi/v/progressbar2) |
`opencv-contrib-python` | `4.2.0.34` | ![PyPI](https://img.shields.io/pypi/v/opencv-contrib-python) |
`awscli` | `1.18.69` | ![PyPI](https://img.shields.io/pypi/v/awscli) |

## Полезные ресурсы

- [Официальный сайт Open Images Dataset V6](https://storage.googleapis.com/openimages/web/index.html)
- [Список всех классов, которые возможно загрузить](https://github.com/DmitryRyumin/OIDv6/blob/master/oidv6/classes.txt)

## [Класс для массовой загрузки набора данных Open Images Dataset V6 (OIDv6)](https://github.com/DmitryRyumin/OIDv6/blob/master/oidv6/OIDv6.py)

### Аргументы командной строки

| Аргумент&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Тип | Описание | Допустимые значения |
| -------------------------- | ---  | -------- | ------------------- |
| command | str | Команда загрузки | `downloader` |
| command | str | Язык<br>`Значение по умолчанию: en` | `en`<br>`ru` |
| --dataset | str | Корневая директория для сохранения OIDv6<br>`Значение по умолчанию: OIDv6` | - |
| --type_data | str | Набор данных<br>`Значение по умолчанию: train` | `train`<br>`validation`<br>`test`<br>`all` |
| --classes | str | Последовательность названий классов или текстовый файл | - |
| --limit | int | Лимит загрузки изображений<br>`Значение по умолчанию: 0 (нет лимита)` | От `0` до `∞` |
| --multi_classes | bool | Загрузка классов в одну директорию | Без значений |
| --yes | bool | Автоматическая загрузка служебных файлов | Без значений |
| --no_labels | bool | Автоматическая загрузка служебных файлов | Без значений |
| --hide_metadata | bool | Вывод метаданных | Без значений |
| --no_clear_shell | bool | Не очищать консоль перед выполнением | Без значений |

<h4 align="center"><span style="color:#EC256F;">Примеры</span></h4>

---

>  **Примечание!** Классы, которые составлены из нескольких слов, следует обрамлять кавычками (если они переданы напрямую в командную строку). Например: `"Organ (Musical Instrument)"`

---

1. Загрузка классов (`apple`, `banana`, `Kitchen & dining room table`) из наборов `train`, `validation` и `test` с метками в полуавтоматическом режиме и лимитом изображений = `4` (Язык: `Русский`)

    > CMD
    >
    > ```shell script
    > oidv6 downloader ru --dataset путь_к_директории --type_data all --classes apple banana "Kitchen & dining room table" --limit 4
    > ```

2. Загрузка тренировочных классов (`cat`, `dog`) из набора `train` с метками в автоматическом режиме и лимитом изображений = `10` (Язык: `Английский`)

    > CMD
    >
    > ```shell script
    > oidv6 downloader en --dataset путь_к_директории --type_data train --classes Cat dOg --limit 10 --yes
    > ```

3.  Загрузка валидационных классов (см. текстовый файл) из набора `validation` с метками в автоматическом режиме и лимитом изображений = `10` (Язык: `Английский`)

    > Текстовый файл
    >
    > ```text
    > person
    > Organ (Musical Instrument)
    > ```

    > CMD
    >
    > ```shell script
    > oidv6 downloader --dataset путь_к_директории --type_data validation --classes путь_к_текстовому_файлу --limit 10 --yes
    > ```

4. Мультизагрузка классов (`axe`, `calculator`) из наборов `train`, `validation` и `test` с метками в автоматическом режиме и лимитом изображений = `12` (Язык: `Английский`)

    > CMD
    >
    > ```shell script
    > oidv6 downloader --dataset путь_к_директории --type_data all --classes axe calculator --limit 12 --multi_classes --yes
    > ```