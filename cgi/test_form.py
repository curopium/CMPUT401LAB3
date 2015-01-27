#!/usr/bin/env python
import cgi
form = cgi.FieldStorage()
val1=form.getvalue('person_name')
val2=form.getvalue('family')
print "Content-type:text/html"
print
print "The form input is here: <br/>"
print val1
print val2

print """
<form method="post" action="form.py">
<textarea name="birthday" cols="40" rows="5">
Enter birthday here ...
</textarea>

<textarea name="hobby" cols="40" rows="5">
Enter hobby here ...
</textarea>

<br/>
<input type="submit" value="Submit">
<br/>

</form>

"""
