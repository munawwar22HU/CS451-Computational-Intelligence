from EA import *
# FPS and FPS
f = EA(FitnessProportionSelect(),FitnessProportionSelect(),num_gen=1000)
f.initialize(KnapSackProblem,'DataSet/f2_l-d_kp_20_878',True)
f.RunAlt('Tables/Knapsack/fps_fps')

#FPS and Random
f = EA(FitnessProportionSelect(),RandomSelect(),num_gen=1000)
f.initialize(KnapSackProblem,'DataSet/f2_l-d_kp_20_878',True)
f.RunAlt('Tables/Knapsack/fps_rand')

# Binary Tournament and Truncation
f = EA(BinaryTournamentSelect(),TruncationSelect(),num_gen=1000)
f.initialize(KnapSackProblem,'DataSet/f2_l-d_kp_20_878',True)
f.RunAlt('Tables/Knapsack/bt_trunc')

#Truncation and Truncation
f = EA(TruncationSelect(),TruncationSelect(),num_gen=1000)
f.initialize(KnapSackProblem,'DataSet/f2_l-d_kp_20_878',True)
f.RunAlt('Tables/Knapsack/trunc_trunc')

# Random and Random 
f = EA(RandomSelect(),RandomSelect(),num_gen=1000)
f.initialize(KnapSackProblem,'DataSet/f2_l-d_kp_20_878',True)
f.RunAlt('Tables/Knapsack/rand_rand')

# FPS and Truncation

f = EA(FitnessProportionSelect(),TruncationSelect(),num_gen=1000)
f.initialize(KnapSackProblem,'DataSet/f2_l-d_kp_20_878',True)
f.RunAlt('Tables/Knapsack/fps_trunc')
 
#RBS and Binary Tournament

f = EA(RankBasedSelect(),BinaryTournamentSelect(),num_gen=1000)
f.initialize(KnapSackProblem,'DataSet/f2_l-d_kp_20_878',True)
f.RunAlt('Tables/Knapsack/rbs_bt')

# Random and Truncation

f = EA(RandomSelect(),TruncationSelect(),num_gen=1000)
f.initialize(KnapSackProblem,'DataSet/f2_l-d_kp_20_878',True)
f.RunAlt('Tables/Knapsack/rand_trunc')


 