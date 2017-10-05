#! /usr/bin/env python
# coding:utf-8
# Author qingniao


class AttribDict(dict):
    def __init__(self, indict=None):
        if indict is None:
            indict = {}
        dict.__init__(self, indict)
        self.__initialised = True

    def __getattr__(self, item):
        """
        Maps values to attributes
        Only called if there *is NOT* an attribute with this name
        """

        try:
            return self.__getitem__(item)
        except KeyError:
            raise AttributeError("unable to access item '%s'" % item)

    def __setattr__(self, item, value):
            """
            Maps attributes to values
            Only if we are initialised
            """

            # This test allows attributes to be set in the __init__ method
            if "_AttribDict__initialised" not in self.__dict__:
                return dict.__setattr__(self, item, value)

            # Any normal attributes are handled normally
            elif item in self.__dict__:
                dict.__setattr__(self, item, value)

            else:
                self.__setitem__(item, value)

    def __getstate__(self):
        return self.__dict__

    def __setstate__(self, dict):
        self.__dict__ = dict


if __name__ == '__main__':
    pass
