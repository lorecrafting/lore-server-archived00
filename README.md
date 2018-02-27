# Welcome to Evennia!

This is your game directory, set up to let you start with
your new game right away. An overview of this directory is found here:
https://github.com/evennia/evennia/wiki/Directory-Overview#the-game-directory

You can delete this readme file when you've read it and you can
re-arrange things in this game-directory to suit your own sense of
organisation (the only exception is the directory structure of the
`server/` directory, which Evennia expects). If you change the structure
you must however also edit/add to your settings file to tell Evennia
where to look for things.

## First Time Setup

https://github.com/evennia/evennia/wiki/Getting-Started#mac-install

Follow instructions just right up before it tells you to do `evennia --init mygame`.
Since this is our game folder we don't need to init a new one.  Just follow directions up 
to initting the game, and instead of initting, just cd into the repository you cloned down to your local machine
and start the server.

## Starting Server and Developing Locally

Your game's main configuration file is found in
`server/conf/settings.py` (but you don't need to change it to get
started). If you just created this directory (which means you'll already
have a `virtualenv` running if you followed the default instructions),
`cd` to this directory then initialize a new database using


    evennia migrate
    (You may receive a seeder database in which case you don't need to migrate)

To start the server, stand in this directory and run

    evennia start

This will start the server, logging output to the console. Make
sure to create a superuser when asked. By default you can now connect
to your new game using a MUD client on `localhost`, port `4000`.  You can
also log into the web client by pointing a browser to
`http://localhost:4001`.

## Deploying to Production

The production server is on an Amazon EC2 Ubuntu 16.04LTS instance with a public ip of `34.216.237.61` and public DNS of `lorecraft.io`.  Inbound ports of 80, 443 and 22 are open.  Nginx first redirects all HTTP traffic to HTTPS and reverse proxies into the Evennia Webserver at port 4001. Nginx will also reverse proxy all secure websocket connections to port 4005  The Evennia webclient and admin panel is publicly accessible through https://lorecraft.io . 

The lorecraft custom UI client is deployed elsewhere via www.netlify.com and is publicly accessible at https://lorecraft.netlify.com It talks to the Evennia server via secure websockets.

To deploy changes onto the production server, commit changes onto master branch and push changes upstream.
Ask an admin to give you access to the production server.  They will create a new linux user and attach your key to the username.

Once you are able to SSH into the instance, run this on your local computer: 

`ssh -v -i ~/.ssh/your-key-file.pem yourusername@lorecraft.io ./muddev/scripts/ev-pull-reload.sh`

This will SSH into the instance and immediately execute a script that pulls the changes you pushed up to master and reload Evennia.  You should store this command as an alias.


# Resources

From here on you might want to look at one of the beginner tutorials:
http://github.com/evennia/evennia/wiki/Tutorials.

Evennia's documentation is here:
https://github.com/evennia/evennia/wiki.

Giving access to production server:
https://aws.amazon.com/premiumsupport/knowledge-center/new-user-accounts-linux-instance/

Enjoy!
