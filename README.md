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

## Primary Tasks

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

## Secondary Tasks

If you manage to implement and review all of the functions in 
`src/data_acquisition.py`, then move on to the in class example on 
[hemodynamic response functions](http://www.jarrodmillman.com/rcsds/lectures/convolution_background.html).

Start by using your `data_acquisition` module to download and save the 
necessary modules to your `src/` directiory. You might start by downloading the
[stimuli.py](http://www.jarrodmillman.com/rcsds/_downloads/stimuli.py)and
[pearson.py](http://www.jarrodmillman.com/rcsds/_downloads/pearson_solutions.py)
modules. You will also need to download the 
[condition file](http://www.jarrodmillman.com/rcsds/_downloads/ds114_sub009_t2r1_cond.txt)
to your `data/` directory.

Once you have all the tools you need, collaborate with your group to follow the
[convolution lecture](http://www.jarrodmillman.com/rcsds/lectures/convolution_background.html)
and create an HRF. Having constructed the HRF, apply the pearson correlation
analysis using the HRF as the correlate rather than the binary task on/off
condition.
