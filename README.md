# Collaboration / workflow practice for final project

The purpose of this repo is to give you the opportunity to set up a
collaborative workflow and practice using it without polluting your actual
project repository for the class. You will also be using this as an opportunity
to implement programatic downloading and verification of your data. These are
important for reproducibility and will be required of your final project; so 
we figured it be good to get you in the habit of practicing it now.

## Setup

**Do not clone this directly from the berkeley-stat159 organization!**

First, break up into your teams. If your actual project team mates are not in
the same lab session as you, just join the others sitting around you. You won't
be working on your projects directly, so you don't have to be in your project
teams.

Now, select one member from your group to be your "collaboration host". This 
person will *fork* from `https://github.com/berkeley-stat159/lab6_exercise.git`

Everyone else in the group will now fork from your collaboration host's fork.
We're doing it this way so each group can have the same starting point, but all
of the practice work from each group is contained within that group.

Once everyone has forked correctly, every group member should clone from their
fork and set up their remotes like we did in class on Thursday. You should have
two remotes, one pointing to your fork and another pointing to your 
collaboration host's fork (you don't need to have a remote pointing to the 
original berkeley-stat159 repo for the exercise).

## Tasks

 - [ ] Add a `data` directory to the project. Create a `.gitignore` and add the
       `data` directory to it so any data files stored in that directory will
       be ignored by github

 - [ ] Implement functions to download and verify data. The prototypes for these
       functions can be found in `src`

       - You may want to split your group into subgroups and have each 
         subgroup work on a different task. Don't forget about branching so you
	 can have multiple parallel lines of development.

 - [ ] Practice code review via pull requests. Make sure that your 
       implementations run on every group memeber's system (cross-platform
       compatibility is important)
