Omgrofl-compiler
===================

omgrofl compiler made in python

About
-----

This project aims to create a fully-functional interpreter of an esoteric
programming language called Omgrofl. More information on the language itself
can be found here: http://esolangs.org/wiki/Omgrofl

How it works
------------
First we have to read the code and create lexems. That's the job of the <b>lexer</b>.
By reading the code analyzing it, we can then use the parser to create an Abstract Syntax Tree.



Getting started
---------------

Run an example:

You can run test.py and change the example file at line 56

Currently supported statements
------------------------------

+ Assignment (*variable* iz *variable/value*; *variable* to /dev/null)
+ Char output (rofl *variable*)
+ Char input (stfw *variable*)
+ Infinite loop (rtfm ... brb)
+ For loop (4 *variable* iz *variable/value* 2 *variable/value* ... brb)
+ Loop break (tldr)
+ Comments (w00t)
+ Sleep (afk *variable/value*)
+ Program exit (stfu)
+ Incrementing / decrementing (lmao/roflmao *variable*)
+ Conditions (wtf *variable/value* iz (nope) liek/uber *variable/value* ... brb)
+ Stack/Queue (n00b/l33t/haxor *variable*)
