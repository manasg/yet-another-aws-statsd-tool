Yet Another AWS StatsD Tool
==========================

Why?
----
Sometimes its just faster to write your own than trying to use a one written in NodeJS

What does it do?
----------------
Gets whatever you need from AWS (via boto) and sends them to StatsD

Can I use it?
-------------
Yes, its public. But it is not a product. I view it as a set of scripts

Dependencies
------------
Tested on Ubuntu 12.04. 
Python, boto and statsd_client (installable via pip) 

Test
----
python test.py 
can be used to make sure credentials are loaded and there is connectivity

How to use?
-----------
I would run these via Cron

