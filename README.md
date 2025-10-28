# Introduction
Solitary confinement is often criticized as being one of the most cruel punishments utilized by the U.S. Criminal Justice System. In it, individuals are deprived of human contact and, as a result, can develop disorders that prevent them from reintegrating into society. This study sought to establish whether the opposite of that punishment might therefore have the opposite effect. Specifically, it examines the effect of community groups — such as religious or educational groups — on rule violation rates in correctional facilities.

# Methods 
Here, we analyzed the “Survey of Inmates in State and Federal Correctional Facilities, 2004” by the Bureau of Justice and Statistics. It includes 14,499 x 3,000 data entries of incarcerated individuals in state facilities. We chose the 2004 version because, unlike others, it included a “Facility ID,” which we controlled for. Note: we used state not federal facilities, as this provided a geographic distribution. We relied on a logistic regression to model correlation between involvement in community groups and rule violations. We also controlled for confounding variables (race, Hispanic, sentence length, sex, age, U.S. born, age at first arrest, marital status, Facility ID).

# Results 
The results of this study were unambiguous and contrary to our hypothesis: involvement in any community group is correlated with an increase in overall rule violation rates, some of which (education, inmate assistance, child-rearing, life skills, and race/ethnic) were statistically significant (p<0.05). This is evident both in the disparity between the rule violation rates of group members versus non-group members as well as in the statistical analysis. To better show these results, we include the following sample comparison showing the group with the highest percentage difference: the GED group. Separately, this study also finds that, while involvement in community groups is correlated with a statistically significant (p<0.05) greater rate of rule violations, it is also correlated with a smaller rate of certain major rule violations (albeit with a less significant p-value). We conducted this analysis by using a Zero-Inflated Negative Binomial distribution on the violation category with the highest number of entries: “Other Major Rule Violations.”This yielded us the following statistical output. 

<img width="641" height="406" alt="Zero-Inflated Negative Binomial of Other Major Rule Violations" src="https://github.com/user-attachments/assets/65b2bcb3-d150-4244-b70b-8643175799d5" />

This shows that, for “other major rule violations” (including slowdowns, food strikes, setting fires, rioting, etc.), certain community groups, specifically educational, life skills, religious, and self-help, correlated with a decrease in rule violations. However, this is only statistically significant for self-help groups (p = 0.046) and almost statistically significant for educational groups (p= 0.052).

### Other Significant Figures

<img width="1470" height="939" alt="Control Variables with Odds Ratios" src="https://github.com/user-attachments/assets/25410a17-9b95-4385-96a9-5ab1bbf9c996" />

# Future Directions
Future Directions One research opportunity worth exploring consists in abstracting the data to state-level recidivism rates as related to state-level availability of communities. Here, we identified the state (location) of each facility through the mode pre-incarceration residence of its incarcerated population. While this is only an estimate, it does seem to be relatively accurate. Using this information, future studies can analyze if there is a correlation between state community group involvement rates and their recidivism rates in 2004. This could give more meaningful results by using recidivism instead of rule violations, but it would also serve to understand the availability of community groups in prisons around the United States.

# Limitations
### Binary Output
Only having a binary output (violation or no violation) limited the nuance of our study. There was a related question with a count, for which we tested a negative binomial regression on. However, the results here were largely insignificant (pseudo-r < 0.05) as almost all the responses were clustered around 0 and were self-reported which introduced a lot more random error.

### Commitment to Groups
We were also limited by a lack of data on the amount of time in groups. For instance, someone who only attended one religious group meeting would still count as a member. This likely skewed our results towards a positive correlation.

### Timing of Violations
The lack of timing data for rule violations also limited our findings as it prevented us from differentiating between someone who joined a group after committing a violation from one who committed a violation after joining a group. In doing so, this limitation likely skewed our results towards a positive correlation.

### Availability of Community
Groups and Security Level Because of the anonymous nature of the survey, there was no way of discriminating between facilities with respect to their availability of community groups and to security level. Controlling for Facility ID would not prevent this, as a maximum security prison with no rule violations and no community groups would count the same as a prison where no one joined community groups and still did not commit rule violations. This likely skewed our results towards a positive correlation.
