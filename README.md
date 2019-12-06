# django-jaeger-middleware

This is a simple jaeger tracing middleware for Django applications. 

I read Jaeger - Distributed Tracing System on [github](https://github.com/jaegertracing/jaeger-client-python) and make it plus.

## Installing

```bash
$ pip install django-jaeger-middleware
```

Then add ```django-jaeger-middleware.middleware.JaegerMiddleWare``` to the end your ```MIDDLEWARE``` in `settings.py`. 

For example:

```
MIDDLEWARE = [
	...
	'django-jaeger-middleware.middleware.JaegerMiddleWare'
]
```

## Enjoy!

Email me with any questions: [galphaxie@gmail.com](galphaxie@gmail.com).
