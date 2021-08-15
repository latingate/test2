class User:
    def set_values(self, **kwargs):
        # all keys
        # self.__dict__.update(kwargs)

        # only specific allowed keys
        allowed_keys = {'name', 'age'}
        self.__dict__.update((k, v) for k, v in kwargs.items() if k in allowed_keys)

    def display(self):
        print(self.__dict__)

    name: str
    age: int


user = User()
user.set_values(age=53, not_displayed='not displayed if filtered', name='gal')
user.display()


def buy(**shoppinglist):
    for name, qty in shoppinglist.items():
        print('{}: {}'.format(name, qty))


buy(apple=4, eggs=21, bananas='No')
