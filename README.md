## Blog website made using python and flask
---

- pip install -r requirements.txt
- edit the port if required
- python app.py

### NOTE: this is only for testing environments and not recommended for production environment


#### for a simple production environment add this code in app.py:

```
if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
```
or refer to the [official flask docs](https://flask.palletsprojects.com/en/3.0.x/deploying/)