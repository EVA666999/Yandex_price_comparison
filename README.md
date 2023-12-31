<h1>Yandex_price_comparison</h1>
<p>Добро пожаловать в репозиторий проекта Yandex_price_comparison!</p>
<p>Это API сервис, который по запросу пользователя выдаёт товар с минимальной ценой на площадке Яндекс.Маркет. В этом проекте я применил следующие технологии и концепции:</p>

<h3>Как всё рабоатет?</h3>
<ul>
  <li>есть API ссылка в которой вставляются ныжные переменные для запроса <pre>f'https://api.partner.market.yandex.ru/v2/models?query={query}&regionId={region_id}&page={page}'</pre></li>
  <li>query это название товара, region_id номер региона который можно узнать через гет запрос и page это количество обрабатываемых страниц</li>
  <li>Код собирает данные по запросу query со всех страниц с помошью бесконечного цыкла while True и базового случая if page > 50: break так как страниц всего 50</li>
  <li>Дальше переменной results будет находиться список всех значений, связанных с ключом 'models' я вставил это в новый список total_results += results</li>
  <li>Отфильтровал новый список так что бы значение query было в поле name для модели <pre> filtered_results = [model for model in total_results if query_lower in model.get('name').lower()]</pre></li>
  <li>И получил минимальную цену товара и ссылку на него с помощью цыкла for </li>
</ul>

<h3>Технологии 🛠</h3>
<ul>
  <li>Python 3.9</li>
  <li>Django 2.2.19</li>
  <li>HTML</li>
  <li>CSS</li>
  <li>requests</li>
  <li>API</li>
</ul>

<h1>Запуск проекта в dev-режиме</h1>
<h3>Чтобы запустить проект в режиме разработки, следуйте инструкциям ниже:</h3>
<h4><b>1.</b>Установите и активируйте виртуальное окружение</h4>
<pre>
<code>python -m venv venv</code>
</pre>
<pre>
<code>source venv/Scripts/activate</code>
</pre>
<h4><b>2.</b>Установите зависимости из файла requirements.txt</h4>
<pre>
<code>pip install -r requirements.txt</code>
</pre>
<h4><b>3.</b>В файле test_api_key.txt находится тестовый API яндекс токен, его нужно вставить в переменную token в функцие search_view</h4>
<pre>
  def search_view(request):
    if request.method == 'POST':
        query = request.POST.get('query', '')
        region_id = '2'
        token = # Тут должен быть токен
</pre>
<h4><b>3.</b>В папке с файлом manage.py выполните следующую команду</h4>
<pre>
<code>python manage.py runserver</code>
</pre>
<h3>Авторы</h3>

- [@Василе](https://www.github.com/EVA666999)


<p>PS. Так как Яндекс не предоставил мне полный доступ к API у программы есть ограничение на количество запросов из-за этого точная минимальная цена может быть неверной, когда мне предоставят полный доступ я это исправлю.</p>
