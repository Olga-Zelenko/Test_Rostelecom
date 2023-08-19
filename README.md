<h1 align="center">Тестирование страниц авторизации и регистрации сайта <a href="https://b2c.passport.rt.ru" target="_blank">Ростелеком</a> 
<img src="https://38.img.avito.st/image/1/H1-pk7aBs7bfNkGwm_soflAwt7ALMrOwbFO3sN82QbAfNL-yHzKz8g" height="32"/></h1>
<h3 align="center">Выполнил: Зеленко Ольга Петровна</h3>

Объект тестирования: https://b2c.passport.rt.ru
Тестирование осуществлялось в соответствии с [требованиями](https://docs.google.com/document/d/1ZxIwNo3wYSuY9GQNEBmWLzo-TsrqX2mz/edit?usp=sharing&ouid=108178557176992179443&rtpof=true&sd=true) предоставленными заказчиком.

Для выполнения тестирования было использовано следующее ПО:
<ul>
  <li>Windows 10 Pro, вер.22H2, сборка ОС 19045.3208</li>
  <li>PyCharm 2022.3.2 (Community Edition)</li>
  <li>Google Chrome Версия 115.0.5790.171 (Официальная сборка), (64 бит)</li>
  <li>Microsoft Office Версия 1908</li>
</ul>

<h3 align="center">Методы и виды тестирования, применённые при разработке проекта</h3>

Для разработки тест-кейсов применены:
<ul>
  <li>метод "черного ящика"</li>
  <li>функциональное тестирование</li>
  <li>UX тестирование</li>
</ul>
Использованы следующие техники тест дизайна: 
<ul>
  <li>диаграмма состояний и переходов</li>
  <li>классы эквивалентности</li>
  <li>граничные значения и попарное тестирование</li>
</ul>

Разработка проекта автотестирования выполнена по паттерну PageObject. Для разработки автотестов применялись библиотеки pytest, Selenium и pytest-selenium. Использовались фикстуры, фикстуры параметризации, различные способы описания локаторов (СSS_SELECTOR, XPATH, ID, CLASS_NAME, NAME). 

Для запуска проекта используется Web driver для GoogleChrome с автоматической устновкой driver при помощи библиотеки chromedriver-autoinstaller==0.6.2.
Для определения локаторов использовались следующие инструменты: DevTools, Element Locator. 

Перед запуском тестов требуется установить необходимые библиотеки командой:
pip install -r requirements.txt


