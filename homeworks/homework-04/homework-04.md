## Домашняя работа 4


### Формат сдачи домашки

- [формат](../../docs/homework-flow.md)


### Само дз + оценка


- **на 1 балл**:

    создать пустой проект в корне репозитория с файлом `README.md` с каким то описанием и пустым `requirements.txt`


- **на 2 балла**:

    добавить в корне проекта файл `server.py` и проинициализировать в нем приложение `flask`

    ```python
    from flask import Flask
    
    app = Flask(__name__)
    
  
    @app.route("/")
    def server_info():
        return "My server"
  
  
    if __name__ == "__main__":
        app.run(debug=True, port=5000)
    ```
  
    также в `requirements.txt` добавить зависимость для `flask` (можно без версии)


- **на 3 балла**: 

    добавить в файле `server.py` вьюшку для того, чтобы узнать автора:

    ```python
    ...
  
    from flask import jsonify
    
    ...
    
    @app.route("/author")
    def author():
        author = {
            "name": "Stas",
            "course": 3,
            "age": 21,
        }
        return jsonify(author)
  
    ...
    ```
  

- **на 4 балла**: 

    добавить конфиг и зависимость в коде от конфига:

    создаем в корне файл `.env` и создаем там какие угодно настройки, например так:

    ```dotenv
    MODE=development
    DEBUG=True
    PORT=5000
    ```
  
    далее добавляем пакет `dotenv` в `requirements.txt` и в файле `server.py` добавляем любое применение конфига:
    
    ```python
    ...
  
    from dotenv import dotenv_values
  
    ...
  
    def get_port():
        config = dotenv_values(".env")
        if "PORT" in config:
            return config["PORT"]
        return 5000
    
    ...
    ```
  
    затем используем это в запуске приложение в том же файле `server.py`:

    ```python
    ...
  
    if __name__ == "__main__":
        app.run(debug=True, port=get_port())
    ```


- **на 5 баллов**:

    надо добавить файлик `Makefile` и описать в нем любой конфиг управления проектом, например так(для `macOS`):

    ```makefile
    PIP := venv/bin/pip
    PYTHON3 := venv/bin/python3
    TESTS_STARTER := pytest -v .
    
    clear:
        rm -rf venv
    
    venv:
        python3 -m venv venv
    
    install_requirements:
        ${PIP} install -r requirements.txt
    
    run:
        ${PYTHON3} server.py
    
    test:
        ${TESTS_PATH}
    ```
  

- **на 6 баллов**: 
      
    добавить ручку, которая умела бы складывать числа из параметров - в файл `server.py` добавить:
    
    ```python
    ...
    
    from flask import request
  
    ...
  
    @app.route("/sum")
    def runner():
        a = request.args.get('a', type=int)
        b = request.args.get('b', type=int)
        return jsonify({'sum': a + b})
  
    ...

    ```
  
    пример гет запроса: `http://localhost:5000/sum?a=1&b=2`


- **на 7 баллов**:

    вынести сумму как функцию в контроллер:

    + создать в корне `controllers.py` с подобным содержанием:
        
        ```python
        def operation(a, b):
            if (a == None) or (b == None):
                return None
            return a + b
        ```
    
    + добавить в `server.py` использование контроллера:

        ```python
        ...

        from .controllers import operation

        ...

        @app.route("/sum")
        def runner():
            a = request.args.get('a', type=int)
            b = request.args.get('b', type=int)
            return jsonify({'sum': operation(a, b)})

        ...
        ```
    
- **на 8 баллов**: покрыть контроллер тестами
- **на 9 баллов**: добавить тайпинги где только можно

- **А если все это заработает, то будет 10!**

### Дедлайн

17:00 22.05.2023
