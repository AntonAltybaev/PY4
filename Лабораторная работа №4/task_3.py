def delete(list_, index=None):
    return list_[0:index] + list_[index + 1:] if index is not None else list_[:len(list_) - 1]




print(delete([0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 2], index=1))  # [0, 2]
print(delete([0, 1, 2]))  # [0, 1]
