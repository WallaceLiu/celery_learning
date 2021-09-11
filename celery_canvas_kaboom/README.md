# canvas_kaboom

A minimal demo app showcasing broken canvas interactions under near-default
configuration in celery 3.1.x

## chord_chain

A chord with a chain as its callback fails spectacularly, but a 
group connected to a chain works just fine.

Expected use:
* Run ```canvas_kaboom worker --config=canvas_kaboom.config```
* Run ```canvas_kaboom shell --config=canvas_kaboom.config```
* In the shell:
```python
from canvas_kaboom.chord_chain import cc_works, cc_fails
from canvas_kaboom.group_upgrades import gu_works
cc_works()
gu_works()
cc_fails()
```
* Observe output in worker
