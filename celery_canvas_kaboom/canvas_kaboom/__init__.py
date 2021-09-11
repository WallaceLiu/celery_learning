from celery import Celery

app = Celery()

def main():
    app.start()

if __name__ == '__main__':
    main()
