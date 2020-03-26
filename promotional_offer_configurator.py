from datetime import datetime


class PromotionalOfferConfiguration:
    def __init__(self):
        self.card_type = 0
        self.region = 0
        self.merchant_id = 0
        self.is_enabled = False
        self.mod_by = ''
        self.mod_date = datetime.today()

class PromotionalOfferConfigurationRepository:
    def create(self, promotionalOfferConfiguration: PromotionalOfferConfiguration):
        pass

    def get_by_card_type_region_and_merchant(self, card_type: int, region: int, merchant_id: int) -> PromotionalOfferConfiguration:
        pass


class TestPromotionalOfferConfigurationRepository(PromotionalOfferConfigurationRepository):
    def __init__(self):
        self.collection = []

    def create(self, promotionalOfferConfiguration: PromotionalOfferConfiguration):
        self.collection.append(promotionalOfferConfiguration)

    def get_by_card_type_region_and_merchant(self, card_type: int, region: int, merchant_id: int) -> PromotionalOfferConfiguration:
        return next(
            filter(lambda x: x.card_type == card_type and x.region == region and x.merchant_id == merchant_id, self.collection),
            None)


class PromotionalOfferConfigurator:
    def __init__(self, repository: PromotionalOfferConfigurationRepository):
        self.repository = repository

    def is_enabled(self, card_type, merchant_region, merchant_id) -> bool:
        configuration = self.repository.get_by_card_type_region_and_merchant(card_type, merchant_region, merchant_id)
        if configuration is not None:
            return configuration.is_enabled

        configuration = self.repository.get_by_card_type_region_and_merchant(card_type, 0, merchant_id)
        if configuration is not None:
            return configuration.is_enabled

        configuration = self.repository.get_by_card_type_region_and_merchant(card_type, merchant_region, 0)
        if configuration is not None:
            return configuration.is_enabled

        configuration = self.repository.get_by_card_type_region_and_merchant(card_type, 0, 0)
        if configuration is not None:
            return configuration.is_enabled

        return False
