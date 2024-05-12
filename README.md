# СПОСОБ ЗАГРУЗКИ

### Windows

- Установите Python 3.10 и выше
- Создайте виртуальное окружение 
```python 
python -m venv venv
```
- Запустите виртуальное
```python
. venv/bin/activate
```

### MacOs

- Установите Python 3.10 и выше
- Создайте виртуальное окружение 
```python 
python3 -m venv venv
```
- Запустите виртуальное
```python
. venv/bin/activate
```

## Запуск проекта
Далее вам нужно запустить проект для этого пропишите данный команды
### Windows


```python
python manage.py migrate
```
```python
python manage.py loaddata tests_for_exams/fixtures/ipc.json
```
```python
python manage.py runserver 
```

### MacOs

```python
python3 manage.py migrate
```
```python
python3 manage.py loaddata tests_for_exams/fixtures/ipc.json
```
```python
python3 manage.py runserver 
```

Так же вы можете использовать за место **python** команду **./manage.py**.

```python
./manage.py migrate
```
```python
./manage.py loaddata tests_for_exams/fixtures/ipc.json
```
```python
./manage.py runserver 
```

## Вход в административную панель

Перейдите по данной ссылке
```djangourlpath
http://127.0.0.1:8000/admin/login/?next=/admin/
```

```html
Login: admin
Password: 123
```

## Создание теста
Оптимизация и встроенная панель еще в процессе разработки. Для создание теста вам нужно будет перейти по ссылки
```djangourlpath
http://127.0.0.1:8000/generate_ipc_test/
```

## Примечания!
**Проект не будет работать если вы не вошли в административную панель**
