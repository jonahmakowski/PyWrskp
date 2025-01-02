FROM python

WORKDIR /app

COPY ./src/requirements.txt ./

RUN pip install -r requirements.txt

COPY . ./

ENV PORT=80

EXPOSE 80

WORKDIR /app/src

CMD ["gunicorn", "--config", "gunicorn.conf.py", "main:app"]