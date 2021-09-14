"""
    Run Celery Worker
For Celery Flower to run from command line, script runs as separate process with celery command
 Usage: open terminal cd to talent-flask-services directory
 Run the following command to start celery flower:
      celery -A tasks flower --port=5511 --loglevel=info
"""

# Service Specific

from celery_chunks_and_groups_with_chords.celery_app import app

app.start(argv=['celery', 'flower', '--port=5511', '-l', 'info'])
