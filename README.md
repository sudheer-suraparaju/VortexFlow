Vortexflow is a data processing platform. This platform receives high amounts of data. So here we should make sure that the system should not crash, it should utilize all the cpu cores

of the system efficiently. We use parallel processing, so that we can gain high throughput. It should be a fault tolerant self healing system meaning that even if one part of the system

is failed the other part should work flawlessly. We can use a supervisor object which identifies this fault and heals it. The routing of the data should also be taken care.



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

