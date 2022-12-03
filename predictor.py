# Приложение, использующие дамп обученной модели из проекта обучения и выбора моделей
# https://github.com/Arthur-Frank/ebw_prediction_model
# интерфейс приложения реализован с библиотекой tkinter

# Библиотеки для чтения модели из дампа пикл
import pickle
import sklearn
import numpy as np


# Библиотека для создания веб-интерфейса
import tkinter as tk

# Чтение модели из дампа
with open ('ebw_model_predicter.pkl', 'rb') as file:
    model = pickle.load(file)

# Перевод текста в 2d numpy массив
def to_np_arr(text):
    np_2d_arr=np.array([[float(j) for j in i.split(',')] for i in text.splitlines()])
    return np_2d_arr

# Создание интрефейса ввода параметров для предсказания результата

# Кнопка обновления информации полученной из пользовательского ввода
def btn_submit(event):
    text1=entry.get()
    features['text']=text1

# Кнопка вызова образа модели для предсказания значения по введённым пользователям данным
def btn_predict(event):
    # Вызов предсказания из дампа модели происходит внутри метода, запускаемого при тригере эвента "Нажатие кнопки "Predict""
    result=model.predict(to_np_arr(features['text']))
    text2 = f'Глубина шва = {result[0][0]}, Ширина шва = {result[0][1]}'
    values['text']=(text2)

# Создание и разметка окна интерфейса приложения
window = tk.Tk()
greeting = tk.Label(
    text = """
    Enter 4 numbers: IW, IF, VW, FP, split by the comma to predict Depth and Width.
    Then press "Submit" button to submit values. Check it is correct in the label under the entry line.
    Once values are submitted correctly please press the "Predict" button to get predictions.
    """
                    )
greeting.pack()

entry = tk.Entry(width=50)
entry.pack()
entry.insert(0, 'IW, IF, VW, FP')
text = entry.get()
features = tk.Label(text=text)
features.pack()

submbtn_frame = tk.Frame()
predbtn_frame = tk.Frame()
submbtn_frame.pack()
predbtn_frame.pack()

button = tk.Button(master=submbtn_frame, text='Submit values', fg='black', bg='grey', )
button.bind("<Button-1>", btn_submit)
button.pack()

button = tk.Button(master=predbtn_frame, text='Predict', fg='black', bg='grey')
button.bind("<Button-1>", btn_predict)
button.pack()

frame_predict=tk.Frame(height=50)
frame_predict.pack()
values=tk.Label(text='Prediction will be here', master=frame_predict)
values.pack()

window.mainloop()
