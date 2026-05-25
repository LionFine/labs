# Лабораторная работа №6
## Вариант 3. Сегментация текста

Работа выполнена для выбранного в лабораторной №5 алфавита: глаголица.

Исходная строка: `ⰎⰣⰁⰎⰣ ⰕⰅⰁⰡ`. Монохромная версия сохранена в [lab6/images/phrase.bmp](lab6/images/phrase.bmp).

| Строка | Вертикальный профиль | Горизонтальный профиль |
|:------:|:--------------------:|:----------------------:|
| ![phrase](lab6/images/phrase.png) | ![phrase_x](lab6/images/phrase_profile_x.png) | ![phrase_y](lab6/images/phrase_profile_y.png) |

### Сегментация

Символы выделены по вертикальному профилю строки с объединением коротких внутренних разрывов. Ниже показаны найденные прямоугольники.

![segmented](lab6/images/phrase_segmented.png)

Найдено сегментов: `9`. Ожидалось символов без пробелов: `9`.

| № | Ожидаемый символ | Вырезанный сегмент |
|:--:|:----------------:|:------------------:|
| 1 | `Ⰾ` | ![segment_1](lab6/images/segments/01.png) |
| 2 | `Ⱓ` | ![segment_2](lab6/images/segments/02.png) |
| 3 | `Ⰱ` | ![segment_3](lab6/images/segments/03.png) |
| 4 | `Ⰾ` | ![segment_4](lab6/images/segments/04.png) |
| 5 | `Ⱓ` | ![segment_5](lab6/images/segments/05.png) |
| 6 | `Ⱅ` | ![segment_6](lab6/images/segments/06.png) |
| 7 | `Ⰵ` | ![segment_7](lab6/images/segments/07.png) |
| 8 | `Ⰱ` | ![segment_8](lab6/images/segments/08.png) |
| 9 | `Ⱑ` | ![segment_9](lab6/images/segments/09.png) |

### Профили символов алфавита

#### Ⰰ (U2C00)

| Эталон | Профиль X | Профиль Y |
|:------:|:---------:|:---------:|
| ![U2C00](lab6/images/alphabet/U2C00.png) | ![x_U2C00](lab6/images/alphabet_profiles_x/U2C00.png) | ![y_U2C00](lab6/images/alphabet_profiles_y/U2C00.png) |

#### Ⰱ (U2C01)

| Эталон | Профиль X | Профиль Y |
|:------:|:---------:|:---------:|
| ![U2C01](lab6/images/alphabet/U2C01.png) | ![x_U2C01](lab6/images/alphabet_profiles_x/U2C01.png) | ![y_U2C01](lab6/images/alphabet_profiles_y/U2C01.png) |

#### Ⰲ (U2C02)

| Эталон | Профиль X | Профиль Y |
|:------:|:---------:|:---------:|
| ![U2C02](lab6/images/alphabet/U2C02.png) | ![x_U2C02](lab6/images/alphabet_profiles_x/U2C02.png) | ![y_U2C02](lab6/images/alphabet_profiles_y/U2C02.png) |

#### Ⰳ (U2C03)

| Эталон | Профиль X | Профиль Y |
|:------:|:---------:|:---------:|
| ![U2C03](lab6/images/alphabet/U2C03.png) | ![x_U2C03](lab6/images/alphabet_profiles_x/U2C03.png) | ![y_U2C03](lab6/images/alphabet_profiles_y/U2C03.png) |

### Вывод

Построены горизонтальный и вертикальный профили строки, по профилю выделены символы и сохранены их обрамляющие прямоугольники и вырезанные изображения.
