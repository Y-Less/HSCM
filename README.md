HSCM
====

Haskell Code Metrics.

Tools
=====

This folder contains a Python script I wrote for Notepad++ which automatically commits changes to GIT every time a file is saved.  This could be seen as a little bit annoying, but it does have some advantages.  It is important to note that commits in GIT are local, they are not pushed to the remote server individually; you can stage multiple commits and push them all together.  A similar system in SVN for example would be very annoying.  The other advantages are:

1. Automatic backup: Your files are now already in two places on your hard drive.  Not *brilliant* backup, but better than just one copy.

2. Enhanced rollback: You don't loose any state (or VERY little state).

3. Traceability: The real reason I created this plugin was to improve automated analysis of revisions.

The one downside that I've noticed to this (almost INSTANTLY) is that previously I would hit "Ctrl-S" almost every line typed, I'm now just slightly hesitating each time.

Scripts
-------

As mentioned, the tools use a combination of Python with the Notepad++ python script and batch files.  The former allows for interaction with the user within Notepad++ (to get the commit messages).  The latter runs a number of console commands in sequence to commit a git repository on any disk; this is an important requirement from my personal testing and is no less portable than pure Python code - at least when on Windows.

Traceability
------------

In his doctoral work, Ryder used CVS logs of software to track which functions had been fixed or improved and mapped that data to approximate complexity of the function to validate correlations.  This method, with it's prefix keywords, allows for more automated and fine-grained analysis of the code.

Keywords
--------

Every commit has an associated message, and each message has one of the following prefixes followed by a colon (case insensitive):

* BUG: This is a bug-fix commit.  An automated script metrics tool can extract this information to compare two versions and see which functions were fixed, comparing that data to the percieved complexity of said function(s).

* REF or REFACTOR: This is a change to existing code for other reasons.  The original thesis noted that bug fixes may be invisibly included in refactoring if, for example, the change was done to fix a class of issues difficult to fix under an older structure.

* FEAT or FEATURE: Implements a new feature.  This creates a base case for comparing something.

* STRUC or STRUCTURE: A change in the structure of the repository itself (adding folders or files).

* DOC or DOCUMENTATION: Adding documentation to something.  Does this reduce percieved complexity?  Possibly.

* IN or INT or INTERIM: This is a change caused by saving a file mid edit, leaving it in an unstable state.  These should not be pushed remotely and should be ignored during automatic analysis.  So, for example, comparing changes in a BUG commit should compare to the last commit before any INTERIM commits.  This exists simply because ALL saves are committed but sometimes you want to save a file you are still working on.  For this reason an interim message is the default, but that does mean you need to be careful when saving to actually enter a new message as appropriate.
