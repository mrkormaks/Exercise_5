def SynchronizingTables(N, ids, salary):
	correctSalaryList = []
	idsSorted = []
	salarySorted = []

	idsSorted = sorted(ids)
	salarySorted = sorted(salary)
	for i in range(N):
		for j in range(N):
			if idsSorted[j] == ids[i]:
				correctSalaryList.append(salarySorted[j])
	return(correctSalaryList)
