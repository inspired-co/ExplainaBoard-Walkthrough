# Documentation for different Setup


## How to use Linux in Windows OS?
* English doc: https://learn.microsoft.com/en-us/windows/wsl/install
* Chinese doc: https://www.cnblogs.com/jetttang/p/8186315.html

## How to install python3.9 in linux?

```shell script
sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install python3.9
```

Once you installed python3.9, as one best practice, creating a virtual environment under
python 3.9 is recommended
```shell script
sudo apt install python3.9-venv
python3.9 -m venv venv
source venv/bin/activate
pip install --upgrade pip
```
Then you can do whatever you like in the virtual environment you have set up.
