FROM python:3.11-slim-bookworm

WORKDIR /app

RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    pip install --no-cache-dir uv==0.11.2 \
    && uv sync --frozen --no-install-project --no-dev

COPY pyproject.toml uv.lock ./
COPY src/ ./src

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-install-project --no-dev

CMD ["uv", "run", "tennis-scoreboard"]
