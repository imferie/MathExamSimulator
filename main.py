from random import randint
import streamlit as st
import pandas as pd

st.set_page_config(layout="centered", page_icon="📄", page_title="Сессия")
st.header('📄 Генератор билетов')

geom = [
    '1. Группы преобразований и движений плоскости.',
    '2. Неподвижные точки движения. Теорема о движении с двумя неподвижными точками.',
    '3. Теорема о представлении.',
    '4. Свойство подвижности. Теорема Шаля-Даламбера.',
    '5. Гомотетия и ее свойства.',
    '6. Теорема о представлении подобия. Группа подобий.',
    '7. Прямая Эйлера.',
    '8. Окружность девяти точек.',
    '9. Параллельные прямые.',
    '10. Скрещивающиеся прямые.',
    '11. Параллельность прямой и плоскости.',
    '12. Параллельность двух плоскостей.',
    '13. Перпендикулярность прямой и плоскости.',
    '14. Перпендикуляр из точки к плоскости. Теорема о 3П.',
    '15. Графы на плоскости и сфере. Формула Эйлера о графах.',
    '16. Теорема Эйлера о правильных многогранниках.',
    '17. Направление на плоскости и в пространстве.',
    '18. Направленные отрезки и векторы. Сложение векторов.',
    '19. Умножение вектора на число.',
    '20. Коллинеарность, компланарность. Базис плоскости и пр-ва.',
    '21. Векторное уравнение прямой и плоскости. Параметрическое и каноническое задание прямой в пространстве. '
    'Координатное уравнениепрямой в плоскости.',
    '22. Линейные множества. Координатное уравнение плоскости в произвольной системе координат.',
    '23. Проекция одного вектора на другой и ее свойства.',
    '24. Скалярное произведение и его свойства.',
    '25. Вычисление скалярного произведения в ОНБ. Координатное уравнение сферы.',
    '26. Нормаль к плоскости.',
    '27. Координатное уравнение плоскости в декартовой системе координат. Вычисление расстояния от точки до плоскости.',
]

algebra = [
    '1. Предмет комбинаторики. Правила умножения и сложения (показать на примерах). Факториал. Формулы числа '
    'перестановок, сочетаний, размещений(с доказательством).',
    '2. Бинома Ньютона. Свойства биномиальных коэффициентов (с доказательством). Треугольник Паскаля.',
    '3. Вероятностное пространство. Элементарные и сложные события. Вероятность (определение). Несовместные события; '
    'сумма событий (определение). Вероятность суммы несовместных событий.',
    '4. Произведение событий (определение). Независимость событий (определение). Вероятность суммы событий (с '
    'доказательством и примером).',
    '5. Числовая функция (определение). Способы задания числовых функций. График функции. Ограниченность, '
    'монотонность, четность, нечетность, периодичность функции (определения). Связь между свойствами функции и '
    'свойствами ее графика.',
    '6. Функции y = kx + b, y = |x|, y = ax^2 + bx + c (a!=0), y = k / x (k != 0), их свойства и графика',
    '7. Деление многочленов с остатком (с доказательством).',
    '8. Теорема Безу и следствие из нее (с доказательством). Схема Горнера.',
    '9. Теорема о рациональных корнях многочлена с целыми коэффициентами (с доказательством).',
    '10. Кратные корни многочленов. Обобщенная теорема Виета.',
    '11. Многочлен от нескольких переменных; симметрический многочлен; элементарные симметрические многочлены ('
    'определения). Теорема о  представимости симметрического многочлена в виде многочлена от элементарных '
    'симметрических многочленов (без доказательства, показать на примере).',
    '12. Обобщенный угол. Радианное измерение углов. Тригонометрическая окружность. Синус и косинус числа и их '
    'простейшие свойства (с доказательством).',
    '13. Тангенс и котангенс, их геометрическое изображение и простейшие свойства (с доказательством).',
    '14. Основное тригонометрическое тождество. Арксинус, арккосинус, арктангенс, арккотангенс и решение простейших '
    'тригонометрических уравнений.',
    '15. Синус, косинус и тангенс суммы и разности (с доказательством).',
    '16. Формулы приведения (доказательство одной из них по выбору экзаменатора).',
    '17. Формулы двойного угла для синуса, косинуса и тангенса (с доказательством).',
    '18. Формулы половинного угла (понижения степени, удвоения аргумента) для синуса, косинуса и тангенса (с '
    'доказательством).',
    '19. Выражение тригонометрических функций через тангенс половинного аргумента (с доказательством).',
    '20. Формулы преобразования произведения синусов, косинусов, синуса и косинуса в сумму (с доказательством).',
    '21. Формулы преобразования суммы синусов/косинусов в произведение (с доказательством). Преобразование в '
    'произведение суммы синуса и косинуса (показать на примере).',
    '22. Функция f(x) = sin(x), f(x) = cos(x) их свойства и график.',
    '23. Функция f(x) = tg(x), f(x) = ctg(x) их свойства и график.',
    '22. Функция f(x) = arcsin(x), f(x) = arccos(x) их свойства и график. Тождества arcsin(-a) = ..., arccos(-a) = '
    '..., (с доказательствами)',
    '23. Функция f(x) = arctg(x), f(x) = arcctg(x) их свойства и график. Тождества arctg(-a) = ..., arcctg(-a) = ..., '
    '(с доказательствами)',
]

element = st.text('Нажмите кнопку, чтобы сгненерировать')
col1, col2, col3 = st.columns(3)
col2.empty()
first_number, second_number = randint(0, len(geom) - 1), randint(0, len(algebra) - 1)
if col2.button('Сгенерировать билет'):
    element.write(geom[first_number] + '\n' + algebra[second_number])
