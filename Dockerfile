FROM python:3.12.4


RUN apt update && apt install -y npm

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt
RUN npm i

EXPOSE 8000

CMD ["npm", "run", "prod:django:server"]
