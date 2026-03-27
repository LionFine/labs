# Лабораторная работа №4
## Вариант 16. Выделение контуров на изображении

Использована формула варианта 16:
- `Gx = |I - D_h(I)|`
- `Gy = |I - D_v(I)|`
- `G = |Gx| + |Gy|`

где `D_h` и `D_v` — морфологические дилатации по горизонтальному и вертикальному направлениям с окном `3x3`.

Порог бинаризации итогового градиента: `T = 80`.

### Изображение 0

| Исходное | Полутоновое | Бинарное G |
|:--------:|:-----------:|:----------:|
| ![src0](lab4/images/0.png) | ![gray0](lab4/images/grayscale/0.png) | ![gbin0](lab4/images/G_binary/0.png) |

| Gx | Gy | G |
|:--:|:--:|:--:|
| ![gx0](lab4/images/Gx/0.png) | ![gy0](lab4/images/Gy/0.png) | ![g0](lab4/images/G/0.png) |

### Изображение 1

| Исходное | Полутоновое | Бинарное G |
|:--------:|:-----------:|:----------:|
| ![src1](lab4/images/1.png) | ![gray1](lab4/images/grayscale/1.png) | ![gbin1](lab4/images/G_binary/1.png) |

| Gx | Gy | G |
|:--:|:--:|:--:|
| ![gx1](lab4/images/Gx/1.png) | ![gy1](lab4/images/Gy/1.png) | ![g1](lab4/images/G/1.png) |

### Изображение 2

| Исходное | Полутоновое | Бинарное G |
|:--------:|:-----------:|:----------:|
| ![src2](lab4/images/2.png) | ![gray2](lab4/images/grayscale/2.png) | ![gbin2](lab4/images/G_binary/2.png) |

| Gx | Gy | G |
|:--:|:--:|:--:|
| ![gx2](lab4/images/Gx/2.png) | ![gy2](lab4/images/Gy/2.png) | ![g2](lab4/images/G/2.png) |

### Изображение 3

| Исходное | Полутоновое | Бинарное G |
|:--------:|:-----------:|:----------:|
| ![src3](lab4/images/3.png) | ![gray3](lab4/images/grayscale/3.png) | ![gbin3](lab4/images/G_binary/3.png) |

| Gx | Gy | G |
|:--:|:--:|:--:|
| ![gx3](lab4/images/Gx/3.png) | ![gy3](lab4/images/Gy/3.png) | ![g3](lab4/images/G/3.png) |

### Вывод

Построены карты `Gx`, `Gy`, итоговый градиент `G` и бинаризованные контуры для варианта 16 на основе направленной морфологической дилатации.
