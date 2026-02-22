localhost -> host.docker.internal in Docker Desktop
(network: host на Win не работает)
Путь через ./ на win не всегда находился, через .\ ок
promtool check config <promet.yml>

_
Ещё можно положить все docker-compose контейнеры в одну общую сеть external (Checked on Win)
___
docker network create promet_test
_
networks:
  promet:
    external: true
    name: promet_test
__

AI ответ про host.docker.internal на ubuntu:

Чтобы достичь того же результата на Ubuntu, используйте один из следующих способов:

1. Добавление extra_hosts в Docker Compose (Рекомендуется)
Вы можете вручную прописать сопоставление имени host.docker.internal с IP-адресом шлюза хоста. В Docker версии 20.10+ для этого используется специальный ключ host-gateway: 
yaml

services:
  your-service:
    image: your-image
    extra_hosts:
      - "host.docker.internal:host-gateway"

Используйте код с осторожностью.
После этого внутри контейнера адрес http://host.docker.internal будет указывать на ваш хост.

2. Использование IP-адреса шлюза напрямую
В стандартной сети Docker (bridge) хост обычно доступен по IP-адресу 172.17.0.1. 

    Вместо localhost:8080 используйте 172.17.0.1:8080.
    Важно: этот адрес может измениться, если вы создаете свои кастомные сети в Compose. Чтобы узнать точный адрес шлюза, выполните на хосте:
    docker network inspect bridge --format '{{range .IPAM.Config}}{{.Gateway}}{{end}}'.
