FROM python:3.9

ARG ENV

COPY . /app
WORKDIR /app

RUN pip install --upgrade pip && \
    pip install poetry==1.1.11 && \ 
    poetry config virtualenvs.create false

RUN if [ "${ENV}" = "dev" ] ; then poetry install ; else poetry install --no-dev ; fi

ENTRYPOINT ["python3", "-m", "main"]