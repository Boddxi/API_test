import uuid

def get_identificator1() -> str:
    identificator = uuid.uuid4()
    ident = "autotest"
    return ident + str(identificator)[8:]


def get_identificator2() -> str:
    identificator = str(uuid.uuid4())
    ind_list = identificator.split('-')
    ind_list[0] = "autotest"
    return '-'.join(ind_list)


def get_identificator3() -> str:
    identificator = str(uuid.uuid4())
    ind_list = identificator.split('-')
    return identificator.replace(ind_list[0], 'autotest')


autotest_ident1 = get_identificator1()
print(autotest_ident1)

autotest_ident2 = get_identificator2()
print(autotest_ident2)

autotest_ident3 = get_identificator3()
print(autotest_ident3)


