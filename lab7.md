# Лабораторная работа №7
## Вариант 3. Классификация на основе признаков

Классификация выполнена для глаголического алфавита из лабораторных №5-6.

Мера близости рассчитана как `1 / (1 + d)`, где `d` — евклидово расстояние в пространстве нормированных признаков: удельная масса, координаты центра тяжести и осевые моменты инерции.

### Распознавание основной строки

Размер шрифта: `72`.

Ожидалось: `ⰎⰣⰁⰎⰣⰕⰅⰁⰡ`
Распознано: `ⰎⰣⰁⰎⰣⰕⰅⰁⰡ`
Ошибок: `0`, точность: `100.00%`.

Гипотезы сохранены в [lab7/results/hypotheses_base.txt](lab7/results/hypotheses_base.txt).

| Строка | Сегментация |
|:------:|:------------:|
| ![phrase_base](lab7/images/base/phrase.png) | ![boxed_base](lab7/images/base/segmented.png) |

| № | Сегмент |
|:--:|:-------:|
| 1 | ![base_1](lab7/images/base/segments/01.png) |
| 2 | ![base_2](lab7/images/base/segments/02.png) |
| 3 | ![base_3](lab7/images/base/segments/03.png) |
| 4 | ![base_4](lab7/images/base/segments/04.png) |

### Распознавание эксперимента с другим размером шрифта

Размер шрифта: `80`.

Ожидалось: `ⰎⰣⰁⰎⰣⰕⰅⰁⰡ`
Распознано: `ⰎⰣⰁⰎⰣⰕⰅⰁⰡ`
Ошибок: `0`, точность: `100.00%`.

Гипотезы сохранены в [lab7/results/hypotheses_experiment.txt](lab7/results/hypotheses_experiment.txt).

| Строка | Сегментация |
|:------:|:------------:|
| ![phrase_experiment](lab7/images/experiment/phrase.png) | ![boxed_experiment](lab7/images/experiment/segmented.png) |

| № | Сегмент |
|:--:|:-------:|
| 1 | ![experiment_1](lab7/images/experiment/segments/01.png) |
| 2 | ![experiment_2](lab7/images/experiment/segments/02.png) |
| 3 | ![experiment_3](lab7/images/experiment/segments/03.png) |
| 4 | ![experiment_4](lab7/images/experiment/segments/04.png) |

### Вывод

Для каждого сегмента построен отсортированный список гипотез. Лучшие гипотезы собраны в строку и сравнены с исходной строкой, отдельно проверен вариант с изменённым размером шрифта.
