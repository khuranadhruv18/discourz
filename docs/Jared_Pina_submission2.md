	I added the functionality to the login, registration, and edit profile pages. This required setting up 
custom forms for the registration and edit profile pages as well as editing the html templates to use my forms
instead of the default html input fields. I also edited our account model to associate it with the Django user model in
order to be able to use all of the included functionality. 
	I also created a system to make sure that no two users can have the same email or username both for registration 
and editing profiles. I made it so all users recieve a default profile picture on registration but can change it at will 
by editing thier profile as well as giving an image preview on the edit profile page.
	Lastly I made changes to Our Edit Profile form so that users can no longer change their usernames as this can cause issues on 
other parts of the site.