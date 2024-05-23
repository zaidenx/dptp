def remove(c, l):
  """
  Remove a literal from a clause.

  Arguments:
    c: a clause (of type set)
    l: a literal

  Returns:
    the input clause with l removed
  """
  try:
    c.remove(l)
    return c
  except:
    return c

def union(c1, c2):
  """
  Union two clauses. Assume the input clauses are consistent.

  Arguments:
    c1: the first clause
    c2: the second clause

  Returns:
    the union of c1 and c2, or None if the union is inconsistent
  """
  res = c1 | c2;
  for l in res:
    if -l in res:
      return None
  return res

def conditioning(cs, l):
  """
  Perform conditioning of a CNF cs on a literal l and return the result.

  Arguments:
    cs: a CNF
    l: a literal

  Returns:
    conditioning cs on l
  """
  res = []
  for c in cs:
    if l in c: continue
    if -l in c:
      res.append(remove(c, -l))
    else:
      res.append(c)
  return res

def parse(file):
  """
  Parse a CNF file in DIMACS format.

  Arguments:
    file: a CNF file in DIMACS format

  Returns:
    a tuple (nvs, ncs, cs) where nvs is the number of variables,
    ncs is the number of clauses, cs is a sequence of clauses
  """
  cs = []
  nvs = 0
  ncs = 0
  with open(file, "r") as lines:
    for line in lines:
      if line.startswith("c "): pass
      elif line.startswith("p cnf "):
        tokens = line.split(" ")
        nvs = int(tokens[2])
        ncs = int(tokens[3])
      else:
        ls = [int(l) for l in line.split(" ")[:-1]]
        cs.append(set(ls))
  return (nvs, ncs, cs)

def to_dimacs(cs):
  lines = []
  nvars = max([max([abs(l) for l in c]) for c in cs])
  ncls = len(cs)
  lines.append(f"p cnf {nvars} {ncls}")
  for c in cs:
    line = " ".join([str(l) for l in c])
    lines.append(f"{line} 0")
  return "\n".join(lines)
