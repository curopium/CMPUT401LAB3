#!/usr/bin/env python

print """Content-type:text/html

<form method="post" action="test_form.py">
<textarea name="person_name" cols="40" rows="5">
Enter name here ...
</textarea>

<textarea name="family" cols="40" rows="5">
Enter family here ...
</textarea>

<br/>
<input type="submit" value="Submit">
<br/>

</form>

"""

import cgi
form = cgi.FieldStorage()
val1=form.getvalue('birthday')
val2=form.getvalue('hobby')
print "The form input is here: <br/>"
print val1
print val2
