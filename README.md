# Predictor
Simple GUI predictor uses model PKL dump

Приложение, использующие дамп обученной модели из проекта обучения и выбора моделей:
https://github.com/Arthur-Frank/ebw_prediction_model

Интерфейс приложения реализован с библиотекой tkinter 

Использование:
 - запустите код
 - в появившемся окне введите 4 цифры.
 - нажмите кнопку "Submit" для сохранения введённых данных. Проверьте, что данные введены, верно - ниже окна ввода отображаются введённые значения
 - нажмите кнопку "Predict" для получения предсказания 
 
 Приложение использует PKL файл - дамп модели обученной на датасете зависимости ширины и глубины сварного шва от 4х параметров сварки.