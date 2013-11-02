# Introducing Kite !

Kite is an opensource gmail replacement

I really like gmail. I use it a _lot_. Google got a lot of things right when they designed it. 
However I'd like to be in control of my data, and to host it in on my own server.

A few months ago I decided to set up my own mail server so I started shopping around for potential solutions. 
A lot of the components that make an email server already work : Postfix for email handling, Dovecot for IMAP, Spamassassin for SPAM and ElasticSearch for searching. 

Unfortunately, I didn't find a webmail that would cut it, so I decided to write my own. After a few months of coding, kite was born!

Kite is still very much alpha software : it can only display individual messages. I hope to get something a lot more useable in the next few months, though.

What does it look like?

It looks a lot like gmail. Here is the inbox view :


And this is a message view :

Will it be easy to install?

Yes! I'm using puppet to setup the vagrant machine I'm coding on, so in the future, one puppet apply should be enough to set up a server
with kite, Postfix and Dovecot configured with sensible defaults. 

How can I contribute?

The code and the issues are hosted on github. You can also shoot me an email at kite~khamidou.com (replace ~ with @) for suggestions or improvements. 
