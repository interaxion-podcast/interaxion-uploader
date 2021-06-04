# Interaxion Uploader

A simple example for uploading files via HTTP built with Flask. The code is largely based on [ddavignon/flask-multiple-file-upload: Small application for uploading multiple photos using Flask, Flask-Dropzone, and Flask-Uploads](https://github.com/ddavignon/flask-multiple-file-upload).


## Deploy (in onamae.com rental server)

```sh
# Install Anaconda
# (Python from Pyenv goes to ModuleNotFoundError: No module named '_ctypes' and Homebrew cannot be installed on onamae.com)
wget https://repo.anaconda.com/archive/Anaconda3-2021.05-Linux-x86_64.sh
bash Anaconda3-2021.05-Linux-x86_64.sh
TMPDIR="${PWD}/tmp" ./Anaconda3-2021.05-Linux-x86_64.sh

bash
git clone https://github.com/interaxion-podcast/interaxion-uploader.git
cd interaxion-uploader
bash run.sh
```
