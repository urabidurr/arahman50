When we access the url http://localhost:5000/static/foo.html, our prediction is that it will not access this html, but rather more directly access the app route established in ../app.py, since it has the location of static/foo.html, and is more direct than accessing this file.
But, when the app.route of this file is commented out in the app.py file, it no longer runs the code in that method but rather runs to the next option, which is this file.
So, when the app route isn't specifically defined with a method in the main file, it will search for html files that match the same location as would the methods.

When we connect to http://localhost:5000/static/foo, instead of running an html file displaying information, it instead starts a download of the file that we referenced to our systems.
It takes the directory in the folder of the main directory and, if the file is not html or directly integrated with the python output, downloads the file, like this one will download to the system when ran.
