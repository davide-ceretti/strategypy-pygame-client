strategypy-pygame-client
------------------------

A front end for strategypy (https://github.com/davide-ceretti/strategypy) written in PyGame

Installation
------------

* ```sudo apt-get install mercurial libfreetype6-dev python-dev python-numpy ffmpeg libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev libsmpeg-dev libsdl1.2-dev libportmidi-dev libswscale-dev libavformat-dev libavcodec-dev```
* ```pip install -r requirements.txt```

Usage
-----

Example:
* ```./run_example.sh```

Load json game:
* ```cat example.json | python strategypy-pygame-client/main.py```

Pipe output from strategypy (assuming you have strategypy in ../)
* ```python ../strategypy/strategypy/main.py killer prey prey | python strategypy-pygame-client/main.py```

You can also pipe the output of strategypy main directly in the front end.
