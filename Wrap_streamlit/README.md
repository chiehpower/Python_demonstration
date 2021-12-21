# Wrap Streamlit

The purpose is to try to wrap the Streamlit.

There are several packages to be able to wrap the codes including the python libraries (standalone) such as `pyinstaller`, `nuitka`, `py2exe`, `Cx_freeze`, etc.

Basically, Streamlit is one kind of web services and it includes a lot of dependencies, so it is not easily to wrap. 


### Steps:

- Use `Pyinstaller`

```
pyinstaller -F run_streamlit.py
```

- Use `nuitka`

```
python3 -m nuitka main.py --nofollow-imports  --follow-import-to=need --static-libpython=yes --standalone
```
**To be continued...**
