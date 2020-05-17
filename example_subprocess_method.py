from subprocess import *
import sys
import os

def gitcommit(repo_dir, filename="."):
  '''
    filename can be list or string for individual file.
    return @ git add,success_value=1
    return @ git commit,success_value=2
    return @ git push, success_value=3
  '''
  success_value=0
  print("gitcommit:filename=", filename)
  print("gitcommit:repo_dir=", repo_dir)
  wd = os.getcwd()
  try:
    os.chdir(repo_dir)
    print("start git add.")
    output = run(["git", "add", "."], capture_output=True)
    print("git add completed.")
    print("output.stderr:", "'"+output.stderr.decode('utf-8')+"'")
    print("output.stdout:", "'"+output.stdout.decode('utf-8')+"'")
    print("output.stderr==None:", output.stderr==None)
    print("output.stdout==None:", output.stdout==None)
    print("output.returncode:", output.returncode)
    if output.returncode==0:
      success_value=1
      output=None
      print("start git commit.")
      output = run(["git", "commit", "-m", "commit message three"], capture_output=True)
      #exits to exception here when error occurs during git commit.
      print("git commit completed.")
      print("output.stderr:", output.stderr.decode('utf-8'))
      print("output.stdout:", output.stdout.decode('utf-8'))
      print("output.stderr==None:", output.stderr==None)
      print("output.stdout==None:", output.stdout==None)
      print("output.returncode:", output.returncode)
      if output.returncode==0:
        success_value=2
        output=None
        print("start git push.")
        output = run(["git", "push"], capture_output=True)
        print("git push completed.")
        print("output.stderr:", output.stderr)
        print("output.stdout:", output.stdout)
        print("output.stderr==None:", output.stderr==None)
        print("output.stdout==None:", output.stdout==None)
        print("output.returncode:", output.returncode)
        if output.returncode==0:
          success_value=3
          print("success @ git push, output.returncode==0.")
  except CalledProcessError as error:
    #todo: add logging here.
    print("CalledProcessError error caught.")
    print('CalledProcessError:An exception occurred: {}'.format(error))
    print("CalledProcessError:sys.exc_info()[0]:", sys.exc_info()[0])
    print("CalledProcessError:output:", output)
    print("CalledProcessError:output.stderr:", output.stderr)
    print("CalledProcessError:output.stdout:", output.stdout)
  #return to original working dir before exiting.
  os.chdir(wd)
  return success_value

repo_dir=os.getcwd()
gitcommit(filename=".", repo_dir=repo_dir)
