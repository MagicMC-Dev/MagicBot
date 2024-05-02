FROM python:3.11-bookworm as requirements-stage

WORKDIR /app

RUN curl -sSL https://pdm-project.org/install-pdm.py | python3 -

ENV PATH="${PATH}:/root/.local/bin"

RUN pdm install -G:all \
  && pdm run pre-commit install

COPY ./pyproject.toml ./pdm.lock* /app/

ENV TZ Asia/Shanghai

CMD [ "pdm run python bot.py" ]
