# audio-project
## Description
An audio library for room callibration and equalization.



## Setup
### Environment
1. To install the latest version of pip on your host:

    ```bash
    python3 -m pip install --user --upgrade pip
    python3 -m pip --version
    ```

2. To create a [virtual environment](https://docs.python.org/3/library/venv.html) on your host:
    ```bash
    python3 -m venv venv
    ```
    This will create a directory called 'venv' in your current working directory.

3. To start the virtual environment:
    ```bash
    source venv/bin/activate
    ```
    After this you should see the SHELL prompt showing ('venv') indicating that you
    are inside the venv.

4. To install the requirements for the project: 
    ```bash
    pip3 install -r /path/to/project/requirements.txt
    ```

### Making Changes
1. If you have included any new modules though pip install, run the following command
   from inside the venv:
   ```bash
    pipreqs --force /path/to/project
   ```
   This should update the requirements.txt with all the included modules.

### Pulling Changes
1. After pulling the latest changes from github, run the following command to 
   resync your required packages:
   ```bash
    pip3 install -r /path/to/project/requirements.txt
   ```