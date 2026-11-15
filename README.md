# QA Portfolio Project: TaskFlow

Добро пожаловать в мой учебный проект по тестированию веб-приложений.


## О проекте
**TaskFlow** - это простой таск-менеджер (backend: Python/Flask, frontend: HTML/JS, DB: SQLIte), созданный для отработки навыков тестирования полного цикла (STLC).

## Примененные инструменты
* **Web & UI:** Chrome DevTools, Postman (REST), Charles (Proxy), Mockoon (Mocks).
* **Backend & DB:** SQL (SQLite), DBeaver, pgAdmin.
* **Нагрузка и Автоматизация:** Apache JMeter, Docker, Jenkins (CI/CD).
* **Инфраструктура:** Git, GitHub, VS Code, CMD/Git Bash.

## Структура репозитория
* [`/docs`](./docs) - Продуктовая и тестовая документация (PRD, Test Plan, Checklists, Bug Reports).
* [`/app`](./app) - Исходный код приложения (Python/Flask, HTML/JS).
* [`/tests`](./tests) - Артефакты тестирования: коллекция Postman (API-тесты, окружение) и нагрузочные тесты JMeter.

## Как запустить проект

### Локальный запуск (Python)
1. Установите Python (версия 3.10+).
2. Выполните `pip install flask` в терминале.
3. Запустите приложение: `python app/app.py`.
4. Приложение доступно по адресу: `http://127.0.0.1:5000`

### Запуск через Docker
1. Собрать образ: `docker build -t taskflow-app ./app`
2. Запустить контейнер: `docker run -d -p 5001:5000 --name taskflow-container taskflow-app`
3. Приложение доступно по адресу: `http://127.0.0.1:5001`

---
*Автор: Васильев Олег (QA Engineer)*
