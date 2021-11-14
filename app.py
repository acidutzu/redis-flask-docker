import time
import redis

from flask import Flask

app = Flask(__name__)
connect_to_redis = redis.Redis(host='redis', port=6379)


def za_count():
    retry = 5
    while True:
        try:
            return connect_to_redis.incr('tickings')
        except redis.exceptions.ConnectionError as errcon:
            if retry == 0:
                raise errcon
            retry -= 1
            time.sleep(0.5)


@app.route('/')
def hihou():
    counting_page = za_count()
    return 'Salutare si bine v-am gasit dragii mei,cineva spera ca am ramas fara idei... | mesajul a fost vazut de {} ori.\n'.format(counting_page)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
