import numpy
import copy


class GA_tutorial:
    def __init__(self, low, high, num_chrm, num_gene, answer, num_parent=2, max_gen=1000, mut_prob=0.05):
        self.low = low
        self.high = high
        self.num_chrm = num_chrm
        self.num_gene = num_gene
        self.answer = answer
        self.num_parent = num_parent
        self.max_gen = max_gen
        self.mut_prob = mut_prob

    def make_param(self):
        self.chrm = np.random.randint(self.low, self.high, size=(self.num_chrm, self.num_gene))

    def fitness_func(self, fit_val):
        for i in np.arange(self.num_chrm):
            a = (self.chrm[i][np.where(self.chrm[i] > self.answer)] - self.answer).sum()
            b = (self.answer - self.chrm[i][np.where(self.chrm[i] <= self.answer)]).sum()
            fit_val[i] = a + b
        return fit_val

    def search_solution(self):
        gen = 1
        fit_val = np.zeros(self.num_chrm)
        while gen <= self.max_gen:

            fit_val = self.fitness_func(fit_val)
            parent_idx = np.argsort(fit_val)[:2]
            fit_prob = fit_val[parent_idx] / fit_val[parent_idx].sum()

            new_chrm = copy.copy(self.chrm)

            if np.where(fit_val == 0)[0].sum() > 0:
                break

            for i in range(self.num_chrm):
                for j in range(self.num_gene):
                    if np.random.random() < self.mut_prob:
                        new_chrm[i][j] = np.random.randint(self.low, self.high)
                    else:
                        new_chrm[i][j] = self.chrm[np.random.choice(parent_idx, p=fit_prob)][j]

            self.chrm = copy.copy(new_chrm)

            print('='*20)
            print(gen, "th Generation : ", self.chrm)
            print('fitness value :', fit_val)
            print('selected parent :', parent_idx)

            gen += 1
        
        
if __name__ == '__main__':
    ga = GA_tutorial(1, 11, 5, 10, 10)
    ga.make_param()
    ga.search_solution()