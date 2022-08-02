from brownie import depositor, accounts

def main():
    acc = accounts.load('deployment_account')
    depositor.deploy({'from': acc})