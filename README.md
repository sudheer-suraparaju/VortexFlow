1. For this project we are using "Actor design pattern". 
2. As per this design pattern we are imposing following conditions:

&nbsp;	(a). Every actor is a process.

&nbsp;	(b). One actor should not send data to another actor directly.

&nbsp;	(c). Every actor is independent.

&nbsp;	(d). One actor can send messages to another actor. (not the data)

&nbsp;	(e). Every actor can process the messages it receives.

&nbsp;	(f). Every actor can change it's own data that is it's own state.

&nbsp;	(g). No shared data is allowed between two actors to avoid race conditions.

&nbsp;	(h). Two actors communicate only through messages.

&nbsp;	(i). One actor sends messages to another actor and does not wait for the reply, instead works on other things.

