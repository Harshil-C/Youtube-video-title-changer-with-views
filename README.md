# Youtube-video-title-changer-with-views

TRY TO UNDERSTAND THE CODE BEFORE USING IT UNDERSTAND THE RISKS:
YOU MUST ADD A LOOP TO HAVE CONTINUOS UPDATION OF THE TITLE WITH CHANGE IN VIEWS IN THE MAIN FUNC IN MAIN.PY(REMEMBER THE QUOTA COST)
This rep enables you to change youtube video title speacifying the views ,like count or anyother stats(you can add)
things you need :
python 
and google client libraries that are in the code
you need to make a project in the google developer console and enable youtubes data api .fill in the credential ,you need to setup OAuth credential (since updating is a PUT, which need authorization).Download the your_client_secret.json fileand add it to the directory this codes are copied.


run the command `python main.py` on your terminal .You will be asked for the videoid first then category id ,put that in and there will be authorization to proceed
PROBLEM: AFTER SOME UPDATION AND LISTING OF VIDEO THERE IS A QUOTA COST LIMIT FOR THE API WHICH YOU CAN CHANGE UPTO CERTAIN LIMIT, AFTER THE LIMIT YOU CANNOT CHANGE IT NOMORE.YOU CAN ASK FOR MORE QUOTA WHICH REQUIRE SOME PROCEDURE
you can have the title you need by changing the updatevideo() fuction in the main.py.
THIS IS WILL NOT CURRENTLY CHANGE THE TITLE WITH VIEWS IF YOU WANT THAT YOU CAN PUT THE MAIN() FINC IN CONTINOUS LOOP(YOU DONT NEED TO PUT THE ENTIRE MAIN FINC IN THE LOOP ,DONT PUT THE AUTH.AUTHENTICATION IN THE LOOP AS ONLY ONE AUTHENTICATION IS REQUIRED )KEEP IN MIND THAT UPDATIN VIDEO WILL TAKE MUCH MORE QUOTA COST AND SOON YOU WIL HAVE YOUR QUOTA DRAINED.
