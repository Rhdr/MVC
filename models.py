
class DomainCRUDModel:
    '''Query db and create, read, update & delete domain objects'''

    def __init__(self, session_manager='my_session_manager'):
        print(f'__init__.Model, loading session manager {session_manager}')

    def create_account_bank(self, account_name):
        return DomainAccount(account_name)

    def create_account_advertising(self, account_name):
        return DomainAccount(account_name)

    def create_sourcedoc(self, date, sourcedoc_type):
        return DomainSourcedoc(date, sourcedoc_type)

    def create_lineitem(self, account, account_contra, sourcedoc, dr, cr):
        return DomainLineitem(account, account_contra, sourcedoc, dr, cr)

    '''
    def read(self, domain_obj_name, key_dict):
        print(f'Model - read {domain_obj_name}, {key_dict}')

    def update(self, domain_obj_name, values_dict):
        print(f'Model - update {domain_obj_name}, {values_dict}')

    def delete(self, domain_obj_name):
        print(f'Model - delete {domain_obj_name}')
    '''


class DomainAccount:
    __tablename__ = 'Account_Tbl'

    def __init__(self, account_name):
        self.account_name = account_name


class DomainSourcedoc:
    __tablename__ = 'Sourcedoc_Tbl'

    def __init__(self, date, sourcedoc_type):
        self.date = date
        self.type = sourcedoc_type


class DomainLineitem:
    __tablename__ = 'Lineitem_Tbl'

    def __init__(self, account, account_contra, sourcedoc, dr, cr):
        self.account = account
        self.account_contra = account_contra
        self.sourcedoc = sourcedoc
        self.dr = dr
        self.cr = cr


if __name__ == '__main__':
    crud = DomainCRUDModel()
    acc_b = crud.create_account_bank()
    acc_a = crud.create_account_advertising()
    sd = crud.create_sourcedoc()
    print(crud, acc_b, acc_a, sd)
