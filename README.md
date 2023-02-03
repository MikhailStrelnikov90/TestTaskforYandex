# Тестовое задание для Яндекс.Практикума

### Задача. Необходимо написать функцию расчёта стоимости доставки.

Стоимость рассчитывается в зависимости от:

*расстояния до пункта назначения:*

- более 30 км: +300 рублей к доставке;
- до 30 км: +200 рублей к доставке;
- до 10 км: +100 рублей к доставке;
- до 2 км: +50 рублей к доставке;

*габаритов груза:*

- большие габариты: +200 рублей к доставке;
- маленькие габариты: +100 рублей к доставке;

*хрупкости груза.* Если груз хрупкий — +300 рублей к доставке. Хрупкие грузы нельзя возить на расстояние более 30 км;

*загруженности службы доставки*. Стоимость умножается на коэффициент доставки:

- очень высокая загруженность — 1.6;
- высокая загруженность — 1.4;
- повышенная загруженность — 1.2;
- во всех остальных случаях коэффициент равен 1.

Минимальная сумма доставки — 400 рублей. Если сумма доставки меньше минимальной, выводится минимальная сумма.

На входе функция получает расстояние до пункта назначения, габариты, информацию о хрупкости, загруженность службы на текущий момент. На выходе пользователь получает стоимость доставки.

Для выполнения тестов необходимо загрузить фреймворк pytest (pip install pytest)