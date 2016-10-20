# yogeswarant.github.com
Yogi's corner - hosting [www.everogi.in](http://everyogi.in)

### Steps to run development server
```
$ virtualenv-2.7 venv
$ source venv/bin/activate
$ source env.sh
$ pip install --upgrade setuptools
$ pip install -r requirements.pip
$ make devserver 	# to run the server
$ make stopserver 	# to stop the server
$ make github 		# to push output directory to master branch - to publish
```
