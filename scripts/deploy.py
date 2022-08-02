from brownie import sampleToken, accounts

def main():
    acc = accounts.load('deployment_account')
    sampleToken.deploy("My ERC20 Token", "MET", 18, 1e28, {'from': acc})