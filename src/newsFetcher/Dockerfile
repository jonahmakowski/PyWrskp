FROM python

WORKDIR /

COPY ./docker/requirements.txt ./

RUN pip install -r requirements.txt

RUN curl -fsSL https://ollama.com/install.sh | sh

COPY ./docker/setup.sh ./

RUN chmod +x setup.sh

RUN ./setup.sh

COPY . ./

ENV PORT=5000

EXPOSE 5000

WORKDIR /docker

CMD ["sh", "bootup.sh"]