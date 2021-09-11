from celery_large_file_upload_elasticsearch.server import app

if __name__ == "__main__":
    app.run(host='0.0.0.0')
