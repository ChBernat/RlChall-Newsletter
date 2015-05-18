# RlChall-Newsletter
Easy to maintain newsletter based on Django, that has was made for a start-up.

First, you have to install pip for Python3.X.
 Despite the methods given in many tutorials around the internet, there's much more simple way to do so.

 For Linux:

 	wget https://bootstrap.pypa.io/get-pip.py

 It will download 'get-pip.py' file for you. It's the most pythonic way to install things.

	 python3 get-pip.py
 
 This command will simple install pip for your default python3, you can do it for whatever python ver. you already have.


 Okay. So far, so good! You've done your first step to set-up my project.
  The second step.

 Install virtualenv using pip.

	[sudo] pip install virtualenv

 Go to a directory where you have cloned my project and create your own virtual enviromnet.

	[sudo] virtualenv <whatever name you want>

 WHILE NAMING: avoid whitespaces.

  Third step.

 Activate your virtualenv:

 . YourVenvName/bin/activate

And then: 

 pip install -r /path/to/requirements.txt

The command will install requirements for this Newsletter.

Voila! To run development server, you ought to go to the folder where you have 'manage.py' and then run this command:

  python3 manage.py runserver

 manage.py has many more! Check it with: python3 manage.py



Enjoy, don't forget to raport bugs and leave feedback!
