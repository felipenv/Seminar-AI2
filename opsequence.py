from ortools.constraint_solver import pywrapcp
import numpy as np
import random

def main():
  # Start the solver.
  solver = pywrapcp.Solver('jobshop')
  resources_count = 3
  jobs_count = 3
  all_resources = range(0, resources_count)
  all_jobs = range(0, jobs_count)
  process_dict = {'0': '12', '1': '19', '2': '23'}
  # Declare data.
  resources1 = [[0,1,2],[2,0,1],[1,2,0]]
  resources2 = [[1,2,0],[2,0,1],[0,1,2]]
  resources3 = [[2,1,0],[1,0,2],[0,2,1]]
  resources4 = [[1,0,2],[0,2,1],[2,1,0]]
  #resources5 = [[0,0,0],[1,1,1],[2,2,2]]
  #resources6 = [[0,1,2],[0,1,2],[0,1,2]]
  resource = [resources1,resources2,resources3,resources4]
  resources = random.choice(resource)
  processing_times = [[5,7,8],[7,8,5],[8,5,7]]
  sequence_matrix = []
  
  # Computes makespan.
  makespan = 0
  for i in all_jobs:
    makespan += sum(processing_times[i])
  # Creates jobs.
  all_tasks = {}
  for i in all_jobs:
    for j in range(0, len(resources[i])):
      all_tasks[(i, j)] = solver.FixedDurationIntervalVar(0,
                                                          makespan,
                                                          processing_times[i][j],
                                                          False,
                                                          '%s' % (process_dict[str(i)]))

  # Creates sequence variables and add disjunctive constraints.
  all_sequences = []
  all_resources_jobs = []
  for i in all_resources:

    resources_jobs = []
    for j in all_jobs:
      for k in range(0, len(resources[j])):        
        if resources[j][k] == i:
          resources_jobs.append(all_tasks[(j, k)])
    disj = solver.DisjunctiveConstraint(resources_jobs, 'resource %i' % i)
    all_sequences.append(disj.SequenceVar())
    solver.Add(disj)

  # Add conjunctive contraints.
  for i in all_jobs:
    for j in range(0, len(resources[i]) - 1):
      solver.Add(all_tasks[(i, j + 1)].StartsAfterEnd(all_tasks[(i, j)]))
    #Add custom constraints  
      #solver.Add(all_tasks[(0,0)].StartsAfterEnd(all_tasks[(0,2)]))
      #solver.Add(all_tasks[(1,1)].StartsAfterEnd(all_tasks[(1,2)]))
      #solver.Add(all_tasks[(2,0)].StartsAfterEnd(all_tasks[(2,2)]))
  # Set the objective.
  obj_var = solver.Max([all_tasks[(i, len(resources[i])-1)].EndExpr()
                        for i in all_jobs])
  objective_monitor = solver.Minimize(obj_var, 1)
  # search phases.
  sequence_phase = solver.Phase([all_sequences[i] for i in all_resources],
                                solver.SEQUENCE_DEFAULT)
  vars_phase = solver.Phase([obj_var],
                            solver.CHOOSE_FIRST_UNBOUND,
                            solver.ASSIGN_MIN_VALUE)
  main_phase = solver.Compose([sequence_phase, vars_phase])
  # solution collector.
  collector = solver.LastSolutionCollector()

  # Add the interesting variables to the SolutionCollector.
  collector.Add(all_sequences)
  collector.AddObjective(obj_var)

  for i in all_resources:
    sequence = all_sequences[i];
    sequence_count = sequence.Size();
    for j in range(0, sequence_count):
      t = sequence.Interval(j)
      collector.Add(t.StartExpr().Var())
      collector.Add(t.EndExpr().Var())
  # Solving.
  disp_col_width = 10
  if solver.Solve(main_phase, [objective_monitor, collector]):
    
    sol_line = ""
    sol_line_tasks = ""
    
    for i in all_resources:
      seq = all_sequences[i]
      sequence = collector.ForwardSequence(0, seq)
      seq_size = len(sequence)

      for j in range(0, seq_size):
        t = seq.Interval(sequence[j]);
        sol_line_tasks +=  t.Name() + " " * (disp_col_width - len(t.Name()))

      for j in range(0, seq_size):
        t = seq.Interval(sequence[j]);
        sol_tmp = "[" + str(collector.Value(0, t.StartExpr().Var())) + ","
        sol_tmp += str(collector.Value(0, t.EndExpr().Var())) + "] "
        sol_line += sol_tmp + " " * (disp_col_width - len(sol_tmp))

      sol_line += "\n"
      sol_line_tasks += "\n"

      sequence_matrix = sol_line_tasks
    print(sequence_matrix)
  

if __name__ == '__main__':
  main()
