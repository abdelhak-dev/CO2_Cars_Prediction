import uvicorn
import features
import app

if __name__ == "__main__":
    # The next commande line is to acces the API  from any device in local network
    ## So to get in, you should enter the ip adress of the the host computer
    ###By entering commande >$ ipconfig in windows and ifconfig in Linux and MacOS
   # uvicorn.run("app:app", port=8000,host='0.0.0.0',reload=True)
    uvicorn.run("app:app", port=8000, host='127.0.0.3')
    #The next commande is to acces api only on localhost "Your computer only",
    ##Run the commande wish is good for you.
    #uvicorn.run("app:app", port=8000, host='127.0.0.3', reload=True)