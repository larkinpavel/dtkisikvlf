from promotional_offer_configurator import *
import pandas as pd

def populate_repository(repository, data):
    for item in data:
        configuration = PromotionalOfferConfiguration()
        configuration.card_type = item[0]
        configuration.region = item[1]
        configuration.merchant_id = item[2]
        configuration.is_enabled = item[3]
        repository.create(configuration)

def color_true_green_false_red(value):
    color = 'black'
    if type(value) == type(True):
        color = "green" if value else "red"
    return f'color: {color}'

def run_test(test_cases):
    for test_case in test_cases:
        repository = TestPromotionalOfferConfigurationRepository()
        data = test_case[0]
        populate_repository(repository, data)
        df = pd.DataFrame(data, columns=["Card Type", "Region", "Merchant ID", "Is enabled"])
        s = df.style.applymap(color_true_green_false_red).hide_index()
        display(s)
        configurator = PromotionalOfferConfigurator(repository)
        card_type = test_case[1][0]
        region = test_case[1][1]
        merchant_id = test_case[1][2]
        actual_result = configurator.is_enabled(card_type, region, merchant_id)
        expected_result = test_case[2]
        print(f'Is configured: card type = {card_type}, region = {region}, merchant ID = {merchant_id}?')
        print(f'Expected: {expected_result}, actual: {actual_result}')