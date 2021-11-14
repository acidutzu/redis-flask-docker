import time
import redis

from flask import Flask

app = Flask(__name__)
cache = redis.Redis(host='172.17.0.3', port=6379)


def counter():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)


@app.route('/')
def hihou():
    count = counter()
    return 'Salutare si bine v-am gasit dragii mei,cineva spera ca am ramas fara idei... | mesajul a fost vazut de {} ori.\n'.format(count)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
