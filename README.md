# learning-flask

Just one of the things I'm learning. https://github.com/hchiam/learning

## Setup:

```bash
python3 -m venv venv
. venv/bin/activate # to use the virtual environment
pip install Flask
export FLASK_APP=hi.py
flask run
http://localhost:5000
deactivate # to close the virtual environment
```

## After that:
And then after that, every time you want to run the site:
```bash
. venv/bin/activate
flask run
http://localhost:5000
```

Remember to close the venv when you're done:
```bash
deactivate
```

## Example: 

http://hchiam.pythonanywhere.com/

## More examples:

- http://hchiam.pythonanywhere.com/hello
- http://hchiam.pythonanywhere.com/hello/Howard
- http://hchiam.pythonanywhere.com/not-valid-url
- http://hchiam.pythonanywhere.com/post/1
- http://hchiam.pythonanywhere.com/post/2
- http://hchiam.pythonanywhere.com/path/some/arbitrary/path
- http://hchiam.pythonanywhere.com/error
- http://hchiam.pythonanywhere.com/login
