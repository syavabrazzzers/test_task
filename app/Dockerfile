FROM python:3.10 as python-base
ENV PIP_ROOT_USER_ACTION=ignore
RUN mkdir usr/src/code && apt update

WORKDIR usr/src/code
COPY . /usr/src/code

RUN pip3 install -r requirements.txt

CMD ["uvicorn", "main:app", "--reload"]