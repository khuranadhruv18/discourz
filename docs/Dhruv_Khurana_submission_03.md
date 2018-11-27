I helped teammates with technical problems and suggested changes to the idea and organizational structure of the program frequently.
As an example of a time I helped a teammate: I helped him realize that he could verify a username field on the client side, rather than contact the backend.
I suggested cutting the discussion section to make finishing by our deadline more realistic. I also checked in with the team frequently to make sure they were on track to finish, as well as engaged in and encouraged discussion on new ideas.

I, once again, handled all the aspects for the debate part of this project. I created the create debate portion. 
This portion allows users to add a new debate to a list such that others can click on the item and engage (in the future) 
in a realtime one-on-one debate. This included the POST 'if' in debate_create views.py, (changes to) CreateDebate in forms.py, and new form in the corresponding htmls.

I also made it possible for users to vote on past debates. If you go to the second tab on the debate page, you'll see a list of past debates for users to vote on.
When you click on one, you can vote on which user you think made a better argument. This vote is then updated in the database and updated in the tab. This involved either making changes to or creating the
the html file pastChatTemplates for forms, the debate.css file, the forms.py file for whichVote, and the views.py file for the POST function (method pastChat).
