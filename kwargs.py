from dataclasses import dataclass

dataclass(init=False)


class User:
    def set_values(self, **kwargs):
        # for example set_values(age=21, initials='GS')
        # source: https://stackoverflow.com/questions/8187082/how-can-you-set-class-attributes-from-variable-arguments-kwargs-in-python

        # all keys
        # self.__dict__.update(kwargs)

        # with filter keys
        allowed_keys = {'age', 'name'}
        self.__dict__.update((k, v) for k, v in kwargs.items() if k in allowed_keys)

    def display(self):
        if self.age:
            print(self.__dict__)

    _id: str
    first_name: str
    last_name: str
    initials: str
    age: int
    pics: dict


def buy(**shoppinglist):
    for name, qty in shoppinglist.items():
        print('{}: {}'.format(name, qty))


buy(apple=4, eggs=21, bananas='No')

user = User()
user.set_values(age=53, no_good=4342, name='gal')
user.display()
