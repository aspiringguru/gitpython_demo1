# automating git with python

Demo of methods to automate git with python.

## Getting Started


https://docs.python.org/3/library/subprocess.html

### Prerequisites

nil. This uses standard package within python 3 distribution.

### Setup

git needs to be installed and configured at the command line.

https://wiki.paparazziuav.org/wiki/Github_manual_for_Ubuntu
to show the git config details.
```
git config --list
user.name=aspiringguru
user.email=bmatthewtaylor@gmail.com
#
git config --global user.name "<your-github-username>"
git config --global user.email "<your-github-email>"
```

if ~/.ssh does not exist (first time using ssh or ssh-keygen)
```
mkdir -p ~/.ssh
cd ~/.ssh
ssh-keygen -t rsa -C "bmatthewtaylor@gmail.com"
#this generates /home/<your-user-name>/.ssh/id_rsa & id_rsa.pub
ls -la ~/.ssh/
less ~/.ssh/id_rsa
less ~/.ssh/id_rsa.pub
#install gedit if not already
sudo apt-get update
sudo apt install gedit
gedit  --version
gedit id_rsa.pub
#nb: gedit will not work on ubuntu in windows since no desktop
less id_rsa.pub
'''

loginto github > Account Settings > SSH Keys > Add another public key
https://github.com/settings/keys
copy paste content of ~/.ssh/id_rsa.pub into new key field on github.

'''
eval $(ssh-agent)
ps aux | grep ssh
#these should return same pid number
'''

useful test to verify ssh is running ok.
'''
printenv | grep SSH_AUTH_SOCK
#ssh commands talk to the ssh-agent using the SSH_AUTH_SOCK environment variable
'''

setup the git for your repo
'''
cd /foo/bar/git-repo-dir
git init
ls -la
git commit -m 'first commit'
#create new repo on github if needed.
#github will give you instructions like this.
git remote add origin https://github.com/<your-github-username>/<your-git-repo-name>.git
git push -u origin master
#the above needs to be changed to set-url otherwise will get error message like this.
#error: asks for username
git push -u origin master
Username for 'https://github.com':

git remote set-url origin git@github.com:USERNAME/REPOSITORY.git
git push -u origin master



## Authors

* **Matthew Taylor**  - [aspiringguru](https://github.com/aspiringguru)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* StackOverflow
