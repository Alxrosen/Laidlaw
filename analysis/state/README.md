# Future Directions: 
One research opportunity worth exploring consists in abstracting the data to state-level recidivism rates as related to state-level availability of communities. Here, we identified the state (location) of each facility through the mode pre-incarceration residence of its incarcerated population. While this is only an estimate, it does seem to be relatively accurate. Using this information, future studies can analyze if there is a correlation between state community group involvement rates and their recidivism rates in 2004. This could give more meaningful results by using recidivism instead of rule violations, but it would also serve to understand the availability of community groups in prisons around the United States.


#### Project Notes: 
In order to do this, I'll have to run through the 10-item list of all of the community groups that we have identified:
    - child rearing
    - education & GED
    - inmate assistance
    - life skills
    - pre-release
    - race/ethnic
    - religion
    - self-help
    - vocation

Then, I can create a proportion by state to see which ones have inmates that are most likely to participate in these programs. The only problem that I see with that approach is the following:

    1. We may not have a representative sample of the states. The prisons that chose to comply with the survey may have better quality programs for their populations, while the ones that don't may choose not to publicize that information. This would result in the participating prisons having a misrepresentative number of these programs. However, I think that the biggest result of this would just bigger numbers accross the board, which may not necessarily skew it too much. 

    2. Large prisons might be more likely (because they have more resources; presumably better access to communities) to participate in this study, and because they are bigger, they may have more members participating. This would result in there being greater community representation that would exist otherwise. I can see this being particularly misrepresentative for small states, where their big prisons are much more likely to participate, and therefore small prisons being relatively glossed over. Then again, I need to look at how the selection for the prisons and inamtes looks again. One potential way to get around this would be to look at this by facility and THEN find a ratio of facilities by state that offer community programs

#### Project to-do 

This is my plan of action:

    Create a network of all of the facilities that give their incarcerated population access to these community groups. This should be a matrix of 10 (communities) x all of the unique facility IDs. 

    THEN, find the state that each facility corresponds to by looking at the mode state residency of its citizens. 
    
        This is going to be difficult, and you'll have to do a few tests to make sure that the results make sense. 
