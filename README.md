# Tennis Scoreboard

## Запуск Приложения

```sh
uv run tennis-scoreboard
```

## Docker

### Сбилдить образ

```sh
docker build -t tennis-scoreboard -f ./docker/Dockerfile .
```

### Запустить контейнер

```sh
docker run --name tennis-scoreboard-container tennis-scoreboard
```
