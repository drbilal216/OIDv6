#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Массовая загрузка набора данных Open Images Dataset V6

python oidv6/samples/run.py <command> <command> --classes названия_классов_или_текстовый_файл
    [--dataset Dataset --type_data train --limit 0 --multi_classes --yes --no_labels --hide_metadata --no_clear_shell]
"""


# ######################################################################################################################
# Импорт необходимых инструментов
# ######################################################################################################################
from datetime import datetime  # Работа со временем
from types import ModuleType  # Проверка объектов на модуль

# Персональные
import oidv6  # Массовая загрузка набора данных Open Images Dataset V6

from oidv6.OIDv6 import OIDv6  # Массовая загрузка набора данных Open Images Dataset V6
from oidv6.modules.trml.shell import Shell  # Работа с Shell


# ######################################################################################################################
# Сообщения
# ######################################################################################################################
class Messages(OIDv6):
    """Класс для сообщений"""

    # ------------------------------------------------------------------------------------------------------------------
    # Конструктор
    # ------------------------------------------------------------------------------------------------------------------

    def __init__(self):
        super().__init__()  # Выполнение конструктора из суперкласса

        self._oidv6 = self._('{}{}OIDv6 - Массовая загрузка набора данных Open Images Dataset V6 ...{}')


# ######################################################################################################################
# Выполняем только в том случае, если файл запущен сам по себе
# ######################################################################################################################
class Run(Messages):
    """Класс для массовой загрузки набора данных Open Images Dataset V6"""

    # ------------------------------------------------------------------------------------------------------------------
    # Конструктор
    # ------------------------------------------------------------------------------------------------------------------

    def __init__(self):
        super().__init__()  # Выполнение конструктора из суперкласса

    # ------------------------------------------------------------------------------------------------------------------
    #  Внутренние методы
    # ------------------------------------------------------------------------------------------------------------------

    # Построение аргументов командной строки
    def _build_args(self, conv_to_dict = True):
        """
        Построение аргументов командной строки

        ([bool]) -> None or dict

        Аргументы:
            conv_to_dict - Преобразование списка аргументов командной строки в словарь

        Возвращает: dict если парсер командной строки окончательный, в обратном случае None
        """

        super().build_args(False)  # Выполнение функции из суперкласса

        # Добавление аргументов в парсер командной строки
        self._ap.add_argument('command', metavar = '<command> downloader',
                              choices = self.commands, help = self._('Команда загрузки'))

        self._ap.add_argument('--dataset', required = False, metavar = self._('путь_к_директории'),
                              default = self.dir,
                              help = self._('Корневая директория для сохранения OIDv6, значение по умолчанию:') +
                              ' %(default)s')
        self._ap.add_argument('--type_data', required = False, choices = list(self.type_data.keys()) + ['all'],
                              default = 'train', metavar = 'train, validation, test ' + self._('или') + ' all',
                              help = self._('Набор данных, значение по умолчанию:') + ' %(default)s')
        self._ap.add_argument('--classes', required = False, nargs = '+', metavar = self._('название_класса'),
                              help = self._('Последовательность названий классов или текстовый файл'))
        self._ap.add_argument('--limit', required = False, default = 0, type = int, metavar = self._('целое_число'),
                              help = self._('Лимит загрузки изображений, значение по умолчанию:') +
                              ' %(default)s (' + self._('нет лимита') + ')')
        self._ap.add_argument('--multi_classes', required = False, action = 'store_true',
                              help = self._('Загрузка классов в одну директорию'))

        self._ap.add_argument('--yes', required = False, action = 'store_true',
                              help = self._('Автоматическая загрузка служебных файлов'))
        self._ap.add_argument('--no_labels', required = False, action = 'store_true',
                              help = self._('Не формировать метки'))
        self._ap.add_argument('--hide_metadata', required = False, action = 'store_true',
                              help = self._('Вывод метаданных'))
        self._ap.add_argument('--no_clear_shell', required = False, action = 'store_false',
                              help = self._('Не очищать консоль перед выполнением'))

        # Преобразование списка аргументов командной строки в словарь
        if conv_to_dict is True:
            args, _ = self._ap.parse_known_args()
            return vars(args)  # Преобразование списка аргументов командной строки в словарь

    # ------------------------------------------------------------------------------------------------------------------
    #  Внешние методы
    # ------------------------------------------------------------------------------------------------------------------

    # Запуск
    def run(self, metadata = oidv6, out = True):
        """
        Запуск

        ([module, module, bool, bool]) -> None

        Аргументы:
            out - Печатать процесс выполнения
        """

        # Проверка аргументов
        if type(out) is not bool or not isinstance(metadata, ModuleType):
            # Вывод сообщения
            if out is True:
                print(self._invalid_arguments.format(
                    self.red, datetime.now().strftime(self._format_time),
                    self.end, __class__.__name__ + '.' + self.run.__name__
                ))

            return False

        self._args = self._build_args()  # Построение аргументов командной строки

        self.clear_shell(self._args['no_clear_shell'])  # Очистка консоли перед выполнением

        # Приветствие
        Shell.add_line()  # Добавление линии во весь экран
        print(self._oidv6.format(self.bold, self.blue, self.end))
        Shell.add_line()  # Добавление линии во весь экран

        # Запуск
        if self._args['hide_metadata'] is False:
            print(self._metadata.format(
                datetime.now().strftime(self._format_time),
                metadata.__author__,
                metadata.__email__,
                metadata.__maintainer__,
                metadata.__version__
            ))

            Shell.add_line()  # Добавление линии во весь экран

        self.download(self._args, out)


def main():
    run = Run()

    run.run()


if __name__ == "__main__":
    main()
