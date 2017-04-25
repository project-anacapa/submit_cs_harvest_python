# submit_cs_harvest_python
Scripts to harvest data out of legacy submit_cs into the form needed for project anacapa, using Python


# Background info

Carson, Nick

I've set up a submit.cs course called SANDBOX_CH, and made both of you
admins on it (as well as me under my pconrad@cs.ucsb.edu username, as
opposed to my "admin_phill" username which has full admin rights for
submit.cs)

SANDBOX_CH is set up like any other "real" submit.cs course, except
that it is a collection of assignments from a bunch of different
courses: C++, Python, Java.

It is a good collection of various use cases that might come up in
terms of translating from submit.cs to anacapa grader.

When you log in to submit.cs with clholoien@umail.ucsb.edu (or Nick,
with ncbrown@umail.ucsb.edu), you should see the course.

If you click on the name of the course, you land at this page:

 https://submit.cs.ucsb.edu/class/82

That reflects the route for the class "show page" and the id of the
class, which is 82.

What you see then is a list of the projects:

```
ccs_cs20_s16_lab05 
cs16_lab01 
cs16_w15_lab00 
cs32_lab04 
cs56_f16_lab06 
```

If you click on each one, you'll go to its show page, i.e. the URLS are:

| assignment | link |
| - | - |
| ccs_cs20_s16_lab05 | https://submit.cs.ucsb.edu/p/708 |
| cs16_lab01          |       https://submit.cs.ucsb.edu/p/706 |
| cs16_w15_lab00       | https://submit.cs.ucsb.edu/p/705 |
| cs32_lab04            |     https://submit.cs.ucsb.edu/p/707 |
| cs56_f16_lab06        | https://submit.cs.ucsb.edu/p/709 |

Each of those, if you manually stick "info" on the end of it, 
gives you the JSON for the assignment:

* https://submit.cs.ucsb.edu/p/708/info
* https://submit.cs.ucsb.edu/p/706/info
etc.

Here's what the first bit of JSON looks like for project 708 (see below)   (I ran this through the tool http://jsonprettyprint.com/ to get it nicely formatted--it doesn't come out of the URL looking like this.)

That reflects what you could see if you looked at the edit page here,
and followed all of the dozens of mouse clicks:

   https://submit.cs.ucsb.edu/form/project/709

This JSON structure is pretty much everything we need to recreate a programming assignment EXCEPT for the contents of the files.  Those
file contents are each referred to by their SHA hash.    For example,
the "expected" value for the first testcase is

```
"expected": "a717055ae7ab66e18e9295adbd6eacf1ccef305d",
```

To get those contents, you can do the following for any of these hashes, 
as long as you are authorized for that file:

https://submit.cs.ucsb.edu/file/insert-hash-here/dummy-file-name

For example:

https://submit.cs.ucsb.edu/file/a717055ae7ab66e18e9295adbd6eacf1ccef305d/x

Note that the x in this case at the end is a dummy value (though it must be present).  It is used to display the filename in the browser, but it is not validated.

You can also download the file by appending ?raw=1, like this:

https://submit.cs.ucsb.edu/file/insert-hash-here/dummy-file-name?raw=1

For example:

https://submit.cs.ucsb.edu/file/a717055ae7ab66e18e9295adbd6eacf1ccef305d/x?raw=1

So, the overall task for one programming assignment is: 

1.  Create a repo (initially empty) corresponding to that programming assignment, with a given directory structure.
2. Get the JSON.  Convert it from the existing format (one that Nick will specify) and store it in a certain place in that directory structure.
3. For each file referred to in the JSON by its SHA hash, get the contents of that file, and store it in an appropriate place in the directory structure.
4. Commit all of those changes to the repo.

Look this over, and then ask lots of questions. :-)

Regards,
Phill


JSON from https://submit.cs.ucsb.edu/p/708/info

