# Eletronic appliance System

Esse projeto, tem como principal funcionalidade gerenciar dados de Produtos eletronicos.
Um simples crud, no qual o usuário pode criar, atualizar e deletar diferentes produtos que ele queira.

### Features
- Get all products in database
- create a new product 
- update any of them
- delete any product you want 

<img src="/assets/media/Captura de ecrã 2024-11-13 211347.png">

### Clone repository
```
https://github.com/NuneszG/Electronic-appliance-System.git
```

### Docker compose
```
docker-compose db up --build
```
```
docker-compose products up --build
```

### Run container
```
docker-compose up
```

### Virtual space
```
Linux or MacOS
source venv/bin/activate

Windows
./venv/Scripts/activate
```

### Install
```
poetry install
```

### Run
```
With poetry
task server

or

Without poetry
python manage.py runserver
```
