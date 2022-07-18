This is Coinmarketcap portfolio parser

by [t.me/cryptochy](https://t.me/cryptochy)

Parsing any token transactions to dataframe

## Requirements

You need a numpy and beautifulsoup:

    pip install numpy
    pip install beautifulsoup4


## English instruction

1. Select token in your portfolio
2. Click right mouse button and select "Inspect"

![Copy element](https://user-images.githubusercontent.com/48959405/179366380-313f016f-5a35-4879-91fa-25823c6e51fa.png)

3. Copy element body (on image)
4. Paste in "source.txt"
5. Run script

If not working:
- Try changing CSS classes: select element with date on your webpage, select "Inspect", copy CSS class (looks like "sc-1eb5slv-0 <class>", this text after space is your class) and paste in "dates_style" field
- Try this at last order: Do same thing with amount field (looks like "+100 USDT" and has red/green color), has the class "sc-1eb5slv-0 <class>", copy class for green and red color and past in parentheses, example: "sc-1eb5slv-0 (iRvyUh|hUkJcr)"
- Try changing e_const from 0 to 4 (typically is 4 or 2)
- If not working after all, ask for help in out telegram chat: @cryptochy2


## Русская инструкция

0. Подпишитесь на [Crypto Chyvak](https://t.me/cryptochy)
1. Выберите токен в вашем портфеле (Смените язык Coinmarketcap на английский!)
2. Нажмите в любом месте правой кнопкой мыши и нажмите "Изучить код"

![Copy element](https://user-images.githubusercontent.com/48959405/179366380-313f016f-5a35-4879-91fa-25823c6e51fa.png)

3. Нажмите "Скопировать элемент" body (на картинке)
4. Вставьте в файл "source.txt"
5. Запустите код

Если не работает:
- Попробуйте изменить CSS класс: выберите элемент с датой на странице портфеля, нажмите "Изучить код", скопируйте CSS класс (выглядит как "sc-1eb5slv-0 <класс>", то что находится после пробела и надо копировать) и встаьте в поле "dates_style"
- Это пробуйте в последнию очередь: Повторите тоже самое с полем количества (выглядит как "+100 USDT" и зелёного/красного цвета), имеет класс "sc-1eb5slv-0 <класс>", скопируйте класс для зеленого и красного цвета и вставьте в скобки с разделителем, пример: "sc-1eb5slv-0 (iRvyUh|hUkJcr)"
- Попробуйте изменить e_const с 0 до 4 (обычно это 4 или 2)
- Если не работает после всего, спросите в нашем телеграм чате: @cryptochy2


## Инструкция по обработке данных

Вывод должен быть в таком формате:

    Jul 8, 2022 ; -16 ; 353.0 
    Jul 7, 2022 ; 0 ; 369.0 
    Jul 6, 2022 ; 0 ; 369.0
Если что-то не так, то пишите мне в телеграм: @ruslaneum

1. Копируем этот текст и вставляем в гугл таблицы
2. Далее выбираем "Данные" > "Разделить текст на колонки"

![Выбираем это](https://user-images.githubusercontent.com/48959405/179367023-895c9467-e3f7-4c31-ad98-2f6c83ace7ea.png)

3. В качестве разделителя выбираем точку с запятой "Semicolon"
4. Готово, теперь можете строить себе графики (для постройки графиков есть много 2 минутных гайдов) и анализировать всё что хотите
