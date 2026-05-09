# Tennis Scoreboard

```sh
cd tennis-scoreboard
```

## Запуск Приложения

```sh
uv run tennis-scoreboard
```

## Docker

### Сбилдить образ

```sh
docker build --network=host -t tennis-sb-image -f ./docker/Dockerfile .
```

`--network=host` — позволяет Docker использовать интернет-соединение сервера напрямую (в обход виртуальной сети Docker).

### Запустить контейнер

```sh
docker run --rm --name tennis-sb-container tennis-sb-image
```

`--rm` — автоматически удалит контейнер после того, как он завершит работу.

### Запустить контейнер с MySQL

```sh
docker run -d \
  --name mysql \
  --restart unless-stopped \
  --env-file .env \
  -v mysql_data:/var/lib/mysql \
  -p 127.0.0.1:3306:3306 \
  mysql:8.0.46
```

`-d` — запуск в фоне: контейнер работает как сервис  
`--name` — имя контейнера для удобного обращения к нему  
`--restart unless-stopped` — автоперезапуск при падении или перезагрузке сервера  
`--env-file` — передать переменные окружения из файла  
`-v mysql_data:/var/lib/mysql` — named volume: данные хранятся на хосте и переживают пересоздание контейнера  
`-p 127.0.0.1:3306:3306` — порт доступен только с localhost, не снаружи
