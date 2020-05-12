# Python

[![](https://img.shields.io/badge/Progress-Updating-blue)](./)

There are many simple examples about python. 
The purpose is only to record my note.

## memory-profiler 
> Info: https://pypi.org/project/memory-profiler/

Command:
```
mprof run <executable>
mprof
```

For exmaple,
``` 
mprof run test.py
mprof plot
```

List :
```
mprof run: running an executable, recording memory usage
mprof plot: plotting one the recorded memory usage (by default, the last one)
mprof list: listing all recorded memory usage files in a user-friendly way.
mprof clean: removing all recorded memory usage files.
mprof rm: removing specific recorded memory usage files
```

We can also our log of memory usage.
```
fp=open('memory_profiler.log','w+')
@profile(stream=fp)
```
