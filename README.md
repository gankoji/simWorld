# simWorld

simWorld is exactly that: my attempt at simulating a replica of the
Earth. The aim here is to have an environment within which dynamic
simulations of ground, sea, air, and space vehicles can be created to
serve as testbenches for onboard software algorithm development. 

My primary concern here is to have a platform with which I can study
flight control, navigation, and guidance algorithms for these types of
vehicles. You may find a different use for it, or find it completley
incomprehensible. Either way, I've decided to share it with the
community from an early stage, and will welcome feedback, comments,
and pull requests if anyone decides to provide them. 

# Layout

The basic concept is to have a main simulation program which houses
all the foundational components to a dynamic simulation: environmental
models, such as gravity, magnetosphere, atmosphere, winds aloft, etc;
vehicle models, such as small aircraft, ground vehicles, satellites,
and launch vehicles; ground stations, airfields, etc; 

While, as mentioned above, the intent here is to have a platform on
which to build studies of algorithms for the vehicles and other
actors, there are some key points of the simulation that I'll also be
tackling that seem to come up any time one attempts a simulation of
this sort:

1) Data management
2) Clock management (in particular, cross domain clocking)
3) Post processing and inspection

While there are some software packages out there that do a reasonable
job at some or all of these items, such as Simulink, I've chosen to
look at solving these problems in an open-source fashion. 

# The Foundations

Mainly I've chosen to do so to shed the burden of ever-increasing
software licensing fees for such proprietary toolboxes, but I'm also
motivated simply by the fact that environments such as MATLAB or
Mathematica aren't conducive to good software practices, like version
control (Simulink in particular is terrible for this), heterogeneous
data handling/post processing, and of course cleaning up after
yourself and not crashing a box after consuming its memory.

Since we're after open source technologies as a base, and I have a
great deal of experience with it, Python seemed like a great place to
start. It's faster than the above mentioned "scientific" computing
platforms, open-source, and well-maintained. NumPy and SciPy are
obvious additions here. Additionally, I'm currently working to bring
good use to the HDF5 file standard (along with Python's excellent
integration, h5py) to the sim, to facilitate items 1 and 3 above. 

While Python has reasonably good plotting facilities via MatPlotLib, I
do also anticipate a use for other more robust visualization
facilities for things like flows, vector fields and dynamic
manifolds. I've used ParaView for these in the past, although I've yet
to reevaluate it in this context versus its alternatives. 

UPDATE: I have chosen to bring into the fold the Atmosphere tables
from the website Public Domain Aeronautical Software (PDAS) here: # simWorld

simWorld is exactly that: my attempt at simulating a replica of the
Earth. The aim here is to have an environment within which dynamic
simulations of ground, sea, air, and space vehicles can be created to
serve as testbenches for onboard software algorithm development. 

My primary concern here is to have a platform with which I can study
flight control, navigation, and guidance algorithms for these types of
vehicles. You may find a different use for it, or find it completley
incomprehensible. Either way, I've decided to share it with the
community from an early stage, and will welcome feedback, comments,
and pull requests if anyone decides to provide them. 

# Layout

The basic concept is to have a main simulation program which houses
all the foundational components to a dynamic simulation: environmental
models, such as gravity, magnetosphere, atmosphere, winds aloft, etc;
vehicle models, such as small aircraft, ground vehicles, satellites,
and launch vehicles; ground stations, airfields, etc; 

While, as mentioned above, the intent here is to have a platform on
which to build studies of algorithms for the vehicles and other
actors, there are some key points of the simulation that I'll also be
tackling that seem to come up any time one attempts a simulation of
this sort:

1) Data management
2) Clock management (in particular, cross domain clocking)
3) Post processing and inspection

While there are some software packages out there that do a reasonable
job at some or all of these items, such as Simulink, I've chosen to
look at solving these problems in an open-source fashion. 

# The Foundations

Mainly I've chosen to do so to shed the burden of ever-increasing
software licensing fees for such proprietary toolboxes, but I'm also
motivated simply by the fact that environments such as MATLAB or
Mathematica aren't conducive to good software practices, like version
control (Simulink in particular is terrible for this), heterogeneous
data handling/post processing, and of course cleaning up after
yourself and not crashing a box after consuming its memory.

Since we're after open source technologies as a base, and I have a
great deal of experience with it, Python seemed like a great place to
start. It's faster than the above mentioned "scientific" computing
platforms, open-source, and well-maintained. NumPy and SciPy are
obvious additions here. Additionally, I'm currently working to bring
good use to the HDF5 file standard (along with Python's excellent
integration, h5py) to the sim, to facilitate items 1 and 3 above. 

While Python has reasonably good plotting facilities via MatPlotLib, I
do also anticipate a use for other more robust visualization
facilities for things like flows, vector fields and dynamic
manifolds. I've used ParaView for these in the past, although I've yet
to reevaluate it in this context versus its alternatives. 

UPDATE: I have chosen to bring into the fold the Atmosphere tables
from the website Public Domain Aeronautical Software (PDAS) here:# simWorld

simWorld is exactly that: my attempt at simulating a replica of the
Earth. The aim here is to have an environment within which dynamic
simulations of ground, sea, air, and space vehicles can be created to
serve as testbenches for onboard software algorithm development. 

My primary concern here is to have a platform with which I can study
flight control, navigation, and guidance algorithms for these types of
vehicles. You may find a different use for it, or find it completley
incomprehensible. Either way, I've decided to share it with the
community from an early stage, and will welcome feedback, comments,
and pull requests if anyone decides to provide them. 

# Layout

The basic concept is to have a main simulation program which houses
all the foundational components to a dynamic simulation: environmental
models, such as gravity, magnetosphere, atmosphere, winds aloft, etc;
vehicle models, such as small aircraft, ground vehicles, satellites,
and launch vehicles; ground stations, airfields, etc; 

