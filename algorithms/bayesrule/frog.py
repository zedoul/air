# http://www.uio.no/studier/emner/matnat/ibv/BIO4040/h03/undervisningsmateriale/Lectures/lecture10.pdf

import random

# likelihoods are constant
p_1_given_a = 0.6
p_0_given_a = 1 - p_1_given_a
p_1_given_b = 0.4
p_0_given_b = 1 - p_1_given_b

# prior are flexiable

p_a = 0.5
p_b = 0.5

def bayesrule(prior, likelihood, marginal):
    return prior * likelihood / marginal

def marginal(event):
    if event == 1 :
        return p_a * p_1_given_a + p_b * p_1_given_b
    else :
        return p_a * p_0_given_a + p_b * p_0_given_b

observation = []
for i in range(10):
    event = random.randint(0, 1)
    observation.append(event)

    if event == 1 :
        pos_a = bayesrule(p_a, p_1_given_a, marginal(event))
        pos_b = bayesrule(p_b, p_1_given_b, marginal(event))
    else :
        pos_a = bayesrule(p_a, p_0_given_a, marginal(event))
        pos_b = bayesrule(p_b, p_0_given_b, marginal(event))
    p_a = pos_a
    p_b = pos_b

print "So, the object would be A or B?"
print "observation", observation
print "prior of A : ", p_a
print "prior of B : ", p_b
print "Bayesian statistics is to find which class would be sufficient for the object we are observing now"
