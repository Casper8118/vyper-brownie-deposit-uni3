from brownie import sampleToken, accounts

def main():
    token_contract = sampleToken.at("0x102274b543E86e5aa6a2e80e1Fbc37C3ed127638")
    sampleToken.publish_source(token_contract)