While, as mentioned above, the intent here is to have a platform on
which to build studies of algorithms for the vehicles and other
actors, there are some key points of the simulation that I'll also be
tackling that seem to come up any time one attempts a simulation of
this sort:

1) Data management
2) Clock management (in particular, cross domain clocking)
3) Post processing and inspection

While there are some software packages out there that do a reasonable
job at some or all of these items, such as Simulink, I've chosen to
look at solving these problems in an open-source fashion. 

# The Foundations

Mainly I've chosen to do so to shed the burden of ever-increasing
software licensing fees for such proprietary toolboxes, but I'm also
motivated simply by the fact that environments such as MATLAB or
Mathematica aren't conducive to good software practices, like version
control (Simulink in particular is terrible for this), heterogeneous
data handling/post processing, and of course cleaning up after
yourself and not crashing a box after consuming its memory.

Since we're after open source technologies as a base, and I have a
great deal of experience with it, Python seemed like a great place to
start. It's faster than the above mentioned "scientific" computing
platforms, open-source, and well-maintained. NumPy and SciPy are
obvious additions here. Additionally, I'm currently working to bring
good use to the HDF5 file standard (along with Python's excellent
integration, h5py) to the sim, to facilitate items 1 and 3 above. 

While Python has reasonably good plotting facilities via MatPlotLib, I
do also anticipate a use for other more robust visualization
facilities for things like flows, vector fields and dynamic
manifolds. I've used ParaView for these in the past, although I've yet
to reevaluate it in this context versus its alternatives. 

UPDATE: I have chosen to bring into the fold the Atmosphere tables
from the website Public Domain Aeronautical Software (PDAS) here:# simWorld

simWorld is exactly that: my attempt at simulating a replica of the
Earth. The aim here is to have an environment within which dynamic
simulations of ground, sea, air, and space vehicles can be created to
serve as testbenches for onboard software algorithm development. 

My primary concern here is to have a platform with which I can study
flight control, navigation, and guidance algorithms for these types of
vehicles. You may find a different use for it, or find it completley
incomprehensible. Either way, I've decided to share it with the
community from an early stage, and will welcome feedback, comments,
and pull requests if anyone decides to provide them. 

# Layout

The basic concept is to have a main simulation program which houses
all the foundational components to a dynamic simulation: environmental
models, such as gravity, magnetosphere, atmosphere, winds aloft, etc;
vehicle models, such as small aircraft, ground vehicles, satellites,
and launch vehicles; ground stations, airfields, etc; 

While, as mentioned above, the intent here is to have a platform on
which to build studies of algorithms for the vehicles and other
actors, there are some key points of the simulation that I'll also be
tackling that seem to come up any time one attempts a simulation of
this sort:

1) Data management
2) Clock management (in particular, cross domain clocking)
3) Post processing and inspection

While there are some software packages out there that do a reasonable
job at some or all of these items, such as Simulink, I've chosen to
look at solving these problems in an open-source fashion. 

# The Foundations

Mainly I've chosen to do so to shed the burden of ever-increasing
software licensing fees for such proprietary toolboxes, but I'm also
motivated simply by the fact that environments such as MATLAB or
Mathematica aren't conducive to good software practices, like version
control (Simulink in particular is terrible for this), heterogeneous
data handling/post processing, and of course cleaning up after
yourself and not crashing a box after consuming its memory.

Since we're after open source technologies as a base, and I have a
great deal of experience with it, Python seemed like a great place to
start. It's faster than the above mentioned "scientific" computing
platforms, open-source, and well-maintained. NumPy and SciPy are
obvious additions here. Additionally, I'm currently working to bring
good use to the HDF5 file standard (along with Python's excellent
integration, h5py) to the sim, to facilitate items 1 and 3 above. 

While Python has reasonably good plotting facilities via MatPlotLib, I
do also anticipate a use for other more robust visualization
facilities for things like flows, vector fields and dynamic
manifolds. I've used ParaView for these in the past, although I've yet
to reevaluate it in this context versus its alternatives. 

UPDATE: I have chosen to bring into the fold the Atmosphere tables
from the website Public Domain Aeronautical Software (PDAS) here:
http://www.pdas.com/atmosdef.html. This is a nice implementation of
the US76 standard atmosphere model, and I see no reason to replicate
the work if it's already out in the public domain. Credit and thanks
go to the author, which according to that webpage is Ralph
Carmichael. Credit is also due to Rich Kwan, who made the Python 2+3
version of the table generators, which is what I have lifted from to
create an object in the sim with the tables which interpolates based
on input altitude.

# Roadmap

As of this writing, very little of this simulation actually exists. I
have a good number of pieces floating around on my disk here that I'm
slowly working toward coalescing into a decent framework, but
currently there's only a very rudimentary 6 DoF EOM class that will be
committed. In no particular order, the rest of the "basic framework"
I'll be attempting to roll out will look something like this: 

Vehicle Components
- EOM
- Dynamics
- Aero
- Propulsion
- Power/Fuel Systems
- Mass Properties
- Payloads
  - Digital/Analog Interfaces (Cross Domain clocking and data passing)
  - Sensing Equipment
	- Imaging
	- Radar
	- IMUs
	- GNSS
	- Radio Navigation
		- VOR/ILS
		- LORAN

Simulation Components
- Gravity Model
- Atmosphere
- Terrain and Collision
- Winds
- Weather (Precipitation and Occlusion)
- Celestial Objects
  - Star Map
  - GNSS Constellations
	- Signal Paths and Characteristics
  - Local Celestial Bodies
	- Their Perturbations/Attraction Fields
