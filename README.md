# Supplemental Instruction Website

A simple flask app to share files over the web

## Application Use

This application was designed to be used using PythonAnywhere to allow Supplemental Instruction leaders to share files with students. This is a simple two page website: one page that is password protected where leaders can add and remove files and one page where students can view and download files added by the leader.

A copy of this website was used for a section of CS 159 Supplemental Instruction during the Spring 2020 Semester and can be viewed [here](https://purduesi159.pythonanywhere.com/).

## Setting up

The fastest way to setup is to clone the repository. This can be done with the following command:

```sh
$ git clone https://github.com/MattToast/mattWebSI.git
```

First make sure that your environment has all of the dependencies specified in the `requirements.txt`. From there, run the set up script `setup.py` to resolve the path and set up the username and password for the control page. This can be done using the following command:

```sh
$ python3 setup.py
```

The next step is to test that the app works as expected. To do this, deploy the app locally to test using the following command:

```sh
$ python3 app.py
```

Finally, the last step set is to deploy the app on the web. This can be done by following the instructions to deploy a flask app on PythonAnywhere.