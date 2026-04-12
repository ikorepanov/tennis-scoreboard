# Tennis Scoreboard

## Запуск Приложения

```sh
uv run tennis-scoreboard
```

## Docker

### Сбилдить образ

```sh
docker build --network=host -t tennis-sb-image -f ./docker/Dockerfile .
```

NB! `--network=host`: позволяет Docker использовать интернет-соединение сервера напрямую (в обход виртуальной сети Docker).

### Запустить контейнер

```sh
docker run --rm --name tennis-sb-container tennis-sb-image
```

NB! `--rm`: автоматически удалит контейнер после того, как он завершит работу.