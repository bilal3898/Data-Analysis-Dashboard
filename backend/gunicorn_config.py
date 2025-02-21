bind = "0.0.0.0:8000"
workers = 4  # Number of Gunicorn worker processes
timeout = 120  # Request timeout in seconds
loglevel = "info"
accesslog = "-"  # Log access requests to stdout
errorlog = "-"  # Log errors to stdout
