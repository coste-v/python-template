FROM python:3.9

ARG ENV
#ARG USERNAME=virgilecoste
#ARG USER_UID=1000
#ARG USER_GID=$USER_UID

#RUN groupadd --gid $USER_GID $USERNAME \
#    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME

#USER $USERNAME

COPY . /app
WORKDIR /app

RUN pip install --upgrade pip && \
    pip install poetry==1.1.11 && \ 
    poetry config virtualenvs.create false

RUN if [ "${ENV}" = "dev" ] ; then poetry install ; else poetry install --no-dev ; fi

ENTRYPOINT ["python3", "-m", "main"]