```json
{
  "id": 708,
  "testables": {
    "Run lab02Tests.py and lab05Tests.py tests": {
      "test_cases": {
        "Run lab05Tests.py (student version)": {
          "stdin": null,
          "args": "bash .\/removeTestTiming.sh lab05Tests.py",
          "output_filename": null,
          "source": "stdout",
          "expected": "a717055ae7ab66e18e9295adbd6eacf1ccef305d",
          "output_type": "diff",
          "id": 9090
        },
        "Run lab02Tests.py (instructor version)": {
          "stdin": null,
          "args": "bash .\/removeTestTiming.sh lab02Tests.py",
          "output_filename": null,
          "source": "stdout",
          "expected": "119dadaa7e84ee684d54001da89b521a728e0bb6",
          "output_type": "diff",
          "id": 9088
        },
        "Run lab05Tests2.py (instructor version)": {
          "stdin": null,
          "args": "bash .\/removeTestTiming.sh lab05Tests2.py",
          "output_filename": null,
          "source": "stdout",
          "expected": "a717055ae7ab66e18e9295adbd6eacf1ccef305d",
          "output_type": "diff",
          "id": 9089
        }
      },
      "id": 2012
    },
    "Check syntax of student submitted Python files": {
      "test_cases": {
        "lab05Funcs.py file should have no syntax errors": {
          "stdin": null,
          "args": "python lab05Funcs.py",
          "output_filename": null,
          "source": "stderr",
          "expected": "da39a3ee5e6b4b0d3255bfef95601890afd80709",
          "output_type": "diff",
          "id": 9087
        },
        "lab05Tests.py file should have no syntax errors": {
          "stdin": null,
          "args": "python -m py_compile lab05Tests.py",
          "output_filename": null,
          "source": "stderr",
          "expected": "da39a3ee5e6b4b0d3255bfef95601890afd80709",
          "output_type": "diff",
          "id": 9086
        },
        "lab02Funcs.py file should have no syntax errors": {
          "stdin": null,
          "args": "python lab02Funcs.py",
          "output_filename": null,
          "source": "stderr",
          "expected": "da39a3ee5e6b4b0d3255bfef95601890afd80709",
          "output_type": "diff",
          "id": 9085
        }
      },
      "id": 2011
    }
  },
  "name": "ccs_cs20_s16_lab05"
}
```



Dear Carson, Nick:

The previous email focused on how to extract "one programming assignment" from submit.cs, and produce, from it, one github repository (which should be a private one) that corresponds to the contents of the programming assignment.

I may or may not have made this clear, but in the new system, the information that an instructor sets up for a given programming assignment lives in a single github repo, rather than in database tables (as in the current submit.cs, and many other competing autograder designs.)  

(My hope is that this particular design decision---which makes it easy to reuse, share, modify, and track changes to programming assignments over time---is going to be one of the most powerful things that makes our approach to autograder design innovative, cool useful, etc.)

Now---a course is a collection of programming assignments.   If each programming assignment corresponds to a repo, then a "collection of programming assignments" corresponds to a "collection of repos", which in github terms is called an "organization".

[Side note: we need to establish what the analogous concept is in gitlab if, in fact, gitlab calls collections of repos something other than "organizations".]

So, if we want to convert all of the programming assignments for a given submit.cs course into the new format, we need to:

(1) Create a github "organization" for the course (one that can contain private repos---that means a github.ucsb.edu organization for now.)

(2) Retrieve the URL for the show page for the course, e.g.

https://submit.cs.ucsb.edu/class/82

(3) From that extract all of the programming assignment ids from that page, e.g. 
708, 706, 705, 707, 709.   In this case, they are all consecutive, but that's only because this is a dummy course that I created for you---for a real course, there will be arbitrary gaps.  (More on how you do this step below).

(4) For each of those, do the steps in the other email to convert that course into a repo in the anacapa grader format. (i.e. a repo that has the JSON and all of the expected files, build files, and execution files.)

To get the project numbers for a given course from the show page for the course, (e.g. https://submit.cs.ucsb.edu/class/82 ) you could do one of two things:


(1) Scrape the HTML---which may not be that hard in this case.

(2) Modify submit.cs to add a https://submit.cs.ucsb.edu/class/82/info
   page that gives you show page for the course in JSON format.

Initially, I thought we were going to need to do 2.

But to be honest, at this point, after looking at it, I'm thinking "scrape the HTML" might be a perfectly reasonable way to go here.    

(That saves us the hassle of having to make a new release of submit.cs, which I am not anxious to take on unless we really, really have to.)

The HTML is reasonably well constrained---you are looking for lines like these:

```html
 <a href="/p/708">ccs_cs20_s16_lab05</a>
 ...
 <a href="/p/706">cs16_lab01</a>
  ...
 <a href="/p/705">cs16_w15_lab00</a>
 ...
 <a href="/p/707">cs32_lab04</a>
 ...
 <a href="/p/709">cs56_f16_lab06</a>
 ...
```


A simple regex that looks for lines that match these, and captures the part after /p/ inside the href attribute is probably all you need.    This could probably be done with a simple script (shell, Python, Ruby, whatever..)

The name (ccs_cs20_s16_lab05) is redundant since you already have that inside the json that you get from retrieving:

 https://submit.cs.ucsb.edu/p/708/info

Again... let me know what questions this brings up for you.

Regards,
Phill 