#!/usr/bin/env python3

from argparse import ArgumentParser
from cnf import *

verbose = False


def resolve(c1, c2, v):
    b1= (v in c1) and (-v in c2)
    b2= (-v in c1) and(v in c2)
    if not (b1 or b2): return None
    c = c1 | c2
    c.remove(v)
    c.remove(-v)
    for x in c:
        if -x in c:
            return None
    return c


def evaluate(cs, assignment):
    for c in cs:
        c_sat = False
        for l in c:
            if l in assignment:
              c_sat = True
              break
        if not c_sat: return False
    return True

# TODO: implement this function
def decision_procedure(cs, nvs):
  """
  Decides the satisfiability of a given CNF formula.

  Arguments:
    cs: a list of sets of literals
    nvs: the number of variables

  Returns:
    (True, assignment) if the CNF formula is satisfiable,
    and otherwise (False, None)
  """
  resolved = cs
  to_be_resolved = cs
  """
  while True:
      round_resolved = []
      for c1 in to_be_resolved:
          for c2 in resolved:
              for v in range(1, nvs + 1):
                  res = resolve(c1, c2, v)
                  if res == None: continue
                  if verbose:
                      print(f"resolved {res} from clauses {c1} and {c2} on variable {v}")
                  if len(res) == 0: return(False,None)
                  if res not in resolved:
                      round_resolved.append(res)
      if not round_resolved:
          break
      resolved.extend(round_resolved)
      to_be_resolved = round_resolved
      #return(True, None)
  #2**nvs = 2^nvs
"""

  i = 0
  m = 2**nvs
  while i < m:
      tmp = i
      assignment = []
  # v= 1,2,3,...,nvs
      for v in range(1, nvs + 1):
          if tmp % 2 == 0:
              assignment.append(-v)
          else:
              assignment.append(v)
          tmp = tmp // 2
      if verbose:
          print("Assignment:", assignment)
      if evaluate(cs, assignment):
          return (True, assignment)
      i = i + 1
  return (False, None)
def main():
  global verbose
  parser = ArgumentParser(description="Check the satisfiability of a CNF formula in DIMACS format.")
  parser.add_argument("file", nargs="?", help="a file in DIMACS format")
  parser.add_argument("--verbose", action="store_true", help="display verbose messages")
  args = parser.parse_args()
  if args.verbose:
    verbose = True
  if args.file:
    (nvs, ncs, cs) = parse(args.file)
    (sat, assignment) = decision_procedure(cs, nvs)
    if sat:
      print("s SATISFIABLE")
      if assignment is not None:
        print("v {} 0".format(" ".join([str(v) for v in assignment])))
    else:
      print("s UNSATISFIABLE")
  else:
    cs = [set({-1, 2}), set({-1, 3}), set({-2, 4}), set({-3, -4}), set({1, -3, 5})]
    print(f"result: {decision_procedure(cs, 5)}")
    print()

if __name__ == "__main__":
  main()
