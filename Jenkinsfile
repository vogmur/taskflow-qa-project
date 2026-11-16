// Главный блок пайплайна (конвейера)
pipeline {
    // Указываем, что сборка может запускаться на любом доступном агенте (на нашем ПК)
    agent any
    
    // Блок со всеми этапами (стадиями) нашего конвейера
    stages {
        
        // Этап 1: Скачиваем код с GitHub
        stage('Checkout (Скачивание)') {
            steps {
                echo 'Скачиваем проект с GitHub...'
                git branch: 'main', url: 'https://github.com/vogmur/taskflow-qa-project.git'
            }
        }
        
        //Этап 2: Просто проверяем, что Jenkins запустился
        stage('Подготовка') {
            steps {
                echo 'Начинаем сборку проекта TaskFlow...'
            }
        }
        
        // Этап 3: Сборка Docker-образа из нашего Dockerfile
        stage('Сборка Docker') {
            steps {
                echo 'Собираем Docker-образ...'
                // bat - это команда для Windows. Она говорит Дженкинсувыполнить команду в командной строке
                bat 'docker build -t taskflow-app ./app'
            }
        }
        
        // Этап 4: Быстрая проверка работоспособности (Smoke Test)
        stage('Проверка (Smoke Test)') {
            steps {
                echo 'Запускаем контейнер для проверки...'
                // Запускаем контейнер на порту 5002, чтобы не конфликтовать с моим рабочим
                bat 'docker run -d -p 5002:5000 --name taskflow-jenkins-test taskflow-app'
                
                echo 'Ждем 3 секунды, чтобы сервер успел запуститься внутри контейнера...'
                sleep 3
                
                echo 'Проверяем, что контейнер реально запущен...'
                bat 'docker ps'
                
                echo 'Удаляем тестовый контейнер, чтобы не засорять систему...'
                bat 'docker rm -f taskflow-jenkins-test'
            }
        }
    }
}