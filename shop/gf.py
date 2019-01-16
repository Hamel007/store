from random import random


class RandomNumberView(object):

    def get_context_data(self, **kwargs):
        context = super(RandomNumberView, self).get_context_data(**kwargs)
        context['number'] = random.randrange(1, 100)
        # return context
        print('ghghgh')