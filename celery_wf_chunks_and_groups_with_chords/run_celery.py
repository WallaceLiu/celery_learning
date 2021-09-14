"""
    Run Celery Worker

For Celery to run from command line, script runs as separate process with celery command
 Usage: open terminal cd to talent-flask-services directory
 Run the following command to start celery worker:
   celery -A tasks worker -n chords --loglevel=info
"""

# Service Specific
from celery_chunks_and_groups_with_chords.celery_app import app

app.start(argv=['celery', 'worker', '-Ofair', '--without-gossip', '--without-mingle', '-l', 'info', '-n', 'chords',
                '--autoscale', '12,3'])
