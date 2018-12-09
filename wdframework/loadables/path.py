import types


def path(relative_path):
    def decorate(cls):
        class LoadableClass(cls):
            print(cls)
            setattr(cls, "__relative_path", relative_path)
        return LoadableClass
    return decorate

#
# def path(relative_path):
#     def decorate(cls):
#         class LoadableClass(cls):
#             cls.__set_relative_path(relative_path)
#             # setattr(cls, "get_relative_path",
#                     # types.MethodType(get_relative_path, cls))
#         return LoadableClass
#     return decorate
